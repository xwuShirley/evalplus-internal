import requests
import os
from loguru import logger
PULSAR=int(os.environ.get('PULSAR', 0))
PULSAR_PORT = os.environ.get('PULSAR_PORT', '80')
from transformers import AutoTokenizer
def generate_pulsar(model,
                    messages, 
                    cocurrency=1, 
                    logprobs=0,
                    max_tokens =2048, 
                    temperature=0.7,
                    do_sample = True,
                    base_instruction=None, 
                    tokenizer=None):
    if tokenizer is None:
        tokenizer = AutoTokenizer.from_pretrained('/storage/workspaces/meta-llama/Meta-Llama-3.1-8B-Instruct')
    messages = [{'role': 'user', 'content': messages}]
    prompt = tokenizer.apply_chat_template(messages, \
                                        tokenize=False, \
                                        add_generation_prompt=True)  
              
    res = requests.post(f'http://127.0.0.1:{PULSAR_PORT}/generate', json={
            "inputs": prompt,
            "parameters":{
                "max_new_tokens": max_tokens, 
                "do_sample": (temperature != 0), 
                "temperature": (1 if temperature == 0 else temperature),
                "frequency_penalty": 0.0,
                "n": cocurrency,
                "logprobs": logprobs,
            }
        }, headers={}
    )
    if 'error' in res.json():
        logger.error(res.json())
    #import pdb;pdb.set_trace()
    returned = res.json()
    tokens_encoded = returned["usage"]["prompt_tokens"]
    tokens_generated = returned["usage"]["completion_tokens"]
    try:
        cur_logprobs = res.json()['choices'][0]['logprobs']
        cur_outputs = [choice['message']['content'] for choice in res.json()['choices']]  
    except KeyError:
        cur_logprobs = 0
        cur_outputs = [returned['generated_text']] 
    return cur_outputs, tokens_generated



def generate_together(model,
                    messages, 
                    cocurrency=1, 
                    logprobs=0,
                    max_tokens =2048, 
                    temperature=0.7,
                    do_sample = True,
                    base_instruction=None, 
                    tokenizer=None):
    messages = [{'role': 'user', 'content': messages}]
    endpoint = 'https://api.together.xyz/v1/chat/completions'
    if not do_sample:
        temperature = 1.0
    res = requests.post(endpoint, json={
        "model": model,
        "max_tokens": max_tokens,
        "do_sample": do_sample,
        "temperature": temperature,
        "messages": messages,
        "n": cocurrency,
        "logprobs": logprobs,}, headers={
            "Authorization": f"Bearer {os.environ['TOGETHER_API_KEY']}",
    })
    #
    if 'error' in res.json():
        logger.error(res.json())
        if res.json()['error']['type'] == 'invalid_request_error':
            logger.info("Input + output is longer than max_position_id.")
            # if halfed<4:
            #     max_tokens = max_tokens/2
            #     halfed+=1
            # else:
            #     logger.info("fall back to default mode")
            messages = base_instruction
    returned = res.json()
    tokens_encoded = returned["usage"]["prompt_tokens"]
    tokens_generated = returned["usage"]["completion_tokens"]
    try:
        cur_logprobs = res.json()['choices'][0]['logprobs']
        cur_outputs = [choice['message']['content'] for choice in res.json()['choices']]  
    except KeyError:
        cur_logprobs = 0
        cur_outputs = returned['generated_text'] 
    return cur_outputs, tokens_generated