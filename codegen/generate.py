import json
import os
from os import PathLike
from typing import List

from model import DecoderBase, make_model
from rich.progress import (
    BarColumn,
    MofNCompleteColumn,
    Progress,
    TextColumn,
    TimeElapsedColumn,
)
from server import generate_together, generate_pulsar
import re
def extract_python_code(text):
    # Use regular expression to match code block inside triple backticks
    if "```python" in text:
        pattern = r'```python(.*?)```'
        match = re.search(pattern, text, re.DOTALL)
        if match:
            return match.group(1).strip()
        else:
            return text
    else:
        return text
def construct_contract_prompt(prompt: str, contract_type: str, contract: str) -> str:
    if contract_type == "none":
        return prompt
    elif contract_type == "docstring":
        # embed within the docstring
        sep = ""
        if '"""' in prompt:
            sep = '"""'
        elif "'''" in prompt:
            sep = "'''"
        assert sep != ""
        l = prompt.split(sep)
        contract = "\n".join([x.split("#")[0] for x in contract.splitlines()])
        l[1] = (
            l[1] + contract + "\n" + " " * (len(contract) - len(contract.lstrip()) - 1)
        )
        return sep.join(l)
    elif contract_type == "code":
        # at the beginning of the function
        contract = "\n".join([x.split("#")[0] for x in contract.splitlines()])
        return prompt + contract


def codegen(
    target_path: PathLike,
    model: DecoderBase,
    dataset: str,
    greedy=False,
    n_samples=1,
    id_range=None,
    version="default",
    resume=True,
    API=None,
):
    task2nexist = {}
    if resume and target_path.endswith(".jsonl") and os.path.isfile(target_path):
        with open(target_path, "r") as f:
            for line in f:
                if not line.strip():
                    continue
                task_id = json.loads(line)["task_id"]
                task2nexist[task_id] = task2nexist.get(task_id, 0) + 1

    with Progress(
        TextColumn(f"{dataset} •" + "[progress.percentage]{task.percentage:>3.0f}%"),
        BarColumn(),
        MofNCompleteColumn(),
        TextColumn("•"),
        TimeElapsedColumn(),
    ) as p:
        if dataset == "humaneval":
            from evalplus.data import get_human_eval_plus

            dataset = get_human_eval_plus(version=version)
        elif dataset == "mbpp":
            from evalplus.data import get_mbpp_plus

            dataset = get_mbpp_plus(version=version)

        for task_id, task in p.track(dataset.items()):
            if id_range is not None:
                id_num = int(task_id.split("/")[1])
                low, high = id_range
                if id_num < low or id_num >= high:
                    p.console.print(f"Skipping {task_id} as it is not in {id_range}")
                    continue

            if not target_path.endswith(".jsonl"):
                p_name = task_id.replace("/", "_")
                os.makedirs(os.path.join(target_path, p_name), exist_ok=True)
                task2nexist[task_id] = len(
                    [
                        f
                        for f in os.listdir(os.path.join(target_path, p_name))
                        if f.endswith(".py")
                    ]
                )

            n_more_samples = n_samples
            log = f"Codegen: {task_id} @ {model}"
            if resume and task2nexist.get(task_id, 0) > 0:
                log += f" (resuming from {task2nexist[task_id]})"
                n_more_samples -= task2nexist[task_id]

            p.console.print(log)

            sidx = n_samples - n_more_samples
            while sidx < n_samples:
                prompt = task["prompt"].strip() + "\n"

                temperature = 0
                if API is None:
                    
                    outputs = model.codegen(
                        prompt,
                        do_sample=not greedy,
                        num_samples=n_samples - sidx,
                    )
                    assert outputs, "No outputs from model!"
                    for impl in outputs:
                        solution = (
                            prompt + impl if model.is_direct_completion() else impl
                        )
                        solution = extract_python_code(solution)
                        if target_path.endswith(".jsonl"):
                            with open(target_path, "a") as f:
                                f.write(
                                    json.dumps({"task_id": task_id, "solution": solution})
                                    + "\n"
                                )
                        else:
                            with open(
                                os.path.join(target_path, p_name, f"{sidx}.py"),
                                "w",
                                encoding="utf-8",
                            ) as f:
                                f.write(solution)
                        sidx += 1

                else:
                    if API == "together":
                        decoded = generate_together(
                            "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
                            prompt,
                            cocurrency=1, 
                            max_tokens = 2049,
                            do_sample = (temperature != 0), 
                            temperature = temperature
                            )
                    else:
                        decoded = generate_pulsar(
                            "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
                            prompt,
                            cocurrency=1, 
                            max_tokens = 2049,
                            do_sample = (temperature != 0), 
                            temperature = temperature
                            )
                    print (decoded[0][0])
                    outputs = [extract_python_code(decoded[0][0]),]
                    #import pdb;pdb.set_trace()
                    #print (outputs)
                    assert outputs, "No outputs from model!"
                    for impl in outputs:
                        if model is not None:
                            solution = (prompt + impl if model.is_direct_completion() else impl)
                        else:
                            solution = impl

                        if target_path.endswith(".jsonl"):
                            with open(target_path, "a") as f:
                                f.write(
                                    json.dumps({"task_id": task_id, "solution": solution})
                                    + "\n"
                                )
                        else:
                            with open(
                                os.path.join(target_path, p_name, f"{sidx}.py"),
                                "w",
                                encoding="utf-8",
                            ) as f:
                                f.write(solution)
                        sidx += 1
                    #import pdb;pdb.set_trace()


def main(
    model: str,
    dataset: str,
    root: str,
    bs: int = 1,
    n_samples: int = 1,
    temperature: float = 0.0,
    resume: bool = True,
    greedy: bool = False,
    id_range: List = None,
    version: str = "default",
    backend: str = "vllm",
    base_url: str = None,
    tp: int = 1,
    evalperf_type: str = None,  # This is for EvalPerf
    jsonl_fmt: bool = False,
    API: str = None, 
):
    assert dataset in ["humaneval", "mbpp"], f"Invalid dataset {dataset}"
    assert backend in ["vllm", "hf", "openai"]
    assert evalperf_type is None or evalperf_type in [
        "instruct",
        "perf-instruct",
        "perf-CoT",
    ]

    if greedy and (temperature != 0 or bs != 1 or n_samples != 1):
        temperature = 0.0
        bs = 1
        n_samples = 1
        print("Greedy decoding ON (--greedy): setting bs=1, n_samples=1, temperature=0")

    if id_range is not None:
        assert len(id_range) == 2, "id_range must be a list of length 2"
        assert id_range[0] < id_range[1], "id_range must be increasing"
        id_range = tuple(id_range)

    # Make project dir
    os.makedirs(root, exist_ok=True)
    # Make dataset dir
    os.makedirs(os.path.join(root, dataset), exist_ok=True)

    # Model instructions
    instruction_prefix = "Please provide a self-contained Python script that solves the following problem in a markdown code block:"
    response_prefix = "Below is a Python script with a self-contained function that solves the problem and passes corresponding tests:"

    if evalperf_type == "perf-instruct":
        instruction_prefix = "Please provide an efficient and self-contained Python script that solves the following problem in a markdown code block:"
        response_prefix = "Below is a Python script with a self-contained function that efficiently solves the problem and passes corresponding tests:"
    elif evalperf_type == "perf-CoT":
        instruction_prefix = "Think step by step: please provide an efficient and self-contained Python script that solves the following problem in a markdown code block:"
        response_prefix = "Below is a Python script with a self-contained function that efficiently solves the problem and passes corresponding tests:"
    elif evalperf_type is not None and evalperf_type != "instruct":
        raise ValueError(f"Invalid evalperf_type: {evalperf_type}")

    # Model creation
    if API is None:
        model_runner = make_model(
            model=model,
            backend=backend,
            batch_size=bs,
            temperature=temperature,
            dataset=dataset,
            base_url=base_url,
            tp=tp,
            instruction_prefix=instruction_prefix,
            response_prefix=response_prefix,
        )
    else:
        model_runner = None

    # Make dir for codes generated by each model
    identifier = model.replace("/", "--") + f"_{backend}_temp_{temperature}"
    if evalperf_type:
        identifier += f"-{evalperf_type}"

    target_path = os.path.join(root, dataset, identifier)
    if jsonl_fmt:
        target_path += ".jsonl"
    else:
        os.makedirs(target_path, exist_ok=True)
    codegen(
        target_path=target_path,
        dataset=dataset,
        greedy=greedy,
        model=model_runner,
        n_samples=n_samples,
        resume=resume,
        id_range=id_range,
        version=version,
        API = API
    )


if __name__ == "__main__":
    from fire import Fire

    Fire(main)
