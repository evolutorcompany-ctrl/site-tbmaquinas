import json, os, re

log_file = r'C:\Users\Eduarda\.gemini\antigravity-ide\brain\15aeaaf5-8d7c-4601-8996-3eb62895f64b\.system_generated\logs\transcript.jsonl'
out_folder = 'C:/Users/Eduarda/Desktop/projeto Tb Máquinas/tb-maquinas-site'

target_files = ['index.html', 'produtos.html', 'sobre.html', 'servicos.html', 'feiras.html', 'contato.html']
contents = {f: '' for f in target_files}

# Parse transcript to get the latest CodeContent for each file
with open(log_file, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            entry = json.loads(line)
            if 'tool_calls' in entry:
                for tc in entry['tool_calls']:
                    # sometimes it is in arguments, sometimes inside args
                    if 'write_to_file' in str(tc):
                        args = tc.get('arguments')
                        if not args and 'args' in tc:
                            args = tc['args']
                        if type(args) == str:
                            try:
                                args = json.loads(args)
                            except:
                                pass
                        if type(args) == dict:
                            tgt = args.get('TargetFile', '')
                            code = args.get('CodeContent', '')
                            fname = os.path.basename(tgt)
                            if fname in target_files and code:
                                contents[fname] = code
        except Exception as e:
            pass

logo_new = '''<a href="index.html" class="logo" id="logo-header">
          <img src="images/produtos/favicon.png" alt="TB Máquinas" class="site-logo-icon" style="height: 40px; width: auto;">
          <span class="logo-text" style="font-family: var(--font-heading); font-size: 15px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; color: var(--primary);">Máquinas e Equipamentos</span>
        </a>'''

footer_social_new = '''<div class="footer-social">
            <a href="https://www.instagram.com/tbmaquinas_equipamentos/" target="_blank" rel="noopener" aria-label="Instagram"><i class="fab fa-instagram"></i></a>
            <a href="https://www.youtube.com/@TBMAQUINAS" target="_blank" rel="noopener" aria-label="YouTube"><i class="fab fa-youtube"></i></a>
            <a href="https://wa.me/5554992425851" target="_blank" rel="noopener" aria-label="WhatsApp"><i class="fab fa-whatsapp"></i></a>
            <a href="mailto:tbmaquinas@tbmaquinas.com" aria-label="E-mail"><i class="fas fa-envelope"></i></a>
          </div>'''

new_footer_contact = '''<div class="footer-contact-list">
            <div class="footer-contact-item"><i class="fas fa-map-marker-alt"></i><span>Rua Augusto Caprara, 382<br>Bairro Licorsul | CEP 95705-793</span></div>
            <div class="footer-contact-item"><i class="fas fa-phone"></i><a href="tel:+555436981050">+55 54 3698-1050</a></div>
            <div class="footer-contact-item"><i class="fab fa-whatsapp"></i><a href="https://wa.me/5554992425851" target="_blank" rel="noopener">+55 54 99242-5851</a></div>
            <div class="footer-contact-item" style="align-items:flex-start;"><i class="fas fa-envelope"></i><div style="display:flex;flex-direction:column;"><a href="mailto:tbmaquinas@tbmaquinas.com">tbmaquinas@tbmaquinas.com</a><a href="mailto:cassiano.comercial@tbmaquinas.com">cassiano.comercial@tbmaquinas.com</a></div></div>
            <div class="footer-contact-item"><i class="fas fa-clock"></i><span>07:30–11:30 | 13:30–17:00</span></div>
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

for fname, text in contents.items():
    if not text:
        print('Warning: could not find content for', fname)
        continue
        
    # Apply modifications cleanly
    
    # 1. Logo
    text = re.sub(r'<a href="index\.html" class="logo".*?</a>', logo_new, text, flags=re.DOTALL)
    
    # 2. Footer Social
    text = re.sub(r'<div class="footer-social">.*?</div>', footer_social_new, text, flags=re.DOTALL)
    
    # 3. Footer Contact
    text = re.sub(r'<div class="footer-contact-list">.*?</div>\s*</div>', new_footer_contact + '\n        </div>', text, flags=re.DOTALL)
    
    # 4. Global replacements
    text = text.replace('(54) 3698-1050', '+55 54 3698-1050')
    text = text.replace('(54) 99242-5851', '+55 54 99242-5851')
    
    # 5. Generic greens in inline HTML to accent
    text = text.replace('background:#25D366;', 'background:var(--accent);')
    
    # 6. Contact specific
    if fname == 'contato.html':
        text = re.sub(r'<div class="contact-info-list">.*?</div>\s*<div style="margin-top:36px', contact_info_new + '\n            <div style="margin-top:36px', text, flags=re.DOTALL)
        
        map_html = '''<div style="margin-top: 60px; width: 100%; height: 400px; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.1);">
              <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3477.587391942475!2d-51.5230953!3d-29.1764264!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x951c3c9b9b8b9b9b%3A0x9b9b9b9b9b9b9b9b!2sR.%20Augusto%20Caprara%2C%20382%20-%20Licorsul%2C%20Bento%20Gon%C3%A7alves%20-%20RS%2C%2095705-793!5e0!3m2!1spt-BR!2sbr!4v1700000000000!5m2!1spt-BR!2sbr" width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
            </div><!-- MAPA -->'''
        text = text.replace('</section>', map_html + '\n    </section>', 1)
        
    with open(os.path.join(out_folder, fname), 'w', encoding='utf-8') as f:
        f.write(text)
    print('Recovered and updated', fname)
