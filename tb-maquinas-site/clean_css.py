import json
import os

log_file = r'C:\Users\Eduarda\.gemini\antigravity-ide\brain\15aeaaf5-8d7c-4601-8996-3eb62895f64b\.system_generated\logs\transcript.jsonl'
out_path = 'C:/Users/Eduarda/Desktop/projeto Tb Máquinas/tb-maquinas-site/css/style.css'

best_code = None

with open(log_file, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            entry = json.loads(line)
            if 'tool_calls' in entry:
                for tc in entry['tool_calls']:
                    args = tc.get('arguments', {})
                    if not args and 'args' in tc:
                        args = tc['args']
                    
                    if isinstance(args, str):
                        try:
                            args = json.loads(args)
                        except:
                            continue
                            
                    if isinstance(args, dict):
                        tgt = args.get('TargetFile', '')
                        if tgt and 'style.css' in tgt:
                            if 'CodeContent' in args:
                                best_code = args['CodeContent']
        except Exception:
            pass

if best_code:
    # write original css perfectly
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(best_code)
    print("Perfectly recovered style.css!")
else:
    print("Failed to find style.css")
