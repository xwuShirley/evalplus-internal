Result_Path=/home/shirley/codes/evalplus/results-mbpp-8b/
TMP_NAME=eval_llama31_2
dataset=mbpp #humaneval
mkdir -p ${Result_Path}/${TMP_NAME}
export TOGETHER_API_KEY=485b6501ee67cc885f14bf500a77e9e0c696ce7c3967be1b44e1e6836061c7c2
python codegen/generate.py --model "meta-llama/Meta-Llama-3.1-8B-Instruct" \
--greedy --root ${Result_Path}/${TMP_NAME} \
--dataset mbpp --API together &> ${Result_Path}/${TMP_NAME}.log  #--backend vllm --tp 1

root=${Result_Path}/${TMP_NAME}/${dataset}


Name=meta-llama--Meta-Llama-3.1-8B-Instruct_vllm_temp_0.0 #deepseek-ai--deepseek-coder-6.7b-base_vllm_temp_0.0 
ls ${root}/${Name}
python codegen/merge.py ${root}/${Name} ${root}/${Name}.jsonl &>> ${Result_Path}/${TMP_NAME}_eval.log

cat ${root}/${Name}.jsonl
echo ${root}/${Name}.jsonl
python evalplus/sanitize.py --samples ${root}/${Name}.jsonl &>> ${Result_Path}/${TMP_NAME}_eval.log


python evalplus/evaluate.py --dataset ${dataset} --samples ${root}/${Name}.jsonl &>> ${Result_Path}/${TMP_NAME}_eval.log
