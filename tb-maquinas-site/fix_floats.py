import os, re

base = r'C:\Users\Eduarda\Desktop\projeto Tb Máquinas\tb-maquinas-site'

# The float-whatsapp, scroll-top button and main.js script
# need to be inserted just before </body> in every main HTML file

FLOATING_BLOCK = """
  <a href="https://wa.me/5554992425851?text=Ol%C3%A1!%20Gostaria%20de%20obter%20mais%20informa%C3%A7%C3%B5es%20sobre%20os%20produtos%20e%20servi%C3%A7os%20da%20TB%20M%C3%A1quinas." class="float-whatsapp" target="_blank" rel="noopener" aria-label="WhatsApp">
    <i class="fab fa-whatsapp"></i><span class="wa-tooltip">Fale conosco</span>
  </a>
  <button id="scroll-top" aria-label="Voltar ao topo"><i class="fas fa-chevron-up"></i></button>
  <script src="js/main.js"></script>
"""

skip_files = {'product-template.html', 'politica-privacidade.html'}

changed = []
for fname in sorted(f for f in os.listdir(base) if f.endswith('.html')):
    if fname in skip_files:
        continue
    path = os.path.join(base, fname)
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    original = html

    # Remove any existing float-whatsapp / scroll-top / main.js at end (before </body>)
    html = re.sub(
        r'\s*<a [^>]*class="float-whatsapp"[^>]*>.*?</a>\s*\n',
        '\n',
        html, flags=re.DOTALL
    )
    html = re.sub(
        r'\s*<button id="scroll-top"[^>]*>.*?</button>\s*\n',
        '\n',
        html, flags=re.DOTALL
    )
    html = re.sub(
        r'\s*<script src="js/main\.js"></script>\s*\n',
        '\n',
        html, flags=re.DOTALL
    )

    # Insert before </body>
    html = html.replace('</body>', FLOATING_BLOCK + '</body>')

    if html != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        changed.append(fname)

print(f"Fixed {len(changed)} files:")
for f in changed:
    print(f"  + {f}")

# Also fix politica-privacidade.html footer logo
ppath = os.path.join(base, 'politica-privacidade.html')
if os.path.exists(ppath):
    with open(ppath, 'r', encoding='utf-8') as f:
        html = f.read()
    html = re.sub(
        r'(images/produtos/logo_topo_menor\.png|images/logomarca\.png)',
        'images/produtos/cropped-logomarca.png',
        html
    )
    with open(ppath, 'w', encoding='utf-8') as f:
        f.write(html)
    print("  + politica-privacidade.html (logo fix)")

print("Done!")
