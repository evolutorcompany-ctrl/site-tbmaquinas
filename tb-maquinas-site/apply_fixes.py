import os
import re

out_folder = 'C:/Users/Eduarda/Desktop/projeto Tb Máquinas/tb-maquinas-site'

# 1. Update style.css to include mbf-canno font
style_path = os.path.join(out_folder, 'css', 'style.css')
with open(style_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

if '@font-face' not in css_content or 'mbf-canno' not in css_content:
    font_css = """
@font-face {
  font-family: 'mbf-canno';
  src: url('../fonts/mbf-canno.ttf') format('truetype');
  font-weight: normal;
  font-style: normal;
}
"""
    css_content = font_css + css_content
    with open(style_path, 'w', encoding='utf-8') as f:
        f.write(css_content)

print("Updated style.css")

# Helper to process html files
def process_html_files():
    for fname in os.listdir(out_folder):
        if not fname.endswith('.html'):
            continue
            
        path = os.path.join(out_folder, fname)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 2. Update WhatsApp links
        content = re.sub(
            r'"https://wa\.me/5554992425851"', 
            r'"https://wa.me/5554992425851?text=Ol%C3%A1!%20Gostaria%20de%20obter%20mais%20informa%C3%A7%C3%B5es%20sobre%20os%20produtos%20e%20servi%C3%A7os%20da%20TB%20M%C3%A1quinas."', 
            content
        )
        
        # 3. Update Footer Logo
        old_footer_brand = r'<div class="footer-brand">\s*<a href="index\.html" class="logo"[^>]*>\s*<img src="images/produtos/favicon\.png"[^>]*>\s*<span class="logo-text"[^>]*>Máquinas e Equipamentos</span>\s*</a>'
        new_footer_brand = '''<div class="footer-brand">
          <a href="index.html" class="logo" style="display:block;margin-bottom:24px;">
            <img src="images/logomarca.png" alt="TB Máquinas" style="max-height:80px;width:auto;object-fit:contain;">
          </a>'''
        content = re.sub(old_footer_brand, new_footer_brand, content, flags=re.DOTALL)
        
        # 4. Update Footer Copyright
        old_copyright = r'<p class="footer-copyright">&copy; 2026 <strong>TB Máquinas</strong>\. Todos os direitos reservados\.</p>'
        new_copyright = '''<p class="footer-copyright">&copy; 2026 <strong>TB Máquinas</strong>. Todos os direitos reservados. | Desenvolvido por <a href="https://evolutor.com.br/" target="_blank" rel="noopener" style="font-family:'mbf-canno', sans-serif; text-decoration:none; color:inherit;">Evolutor</a></p>'''
        content = re.sub(old_copyright, new_copyright, content)
        
        # 5. Fix Home Hero (only in index.html)
        if fname == 'index.html':
            old_hero = r'<section class="hero-slider" id="hero-slider">.*?</section>'
            new_hero = '''<section class="hero" id="hero">
      <img src="images/hero-bg.jpg" alt="TB Máquinas" class="hero-bg">
      <div class="hero-overlay"></div>
      <div class="container hero-content">
        <div class="hero-text fade-up">
          <span class="hero-label">Fabricação 100% Nacional</span>
          <h1>Inovação em<br><span>Máquinas para Embalagem</span></h1>
          <p class="hero-desc">Equipamentos de alta tecnologia que garantem produtividade, segurança e eficiência para sua indústria.</p>
          <div class="hero-actions">
            <a href="produtos.html" class="btn btn-primary btn-lg">Conheça os Produtos</a>
            <a href="contato.html#formulario" class="btn btn-outline-white btn-lg">Solicitar Orçamento</a>
          </div>
        </div>
      </div>
    </section>'''
            content = re.sub(old_hero, new_hero, content, flags=re.DOTALL)

        # 6. Fix Contato form (only in contato.html)
        if fname == 'contato.html':
            # "Nome Completo" -> "Nome"
            content = content.replace('<label class="form-label" for="nome">Nome Completo</label>', '<label class="form-label" for="nome">Nome</label>')
            
            # Make "empresa" required
            content = content.replace('<input type="text" id="empresa" name="empresa" class="form-control" placeholder="Nome da sua empresa">', '<input type="text" id="empresa" name="empresa" class="form-control" required placeholder="Nome da sua empresa">')
            
            # Make "interesse" required
            content = content.replace('<select id="interesse" name="interesse" class="form-control">', '<select id="interesse" name="interesse" class="form-control" required>')
            
            # Add pattern to email
            content = content.replace('<input type="email" id="email" name="email" class="form-control" required placeholder="seu@email.com">', '<input type="email" id="email" name="email" class="form-control" required pattern="[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}" placeholder="seu@email.com">')
            
            # Add JS validation script at the end of the body
            js_script = """
  <script>
    document.addEventListener("DOMContentLoaded", function() {
      const form = document.querySelector(".contact-form-card form");
      if(form) {
        form.addEventListener("submit", function(e) {
          e.preventDefault();
          
          const nome = document.getElementById("nome").value.trim();
          const empresa = document.getElementById("empresa").value.trim();
          const telefone = document.getElementById("telefone").value.trim();
          const email = document.getElementById("email").value.trim();
          const interesse = document.getElementById("interesse").value.trim();
          
          if(!nome || !empresa || !telefone || !interesse || !email) {
            alert("Por favor, preencha todos os campos obrigatórios (Nome, Empresa, Telefone, E-mail, Interesse).");
            return;
          }
          
          const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$/;
          if(!emailRegex.test(email)) {
            alert("Por favor, insira um e-mail válido com domínio correto (exemplo: contato@email.com).");
            return;
          }
          
          alert("Mensagem enviada com sucesso!");
          form.reset();
        });
      }
    });
  </script>
</body>"""
            if "const emailRegex" not in content:
                content = content.replace("</body>", js_script)

        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Processed {fname}")

process_html_files()
