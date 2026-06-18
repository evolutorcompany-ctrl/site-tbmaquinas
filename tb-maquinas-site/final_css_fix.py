import os

out_folder = 'C:/Users/Eduarda/Desktop/projeto Tb Máquinas/tb-maquinas-site'
style_path = os.path.join(out_folder, 'css', 'style.css')

with open(style_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all literal \n with real newlines
fixed = content.replace('\\n', '\n').replace('\\t', '\t').replace('\\"', '"').replace('\\\\', '\\')

with open(style_path, 'w', encoding='utf-8') as f:
    f.write(fixed)

print("Fixed CSS fully!")
