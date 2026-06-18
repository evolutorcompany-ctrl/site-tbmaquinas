import os
import re

out_folder = 'C:/Users/Eduarda/Desktop/projeto Tb Máquinas/tb-maquinas-site'

# 1. Update style.css
style_path = os.path.join(out_folder, 'css', 'style.css')
with open(style_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace :root variables
css = re.sub(r'--primary:\s*#[0-9a-fA-F]+;', '--primary:       #000000;', css)
css = re.sub(r'--primary-hover:\s*#[0-9a-fA-F]+;', '--primary-hover: #424449;', css)
css = re.sub(r'--accent:\s*#[0-9a-fA-F]+;', '--accent:        #FF7B00;', css)
css = re.sub(r'--accent-hover:\s*#[0-9a-fA-F]+;', '--accent-hover:  #e66b00;', css)
css = re.sub(r'--light-bg:\s*rgba[^;]+;', '--light-bg:      #424449;', css)
css = re.sub(r'--body-text:\s*rgba[^;]+;', '--body-text:     #cccccc;', css)
css = re.sub(r'--dark-text:\s*#[0-9a-fA-F]+;', '--dark-text:     #ffffff;', css)
css = re.sub(r'--border:\s*rgba[^;]+;', '--border:        #4C4E52;', css)
css = re.sub(r'--topbar-bg:\s*#[0-9a-fA-F]+;', '--topbar-bg:     #000000;', css)
css = re.sub(r'--nav-bg:\s*#[0-9a-fA-F]+;', '--nav-bg:        #000000;', css)
css = re.sub(r'--footer-bg:\s*#[0-9a-fA-F]+;', '--footer-bg:     #000000;', css)

# Body background
css = re.sub(r'background:\s*var\(--white\);', 'background: #000000;', css)

# Replace dark text on black
css = css.replace('color: var(--primary);', 'color: var(--white);')
css = css.replace('color: var(--dark-text);', 'color: var(--white);')
# Reset btn-outline to use white
css = re.sub(r'\.btn-outline\s*{[^}]+}', r'.btn-outline { background: transparent; color: var(--white); border-color: #4C4E52; }', css)
css = re.sub(r'\.btn-outline:hover\s*{[^}]+}', r'.btn-outline:hover { background: #424449; color: var(--white); transform: translateY(-2px); }', css)

# Nav link active/hover
css = css.replace('color: var(--primary);', 'color: var(--white);')

# Replace rgba(2,26,71...) with rgba(0,0,0...) or rgba(255,255,255...)
css = css.replace('rgba(2,26,71,0.04)', '#424449')
css = css.replace('rgba(2,26,71,0.75)', '#cccccc')
css = css.replace('rgba(2,26,71,0.12)', '#4C4E52')
css = css.replace('rgba(2,26,71,0.92)', 'rgba(0,0,0,0.92)')
css = css.replace('rgba(2,26,71,0.72)', 'rgba(0,0,0,0.72)')
css = css.replace('rgba(2,26,71,0.3)', 'rgba(0,0,0,0.3)')
css = css.replace('rgba(2,26,71,0.08)', '#424449')
css = css.replace('rgba(2,26,71,0.06)', '#424449')
css = css.replace('rgba(2,26,71,0.1)', 'rgba(255,255,255,0.1)')

# Specific color fixes
css = css.replace('#031f55', '#424449')
css = css.replace('#021a47', '#000000')

# Product card backgrounds
css = re.sub(r'\.product-card\s*{[^}]+}', r'.product-card { background: #424449; border: 1px solid var(--border); border-radius: var(--radius-lg); overflow: hidden; transition: var(--transition); display: flex; flex-direction: column; }', css)

with open(style_path, 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Process HTML files for Logo and Icons
for fname in os.listdir(out_folder):
    if not fname.endswith('.html'):
        continue
        
    path = os.path.join(out_folder, fname)
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Footer Logo
    # Current logo uses `images/logomarca.png`
    html = html.replace('images/logomarca.png', 'images/produtos/logo_topo_menor.png')

    # Fix inline hardcoded colors if any (e.g. style="color: #fff;")
    # Fix icons in contato.html
    if fname == 'contato.html':
        # Remove background:var(--accent);color:#fff; from icons
        html = html.replace('style="background:var(--accent);color:#fff;"', '')
        # Form card background fix
        html = html.replace('background: var(--white);', 'background: #424449;')
        html = html.replace('color: var(--dark-text);', 'color: #ffffff;')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

print("Theme updated successfully!")
