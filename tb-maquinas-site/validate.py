import os

base = r'C:\Users\Eduarda\Desktop\projeto Tb Máquinas\tb-maquinas-site'

print(f"{'File':<45} {'NewLogo':<10} {'FloatWA':<10} {'ScrollTop':<12} {'NoOldLogo':<12} {'FooterOK'}")
print("-" * 110)
for fname in sorted(f for f in os.listdir(base) if f.endswith('.html')):
    path = os.path.join(base, fname)
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    has_new_logo      = 'cropped-logomarca.png' in html
    has_float_wa      = 'float-whatsapp' in html
    has_scroll        = 'scroll-top' in html
    no_old_logo       = 'logo_topo_menor' not in html and 'Langerwisch' not in html
    has_footer_widget = 'footer-widget' in html
    print(f"{fname:<45} {str(has_new_logo):<10} {str(has_float_wa):<10} {str(has_scroll):<12} {str(no_old_logo):<12} {str(has_footer_widget)}")
