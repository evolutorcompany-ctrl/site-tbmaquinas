import json

log_file = r'C:\Users\Eduarda\.gemini\antigravity-ide\brain\15aeaaf5-8d7c-4601-8996-3eb62895f64b\.system_generated\logs\transcript.jsonl'
out_path = 'C:/Users/Eduarda/Desktop/projeto Tb Máquinas/tb-maquinas-site/css/style.css'

best_code = None

with open(log_file, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            entry = json.loads(line)
            if 'tool_calls' in entry:
                for tc in entry['tool_calls']:
                    tc_str = str(tc)
                    if 'write_to_file' in tc_str or 'replace_file_content' in tc_str:
                        args = tc.get('arguments', {})
                        if not args and 'args' in tc:
                            args = tc['args']
                        if type(args) == str:
                            try:
                                args = json.loads(args)
                            except:
                                pass
                        if type(args) == dict:
                            tgt = args.get('TargetFile', '')
                            if 'style.css' in tgt:
                                if 'CodeContent' in args:
                                    best_code = args['CodeContent']
        except Exception:
            pass

if best_code:
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(best_code)
    print("Recovered style.css!")
else:
    print("Could not find style.css in transcript.")
