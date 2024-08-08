# codegen/merge.py
import sys, json, os
from natsort import natsorted

if __name__ == '__main__':
    
    input_dir = sys.argv[1]
    output_file = sys.argv[2]

    with open(output_file, 'w') as f:
        f.write('')

    for task in natsorted(os.listdir(input_dir)):
        task_dir = os.path.join(input_dir, task)
        if not os.path.isdir(task_dir):
            continue
        input_file = os.path.join(task_dir, '0.py')
        with open(input_file, 'r') as f:
            code = f.read()
        task_id = task.replace('_', '/')
        info = {
            'task_id': task_id,
            'solution': code,
        }
        with open(output_file, 'a') as f:
            f.write(json.dumps(info) + '\n')