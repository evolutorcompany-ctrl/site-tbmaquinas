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

text = text.strip()

if text.startswith('"') and text.endswith('"'):
    import ast
    try:
        # Evaluate it as a python string literal!
        decoded = ast.literal_eval(text)
    except:
        # Fallback
        text = text[1:-1]
        decoded = text.replace('\\n', '\n').replace('\\t', '\t').replace('\\"', '"').replace('\\\\', '\\')
    
    font_css = """@font-face {
  font-family: 'mbf-canno';
  src: url('../fonts/mbf-canno.ttf') format('truetype');
  font-weight: normal;
  font-style: normal;
}
"""
    decoded = font_css + decoded
    
    # Check variables
    import re
    decoded = re.sub(r'--primary:\s*#[0-9a-fA-F]+;', '--primary:       #000000;', decoded)
    decoded = re.sub(r'--primary-hover:\s*#[0-9a-fA-F]+;', '--primary-hover: #424449;', decoded)
    decoded = re.sub(r'--accent:\s*#[0-9a-fA-F]+;', '--accent:        #FF7B00;', decoded)
    decoded = re.sub(r'--accent-hover:\s*#[0-9a-fA-F]+;', '--accent-hover:  #e66b00;', decoded)
    decoded = re.sub(r'--light-bg:\s*#[0-9a-fA-F]+;', '--light-bg:      #F5F5F5;', decoded)
    decoded = re.sub(r'--body-text:\s*#[0-9a-fA-F]+;', '--body-text:     #4C4E52;', decoded)
    decoded = re.sub(r'--dark-text:\s*#[0-9a-fA-F]+;', '--dark-text:     #000000;', decoded)
    decoded = re.sub(r'--border:\s*#[0-9a-fA-F]+;', '--border:        #E0E0E0;', decoded)
    decoded = re.sub(r'--topbar-bg:\s*#[0-9a-fA-F]+;', '--topbar-bg:     #000000;', decoded)
    decoded = re.sub(r'--nav-bg:\s*#[0-9a-fA-F]+;', '--nav-bg:        #ffffff;', decoded)
    decoded = re.sub(r'--footer-bg:\s*#[0-9a-fA-F]+;', '--footer-bg:     #000000;', decoded)

    with open(style_path, 'w', encoding='utf-8') as f:
        f.write(decoded)
    print("Foolproof fix successful.")
else:
    print("Not a quoted string anymore?")
