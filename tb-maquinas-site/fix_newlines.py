import os
import ast

out_folder = 'C:/Users/Eduarda/Desktop/projeto Tb Máquinas/tb-maquinas-site'
style_path = os.path.join(out_folder, 'css', 'style.css')

with open(style_path, 'r', encoding='utf-8') as f:
    content = f.read()

# content might have @font-face block first, then a big quoted string
parts = content.split('"/*')
if len(parts) > 1:
    font_face = parts[0]
    quoted_part = '"/*' + parts[1]
    
    # if it's literally a string with "\n", ast.literal_eval handles it safely
    # but we might have issues if it's not a perfectly quoted string.
    # Let's clean it manually
    if quoted_part.endswith('"'):
        quoted_part = quoted_part[:-1]
    
    if quoted_part.startswith('"'):
        quoted_part = quoted_part[1:]
    
    # Replace literal \n with real newline
    # Replace literal \t with real tab
    # Replace literal \\ with \
    real_css = quoted_part.replace('\\n', '\n').replace('\\t', '\t').replace('\\"', '"').replace('\\\\', '\\')
    
    final_content = font_face + real_css
    
    with open(style_path, 'w', encoding='utf-8') as f:
        f.write(final_content)
    print("Fixed newlines!")
else:
    print("No quoted /* found, nothing to fix.")
