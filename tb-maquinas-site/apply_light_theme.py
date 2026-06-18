import os

out_folder = 'C:/Users/Eduarda/Desktop/projeto Tb Máquinas/tb-maquinas-site'

# 1. Update style.css
style_path = os.path.join(out_folder, 'css', 'style.css')
with open(style_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Re-add font if missing
if '@font-face' not in css or 'mbf-canno' not in css:
    font_css = """
@font-face {
  font-family: 'mbf-canno';
  src: url('../fonts/mbf-canno.ttf') format('truetype');
  font-weight: normal;
  font-style: normal;
}
"""
    css = font_css + css

# Replace Blue with Black/Gray
css = css.replace('#021a47', '#000000')
css = css.replace('#031f55', '#424449')

# Replace Old Orange with New Orange
css = css.replace('#ff7e05', '#FF7B00')
css = css.replace('#f27420', '#e66b00')

# Replace rgba variations of Blue with Black/Gray variations
css = css.replace('rgba(2,26,71,0.04)', '#F5F5F5') # Light background
css = css.replace('rgba(2,26,71,0.75)', '#4C4E52') # Body text
css = css.replace('rgba(2,26,71,0.12)', '#E0E0E0') # Borders
css = css.replace('rgba(2,26,71,0.92)', 'rgba(0,0,0,0.92)')
css = css.replace('rgba(2,26,71,0.72)', 'rgba(0,0,0,0.72)')
css = css.replace('rgba(2,26,71,0.3)', 'rgba(0,0,0,0.3)')
css = css.replace('rgba(2,26,71,0.08)', 'rgba(0,0,0,0.08)')
css = css.replace('rgba(2,26,71,0.06)', 'rgba(0,0,0,0.06)')
css = css.replace('rgba(2,26,71,0.1)', 'rgba(0,0,0,0.1)')

# Make sure --body-text uses the precise variable requested or gray
# Replace any lingering --light-bg to use #F5F5F5 if missed
css = css.replace('--light-bg:      rgba(0,0,0,0.04);', '--light-bg:      #F5F5F5;')

with open(style_path, 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Fix contato.html (revert the dark card)
contato_path = os.path.join(out_folder, 'contato.html')
if os.path.exists(contato_path):
    with open(contato_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = html.replace('background: #424449;', 'background: var(--white);')
    html = html.replace('color: #ffffff;', 'color: var(--dark-text);')

    with open(contato_path, 'w', encoding='utf-8') as f:
        f.write(html)

print("Light theme applied successfully!")
