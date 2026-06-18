import os

out_folder = 'C:/Users/Eduarda/Desktop/projeto Tb Máquinas/tb-maquinas-site'
style_path = os.path.join(out_folder, 'css', 'style.css')
with open(style_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Remove the initial `@font-face` block and any quotes if they exist
start_idx = text.find('/* ════')
if start_idx == -1:
    start_idx = text.find('/* ─── VARI')

if start_idx != -1:
    # See if there's a quote right before it
    if text[start_idx-1] == '"':
        start_idx -= 1
        
    text = text[start_idx:]
    
if text.startswith('"') and text.endswith('"'):
    text = text[1:-1]

text = text.replace('\\n', '\n')
text = text.replace('\\t', '\t')
text = text.replace('\\"', '"')
text = text.replace('\\\\', '\\')

font_css = """@font-face {
  font-family: 'mbf-canno';
  src: url('../fonts/mbf-canno.ttf') format('truetype');
  font-weight: normal;
  font-style: normal;
}
"""

text = font_css + text

# Do the replacements
text = text.replace('#021a47', '#000000')
text = text.replace('#031f55', '#424449')
text = text.replace('#ff7e05', '#FF7B00')
text = text.replace('#f27420', '#e66b00')
text = text.replace('rgba(2,26,71,0.04)', '#F5F5F5')
text = text.replace('rgba(2,26,71,0.75)', '#4C4E52')
text = text.replace('rgba(2,26,71,0.12)', '#E0E0E0')
text = text.replace('rgba(2,26,71,0.92)', 'rgba(0,0,0,0.92)')
text = text.replace('rgba(2,26,71,0.72)', 'rgba(0,0,0,0.72)')
text = text.replace('rgba(2,26,71,0.3)', 'rgba(0,0,0,0.3)')
text = text.replace('rgba(2,26,71,0.08)', 'rgba(0,0,0,0.08)')
text = text.replace('rgba(2,26,71,0.06)', 'rgba(0,0,0,0.06)')
text = text.replace('rgba(2,26,71,0.1)', 'rgba(0,0,0,0.1)')

# Also ensure body-text, dark-text, footer-bg are correct if they were #7f7f8a #191919 #111827 from a different template
import re
text = re.sub(r'--primary:\s*#[0-9a-fA-F]+;', '--primary:       #000000;', text)
text = re.sub(r'--primary-hover:\s*#[0-9a-fA-F]+;', '--primary-hover: #424449;', text)
text = re.sub(r'--accent:\s*#[0-9a-fA-F]+;', '--accent:        #FF7B00;', text)
text = re.sub(r'--accent-hover:\s*#[0-9a-fA-F]+;', '--accent-hover:  #e66b00;', text)
text = re.sub(r'--light-bg:\s*#[0-9a-fA-F]+;', '--light-bg:      #F5F5F5;', text)
text = re.sub(r'--body-text:\s*#[0-9a-fA-F]+;', '--body-text:     #4C4E52;', text)
text = re.sub(r'--dark-text:\s*#[0-9a-fA-F]+;', '--dark-text:     #000000;', text)
text = re.sub(r'--border:\s*#[0-9a-fA-F]+;', '--border:        #E0E0E0;', text)
text = re.sub(r'--topbar-bg:\s*#[0-9a-fA-F]+;', '--topbar-bg:     #000000;', text)
text = re.sub(r'--nav-bg:\s*#[0-9a-fA-F]+;', '--nav-bg:        #ffffff;', text)
text = re.sub(r'--footer-bg:\s*#[0-9a-fA-F]+;', '--footer-bg:     #000000;', text)

with open(style_path, 'w', encoding='utf-8') as f:
    f.write(text)
    
print("Brute force applied.")
