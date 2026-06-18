import os, glob, re

folder = 'C:/Users/Eduarda/Desktop/projeto Tb Máquinas/tb-maquinas-site'
html_files = glob.glob(os.path.join(folder, '*.html'))
css_file = os.path.join(folder, 'css', 'style.css')

# 1. Update CSS colors
with open(css_file, 'rb') as f:
    css = f.read().decode('utf-8')

css = css.replace('--light-bg:      #f5f5f5;', '--light-bg:      rgba(2,26,71,0.04);')
css = css.replace('--body-text:     #7f7f8a;', '--body-text:     rgba(2,26,71,0.75);')
css = css.replace('--dark-text:     #191919;', '--dark-text:     #021a47;')
css = css.replace('--border:        #e3e3e3;', '--border:        rgba(2,26,71,0.12);')
css = css.replace('--footer-bg:     #111827;', '--footer-bg:     #021a47;')
css = css.replace('background: #25D366;', 'background: var(--accent);')
css = css.replace('border-color: #25D366;', 'border-color: var(--accent);')
css = css.replace('background: #1ebe5d;', 'background: var(--accent-hover);')
css = css.replace('border-color: #1ebe5d;', 'border-color: var(--accent-hover);')
css = css.replace('rgba(37,211,102,0.5)', 'rgba(255,126,5,0.5)')
css = css.replace('rgba(37,211,102,0.7)', 'rgba(255,126,5,0.7)')
css = css.replace('rgba(37,211,102,0.4)', 'rgba(255,126,5,0.4)')
css = css.replace('rgba(37,211,102,0)', 'rgba(255,126,5,0)')

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css)

# Common corrupted strings mapping
replacements = {
    'MÃ¡quinas': 'Máquinas',
    'MÃ£': 'Mã',
    'Ã§': 'ç',
    'Ã©': 'é',
    'Ãª': 'ê',
    'Ã³': 'ó',
    'Ãµes': 'ões',
    'Ã§Ã£o': 'ção',
    'Ãº': 'ú',
    'Ã¢': 'â',
    'InovaÃ§Ã£o': 'Inovação',
    'Ã¡': 'á',
    'Ã­': 'í',
    'Ãµ': 'õ',
    'Ã\x81': 'Á',
    'Ã\x82': 'Â',
    'Ã\x83': 'Ã',
    'Ã\x89': 'É',
    'Ã\x8a': 'Ê',
    'Ã\x8d': 'Í',
    'Ã\x93': 'Ó',
    'Ã\x94': 'Ô',
    'Ã\x95': 'Õ',
    'Ã\x9a': 'Ú',
    'Ã\x87': 'Ç',
    'Mǭquinas': 'Máquinas',
    'Inovaǜo': 'Inovação',
    'acǧmulo': 'acúmulo',
    'nvel': 'nível',
    'oramento': 'orçamento',
    'Incio': 'Início',
    'Servios': 'Serviços',
    'ContÃ¡ct': 'Contato',
    'MÃ³dulo': 'Módulo',
    'ProduÃ§Ã£o': 'Produção',
    'SoluÃ§Ãµes': 'Soluções',
    'AutomaÃ§Ã£o': 'Automação',
    'InformaÃ§Ãµes': 'Informações',
    'ConfiguraÃ§Ãµes': 'Configurações'
}

logo_old = '''<a href="index.html" class="logo">
          <img src="images/produtos/logomarca.png" alt="TB Máquinas" class="site-logo-main" onerror="this.src='images/produtos/logomarca.png'">
        </a>'''
logo_new = '''<a href="index.html" class="logo" style="display:flex;align-items:center;gap:12px;text-decoration:none;">
          <img src="images/produtos/favicon.png" alt="TB Máquinas" style="height:40px;width:auto;object-fit:contain;">
          <span class="logo-text" style="font-family: var(--font-heading); font-size: 15px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; color: var(--primary);">Máquinas e Equipamentos</span>
        </a>'''

logo_old2 = '''<a href="index.html" class="logo" id="logo-header">
          <img src="images/produtos/logomarca.png" alt="TB Máquinas" class="site-logo-main" onerror="this.src='images/produtos/logomarca.png'">
        </a>'''
logo_new2 = '''<a href="index.html" class="logo" id="logo-header" style="display:flex;align-items:center;gap:12px;text-decoration:none;">
          <img src="images/produtos/favicon.png" alt="TB Máquinas" style="height:40px;width:auto;object-fit:contain;">
          <span class="logo-text" style="font-family: var(--font-heading); font-size: 15px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; color: var(--primary);">Máquinas e Equipamentos</span>
        </a>'''

footer_social_old = '''<div class="footer-social">
            <a href="https://wa.me/5554992425851" target="_blank" rel="noopener" aria-label="WhatsApp"><i class="fab fa-whatsapp"></i></a>
            <a href="mailto:tbmaquinas@tbmaquinas.com" aria-label="E-mail"><i class="fas fa-envelope"></i></a>
          </div>'''
footer_social_new = '''<div class="footer-social">
            <a href="https://www.instagram.com/tbmaquinas_equipamentos/" target="_blank" rel="noopener" aria-label="Instagram"><i class="fab fa-instagram"></i></a>
            <a href="https://www.youtube.com/@TBMAQUINAS" target="_blank" rel="noopener" aria-label="YouTube"><i class="fab fa-youtube"></i></a>
            <a href="https://wa.me/5554992425851" target="_blank" rel="noopener" aria-label="WhatsApp"><i class="fab fa-whatsapp"></i></a>
            <a href="mailto:tbmaquinas@tbmaquinas.com" aria-label="E-mail"><i class="fas fa-envelope"></i></a>
          </div>'''

contact_info_old = '''<div class="contact-info-list">
              <div class="contact-info-item">
                <div class="contact-info-icon"><i class="fas fa-phone"></i></div>
                <div class="contact-info-text">
                  <strong>Telefone</strong>
                  <a href="tel:+555436981050">(54) 3698-1050</a>
                </div>
              </div>
              <div class="contact-info-item">
                <div class="contact-info-icon" style="background:var(--accent);color:#fff;"><i class="fab fa-whatsapp"></i></div>
                <div class="contact-info-text">
                  <strong>WhatsApp</strong>
                  <a href="https://wa.me/5554992425851" target="_blank" rel="noopener">(54) 99242-5851</a>
                </div>
              </div>
              <div class="contact-info-item">
                <div class="contact-info-icon"><i class="fas fa-envelope"></i></div>
                <div class="contact-info-text">
                  <strong>E-mail</strong>
                  <a href="mailto:tbmaquinas@tbmaquinas.com">tbmaquinas@tbmaquinas.com</a>
                </div>
              </div>
              <div class="contact-info-item">
                <div class="contact-info-icon"><i class="fas fa-clock"></i></div>
                <div class="contact-info-text">
                  <strong>Atendimento</strong>
                  <span>07:30 às 11:30 | 13:30 às 17:00<br>de acordo com a necessidade do cliente</span>
                </div>
              </div>
            </div>'''

contact_info_new = '''<div class="contact-info-list">
              <div class="contact-info-item">
                <div class="contact-info-icon"><i class="fas fa-phone"></i></div>
                <div class="contact-info-text">
                  <strong>Telefone</strong>
                  <a href="tel:+555436981050">+55 54 3698-1050</a>
                </div>
              </div>
              <div class="contact-info-item">
                <div class="contact-info-icon" style="background:var(--accent);color:#fff;"><i class="fab fa-whatsapp"></i></div>
                <div class="contact-info-text">
                  <strong>WhatsApp</strong>
                  <a href="https://wa.me/5554992425851" target="_blank" rel="noopener">+55 54 99242-5851</a>
                </div>
              </div>
              <div class="contact-info-item">
                <div class="contact-info-icon"><i class="fas fa-envelope"></i></div>
                <div class="contact-info-text">
                  <strong>E-mail</strong>
                  <a href="mailto:tbmaquinas@tbmaquinas.com">tbmaquinas@tbmaquinas.com</a>
                  <a href="mailto:cassiano.comercial@tbmaquinas.com">cassiano.comercial@tbmaquinas.com</a>
                </div>
              </div>
              <div class="contact-info-item">
                <div class="contact-info-icon"><i class="fas fa-map-marker-alt"></i></div>
                <div class="contact-info-text">
                  <strong>Endereço</strong>
                  <span>Rua Augusto Caprara, 382<br>Bairro Licorsul | CEP 95705-793</span>
                </div>
              </div>
              <div class="contact-info-item">
                <div class="contact-info-icon" style="background:var(--accent);color:#fff;"><i class="fab fa-instagram"></i></div>
                <div class="contact-info-text">
                  <strong>Instagram</strong>
                  <a href="https://www.instagram.com/tbmaquinas_equipamentos/" target="_blank" rel="noopener">@tbmaquinas_equipamentos</a>
                </div>
              </div>
              <div class="contact-info-item">
                <div class="contact-info-icon" style="background:var(--accent);color:#fff;"><i class="fab fa-youtube"></i></div>
                <div class="contact-info-text">
                  <strong>YouTube</strong>
                  <a href="https://www.youtube.com/@TBMAQUINAS" target="_blank" rel="noopener">@TBMAQUINAS</a>
                </div>
              </div>
              <div class="contact-info-item">
                <div class="contact-info-icon"><i class="fas fa-clock"></i></div>
                <div class="contact-info-text">
                  <strong>Atendimento</strong>
                  <span>07:30 às 11:30 | 13:30 às 17:00<br>de acordo com a necessidade do cliente</span>
                </div>
              </div>
            </div>'''

for file in html_files:
    try:
        with open(file, 'rb') as f:
            data = f.read()
        
        # Determine current text
        if data.startswith(b'\xef\xbb\xbf'):
            text = data[3:].decode('utf-8', errors='ignore')
        else:
            try:
                # If it decodes fine without errors, maybe it was utf-8 but corrupted.
                text = data.decode('utf-8')
            except UnicodeDecodeError:
                # Fallback to windows-1252 if it was saved that way
                text = data.decode('windows-1252')
        
        # Try a safe un-corrupt if we find the exact MÃ¡quinas
        if 'MÃ¡quinas' in text:
            try:
                fixed_text = text.encode('windows-1252').decode('utf-8')
                text = fixed_text
            except:
                pass
        
        for k, v in replacements.items():
            text = text.replace(k, v)

        # Apply Global Phone, Email, Address
        text = text.replace('(54) 3698-1050', '+55 54 3698-1050')
        text = text.replace('(54) 99242-5851', '+55 54 99242-5851')
        text = text.replace('555436981050', '555436981050') # keep tel links
        
        # Global logo
        text = text.replace(logo_old, logo_new)
        text = text.replace(logo_old2, logo_new2)
        # Regex replace just in case my replace didn't match perfectly
        text = re.sub(r'<a href="index\.html" class="logo"( id="logo-header")?>\s*<img src="images/produtos/logomarca\.png".*?</a>', logo_new2, text, flags=re.DOTALL)
        
        # Global Footer Social
        text = text.replace(footer_social_old, footer_social_new)
        
        # Footer Contact List
        new_footer_contact = '''<div class="footer-contact-list">
            <div class="footer-contact-item"><i class="fas fa-map-marker-alt"></i><span>Rua Augusto Caprara, 382<br>Bairro Licorsul | CEP 95705-793</span></div>
            <div class="footer-contact-item"><i class="fas fa-phone"></i><a href="tel:+555436981050">+55 54 3698-1050</a></div>
            <div class="footer-contact-item"><i class="fab fa-whatsapp"></i><a href="https://wa.me/5554992425851" target="_blank" rel="noopener">+55 54 99242-5851</a></div>
            <div class="footer-contact-item" style="align-items:flex-start;"><i class="fas fa-envelope"></i><div style="display:flex;flex-direction:column;"><a href="mailto:tbmaquinas@tbmaquinas.com">tbmaquinas@tbmaquinas.com</a><a href="mailto:cassiano.comercial@tbmaquinas.com">cassiano.comercial@tbmaquinas.com</a></div></div>
            <div class="footer-contact-item"><i class="fas fa-clock"></i><span>07:30–11:30 | 13:30–17:00</span></div>
          </div>'''
        text = re.sub(r'<div class="footer-contact-list">.*?</div>\s*</div>', new_footer_contact + '\n        </div>', text, flags=re.DOTALL)
        
        # Contact Page specifics
        if 'contato.html' in file:
            text = text.replace(contact_info_old, contact_info_new)
            # Add map
            if '<!-- MAPA -->' not in text:
                map_html = '''<div style="margin-top: 60px; width: 100%; height: 400px; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.1);">
              <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3477.587391942475!2d-51.5230953!3d-29.1764264!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x951c3c9b9b8b9b9b%3A0x9b9b9b9b9b9b9b9b!2sR.%20Augusto%20Caprara%2C%20382%20-%20Licorsul%2C%20Bento%20Gon%C3%A7alves%20-%20RS%2C%2095705-793!5e0!3m2!1spt-BR!2sbr!4v1700000000000!5m2!1spt-BR!2sbr" width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
            </div><!-- MAPA -->'''
                text = text.replace('</section>', map_html + '\n    </section>', 1)

        # Fix green generic colors manually if any remain in html inline styles
        text = text.replace('background:#25D366;', 'background:var(--accent);')
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(text)
        print('Processed:', os.path.basename(file))
    except Exception as e:
        print('Error on', os.path.basename(file), ':', e)
