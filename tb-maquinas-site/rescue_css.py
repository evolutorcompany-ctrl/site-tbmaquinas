import json
import os
import ast

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
    # If best_code starts with quote and ends with quote, it is a JSON literal string
    # Let's decode it safely
    if isinstance(best_code, str):
        # Even if it's string, we can try to JSON parse it if it's double-encoded
        if best_code.startswith('"') and best_code.endswith('"'):
            try:
                best_code = json.loads(best_code)
            except:
                try:
                    best_code = ast.literal_eval(best_code)
                except:
                    pass
    
    # Re-apply color theme replacements properly
    font_css = """@font-face {
  font-family: 'mbf-canno';
  src: url('../fonts/mbf-canno.ttf') format('truetype');
  font-weight: normal;
  font-style: normal;
}
"""
    if 'mbf-canno' not in best_code:
        best_code = font_css + best_code

    css = best_code
    css = css.replace('#021a47', '#000000')
    css = css.replace('#031f55', '#424449')
    css = css.replace('#ff7e05', '#FF7B00')
    css = css.replace('#f27420', '#e66b00')
    css = css.replace('rgba(2,26,71,0.04)', '#F5F5F5')
    css = css.replace('rgba(2,26,71,0.75)', '#4C4E52')
    css = css.replace('rgba(2,26,71,0.12)', '#E0E0E0')
    css = css.replace('rgba(2,26,71,0.92)', 'rgba(0,0,0,0.92)')
    css = css.replace('rgba(2,26,71,0.72)', 'rgba(0,0,0,0.72)')
    css = css.replace('rgba(2,26,71,0.3)', 'rgba(0,0,0,0.3)')
    css = css.replace('rgba(2,26,71,0.08)', 'rgba(0,0,0,0.08)')
    css = css.replace('rgba(2,26,71,0.06)', 'rgba(0,0,0,0.06)')
    css = css.replace('rgba(2,26,71,0.1)', 'rgba(0,0,0,0.1)')

    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(css)
    print("Perfectly rescued style.css and applied theme!")
else:
    print("Failed to find style.css")
