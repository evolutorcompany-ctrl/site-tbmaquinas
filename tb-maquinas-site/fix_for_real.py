import os
out_folder = 'C:/Users/Eduarda/Desktop/projeto Tb Máquinas/tb-maquinas-site'
style_path = os.path.join(out_folder, 'css', 'style.css')
with open(style_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Fix the font-face prepended part
if text.startswith('@font-face'):
    parts = text.split('"/*')
    if len(parts) > 1:
        text = '"/*' + parts[1]

# Now text should be exactly the JSON string literal
if text.startswith('"') and text.endswith('"'):
    # Safe manual un-escaping
    # Strip the surrounding quotes
    text = text[1:-1]
    
    # Replace the \n literals
    text = text.replace('\\n', '\n')
    text = text.replace('\\t', '\t')
    text = text.replace('\\"', '"')
    text = text.replace('\\\\', '\\')
    
# Prepend font
font_css = """@font-face {
  font-family: 'mbf-canno';
  src: url('../fonts/mbf-canno.ttf') format('truetype');
  font-weight: normal;
  font-style: normal;
}
"""
text = font_css + text

with open(style_path, 'w', encoding='utf-8') as f:
    f.write(text)
    
print("Fixed for real.")
