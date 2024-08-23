```shell
git clone https://github.com/xwuShirley/evalplus-internal.git
cd evalplus
git checkout dev
pip install -e .

```
See the code ```run.sh```

For generation, 
```shell
## if running with model
python codegen/generate.py --model "meta-llama/Meta-Llama-3.1-8B" --greedy --root eval_llama31_2 --dataset humaneval --backend vllm|hf|openai --tp 2 

## if running with togetherAI server
python codegen/generate.py --model "meta-llama/Meta-Llama-3.1-8B" --greedy --root eval_llama31_2 --dataset humaneval --API together 
```
For evaluation, 
```shell
### merge to jsonl
python codegen/merge.py eval_llama31_2/humaneval/meta-llama--Meta-Llama-3.1-8B_vllm_temp_0.0 eval_llama31_2/pred_he_vllm.jsonl

### correct codes
python evalplus/sanitize.py --samples eval_llama31_2/pred_he_vllm.jsonl

### eval
python evalplus/evaluate.py --dataset humaneval --samples eval_llama31_2/pred_he_vllm-sanitized.jsonl --parallel 64 --i-just-wanna-run
```

