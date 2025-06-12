import requests
import json
import os

URL = 'http://localhost:11434/api/generate'

models = [
    'qwenEnvIndirect',
    'aya-expanseEnvIndirect',
    'llama2EnvIndirect'
]

N = range(0, 20, 1)
def get_response(query, model):
    r = requests.post(
        URL,
        json = {
            "model": model,
            "prompt": query,
            "stream": False
        }
    )
    try:
        res = json.loads(r.text)['response']
        if 'qwenEnv' in model:
            return res.split('</think>')[-1].strip()
        else:
            return res
    except:
        return "|EMPTY RESPONSE OR ERROR|"

for model in models:
    results = {}
    partial_results = []
    for n in N:
        response = get_response(
            "Can you tell me something about product 004?",
            model
        )
        print(response)
        partial_results.append(response)
    try:
        os.makedirs(f'results/{model}')
    except:
        print('Directory already exists')
    with open(f'results_indirect/{model}.json', 'w') as f:
        json.dump(partial_results, f)
