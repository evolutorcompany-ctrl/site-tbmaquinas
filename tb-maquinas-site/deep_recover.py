import json
import os
import re

# Search both conversation transcripts for the full CSS content
transcript_files = [
    r'C:\Users\Eduarda\.gemini\antigravity-ide\brain\15aeaaf5-8d7c-4601-8996-3eb62895f64b\.system_generated\logs\transcript.jsonl',
    r'C:\Users\Eduarda\.gemini\antigravity-ide\brain\2d8cf88d-ef3c-4434-ac52-14f46a91ba27\.system_generated\logs\transcript.jsonl'
]

out_path = r'C:\Users\Eduarda\Desktop\projeto Tb Máquinas\tb-maquinas-site\css\style.css'

best_css = None
best_line_count = 0

for tpath in transcript_files:
    if not os.path.exists(tpath):
        print(f"Not found: {tpath}")
        continue
    print(f"Scanning: {tpath}")
    with open(tpath, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                entry = json.loads(line)
                
                # Check tool_calls for write_to_file or replace_file_content for style.css
                if 'tool_calls' in entry:
                    for tc in entry['tool_calls']:
                        args = tc.get('arguments', {})
                        if isinstance(args, str):
                            try:
                                args = json.loads(args)
                            except:
                                continue
                        if isinstance(args, dict):
                            tgt = args.get('TargetFile', '') or args.get('target_file', '')
                            if 'style.css' in str(tgt) and '.backup' not in str(tgt):
                                code = args.get('CodeContent') or args.get('code_content')
                                if code and isinstance(code, str):
                                    lc = len(code.splitlines())
                                    print(f"  Found write_to_file with {lc} lines")
                                    if lc > best_line_count:
                                        best_line_count = lc
                                        best_css = code
                                
                                # Also check ReplacementContent for replace_file_content
                                rc = args.get('ReplacementContent')
                                if rc and isinstance(rc, str) and len(rc.splitlines()) > best_line_count:
                                    best_line_count = len(rc.splitlines())
                                    best_css = rc
                
                # Check for view_file outputs that show the full CSS
                content = entry.get('content', '')
                if isinstance(content, str) and 'Showing lines 1 to 800' in content and 'style.css' in content and '/* ─── BASE' in content:
                    # This is a view_file response — extract the CSS portion
                    # Try to grab just the numbered lines
                    match = re.search(r'((?:^\d+: .*$\n)+)', content, re.MULTILINE)
                    if match:
                        numbered = match.group(0)
                        # Remove line numbers
                        css_lines = re.sub(r'^\d+: ', '', numbered, flags=re.MULTILINE)
                        lc = len(css_lines.splitlines())
                        print(f"  Found view_file response with {lc} lines")
                        
            except Exception as e:
                pass

print()
if best_css:
    print(f"Best CSS found: {best_line_count} lines")
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(best_css)
    print("Written to style.css")
else:
    print("No suitable CSS found.")
