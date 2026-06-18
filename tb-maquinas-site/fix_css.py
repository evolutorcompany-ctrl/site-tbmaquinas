import json
import os

out_folder = 'C:/Users/Eduarda/Desktop/projeto Tb Máquinas/tb-maquinas-site'
style_path = os.path.join(out_folder, 'css', 'style.css')

with open(style_path, 'r', encoding='utf-8') as f:
    content = f.read()

# It has @font-face at the top, then a quoted string with literal \n
# Let's extract the quoted part
start_quote = content.find('"/*')
if start_quote != -1:
    quoted_content = content[start_quote:]
    # Remove surrounding quotes and decode \n
    if quoted_content.startswith('"') and quoted_content.endswith('"'):
        quoted_content = quoted_content[1:-1]
    
    # decode literal \n to actual newlines
    # Also decode other escapes
    # The safest way is to use json.loads
    try:
        decoded_content = json.loads('"' + quoted_content.replace('"', '\\"') + '"')
    except:
        decoded_content = quoted_content.encode('utf-8').decode('unicode_escape')
    
    font_face = content[:start_quote]
    
    final_content = font_face + decoded_content
    
    with open(style_path, 'w', encoding='utf-8') as f:
        f.write(final_content)
    print("Fixed CSS file.")
else:
    print("No quoted string found, maybe it's already fine?")
