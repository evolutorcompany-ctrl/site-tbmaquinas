import json
import os

log_file = r'C:\Users\Eduarda\.gemini\antigravity-ide\brain\2d8cf88d-ef3c-4434-ac52-14f46a91ba27\.system_generated\logs\transcript.jsonl'
out_path = 'C:/Users/Eduarda/Desktop/projeto Tb Máquinas/tb-maquinas-site/css/style.css.backup'

with open(log_file, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            entry = json.loads(line)
            if entry.get('type') == 'VIEW_FILE_RESPONSE' or 'output' in entry.get('content', ''):
                pass
            # Or just search strings:
            if '/* ─── BASE ──────' in line and 'body {' in line:
                # We found the response!
                content = entry.get('content')
                if isinstance(content, dict) and 'output' in content:
                    with open(out_path, 'w', encoding='utf-8') as out:
                        out.write(content['output'])
                    print("Found in output!")
                    break
                elif isinstance(content, str):
                    with open(out_path, 'w', encoding='utf-8') as out:
                        out.write(content)
                    print("Found in string content!")
                    break
        except Exception as e:
            pass
