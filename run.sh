Result_Path=/home/shirley/codes/evalplus/results-70b/
TMP_NAME=eval_llama31_1
mkdir -p ${Result_Path}/${TMP_NAME}
export TOGETHER_API_KEY=485b6501ee67cc885f14bf500a77e9e0c696ce7c3967be1b44e1e6836061c7c2
python codegen/generate.py --model "meta-llama/Meta-Llama-3.1-70B-Instruct" \
--greedy --root ${Result_Path}/${TMP_NAME} \
--dataset humaneval --API together &> ${Result_Path}/${TMP_NAME}.log  #--backend vllm --tp 1

# # Result_Path=/home/shirley/codes/evalplus/humaneval/eval_llama31_2/humaneval
# Result_Path=/home/shirley/codes/evalplus/eval_llama31_2b/humaneval/
# Name=meta-llama--Meta-Llama-3.1-8B-Instruct_vllm_temp_0.0 #deepseek-ai--deepseek-coder-6.7b-base_vllm_temp_0.0 
# ls ${Result_Path}/${Name}
# python codegen/merge.py ${Result_Path}/${Name} ${Result_Path}/${Name}.jsonl

# cat ${Result_Path}/${Name}.jsonl
# echo ${Result_Path}/${Name}.jsonl
# # # #/home/shirley/codes/evalplus/humaneval/meta-llama--Meta-Llama-3.1-8B_vllm_temp_0.0.jsonl
# python evalplus/sanitize.py --samples ${Result_Path}/${Name}.jsonl


# python evalplus/evaluate.py --dataset humaneval --samples ${Result_Path}/${Name}.jsonl