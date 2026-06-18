import os, re

base = r'C:\Users\Eduarda\Desktop\projeto Tb Máquinas\tb-maquinas-site'

skip = {'product-template.html', 'politica-privacidade.html'}
changed = []

for fname in sorted(f for f in os.listdir(base) if f.endswith('.html')):
    if fname in skip:
        continue
    path = os.path.join(base, fname)
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    original = html

    # --- HEADER logo-text: force white on dark header ---
    html = html.replace(
        "color: var(--dark-text);\">\r\nM\u00e1quinas",
        "color: #ffffff;\">\r\nM\u00e1quinas"
    )
    # Generic fix: logo-text inline style color
    html = re.sub(
        r'(class="logo-text"[^>]*style="[^"]*)color:\s*var\(--dark-text\)',
        r'\1color: #ffffff',
        html
    )
    html = re.sub(
        r'(class="logo-text"[^>]*style="[^"]*)color:\s*var\(--primary\)',
        r'\1color: #ffffff',
        html
    )

    # --- FOOTER: update footer logo area and footer desc/copyright colours ---
    # Footer logo - make sure it's the correct one (cropped-logomarca.png)
    html = re.sub(
        r'images/produtos/logo_topo_menor\.png',
        'images/produtos/cropped-logomarca.png',
        html
    )

    # Footer bottom copyright Evolutor link: was color:inherit (now dark, needs accent)
    html = re.sub(
        r"(Desenvolvido por.*?Evolutor.*?)color:inherit",
        r"\1color:var(--accent)",
        html,
        flags=re.DOTALL
    )

    # Remove whatsapp btn-whatsapp inline color override (redundant now)
    html = re.sub(
        r'(class="btn btn-whatsapp"[^>]*?) style="background:var\(--accent\);border-color:var\(--accent\);"',
        r'\1',
        html
    )

    if html != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        changed.append(fname)

print(f"Updated {len(changed)} files:")
for f in changed:
    print(f"  + {f}")
print("Done!")
