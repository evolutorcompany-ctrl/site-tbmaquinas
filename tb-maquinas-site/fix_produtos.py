import os

path = r'C:\Users\Eduarda\Desktop\projeto Tb Máquinas\tb-maquinas-site\produtos.html'

with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# REPLACEMENT 1: Envolvedoras block
old_envolvedora = """<div class="product-detail fade-up">
          <div class="product-detail-image">
            <img src="images/produtos/env1n.png" alt="Envolvedora de Pallets TB EVP-PRÉ">
          </div>
          <div class="product-detail-content">
            <span class="section-label">Envolvedora de Pallets</span>
            <h2>TB EVP-PRÉ</h2>
            <p>Equipamento com ótima produtividade. Produtividade acima de 30 pallets por hora.</p>
            <ul class="product-specs">
              <h4>Especificações</h4>
              <div class="specs-list">
                <div class="spec-item"><i class="fas fa-check-circle"></i> Até 2.500Kg</div>
                <div class="spec-item"><i class="fas fa-check-circle"></i> Diâmetro do disco 1500/1800mm</div>
                <div class="spec-item"><i class="fas fa-check-circle"></i> Altura da torre 2400/3000mm</div>
                <div class="spec-item"><i class="fas fa-check-circle"></i> Pré-estiro monitorizado</div>
                <div class="spec-item"><i class="fas fa-check-circle"></i> Controle de estiramento stretch</div>
                <div class="spec-item"><i class="fas fa-check-circle"></i> Rampa de acesso</div>
                <div class="spec-item"><i class="fas fa-check-circle"></i> Alimentação 220v/60Hz</div>
                <div class="spec-item"><i class="fas fa-check-circle"></i> Ajuste de altura de carga por sensor</div>
              </div>
            </ul>
            <div class="product-cta-row">
              <a href="envolvedora-tb-evp-pre.html" class="btn btn-primary"><i class="fas fa-eye"></i> Ver Detalhes</a>
              <a href="contato.html#formulario" class="btn btn-outline">Solicitar Orçamento</a>
            </div>
          </div>
        </div>"""

new_envolvedora = """<div class="products-grid">
          <div class="product-card fade-up">
            <div class="product-card-image">
              <img src="images/produtos/env1n.png" alt="Envolvedora de Pallets TB EVP-PRÉ" loading="lazy">
              <span class="product-card-badge">Envolvedora</span>
            </div>
            <div class="product-card-body">
              <span class="product-card-category">Envolvedora de Pallets</span>
              <h3>Envolvedora TB EVP-PRÉ</h3>
              <p>Equipamento com ótima produtividade, alcançando acima de 30 pallets por hora com capacidade para até 2.500Kg e pré-estiro monitorizado.</p>
              <a href="envolvedora-tb-evp-pre.html" class="btn btn-outline btn-sm">Ver Produto <i class="fas fa-arrow-right"></i></a>
            </div>
          </div>
        </div>"""

# REPLACEMENT 2: Mesas de Acúmulo block
old_mesas = """<div class="product-detail reverse fade-up">
          <div class="product-detail-image">
            <img src="images/produtos/mesa01.png" alt="Mesa de Acúmulo Monitorizada TB MS">
          </div>
          <div class="product-detail-content">
            <span class="section-label">Mesa de Acúmulo</span>
            <h2>Monitorizada TB MS</h2>
            <p>Utilizado para o acúmulo e transporte de vasilhames durante produção. Mesa de Acúmulo para vários modelos de frascos.</p>
            <ul class="product-specs">
              <h4>Especificações</h4>
              <div class="specs-list">
                <div class="spec-item"><i class="fas fa-check-circle"></i> Módulo independente de controle</div>
                <div class="spec-item"><i class="fas fa-check-circle"></i> Controle de rotação independente</div>
                <div class="spec-item"><i class="fas fa-check-circle"></i> Painel de comando</div>
                <div class="spec-item"><i class="fas fa-check-circle"></i> Diâmetro de disco 1000mm a 1200mm</div>
                <div class="spec-item"><i class="fas fa-check-circle"></i> Regulagem de entrada do frasco</div>
                <div class="spec-item"><i class="fas fa-check-circle"></i> Vários modelos de frascos</div>
              </div>
            </ul>
            <div class="product-cta-row">
              <a href="mesa-acumulo-tb-ms.html" class="btn btn-primary"><i class="fas fa-eye"></i> Ver Detalhes</a>
              <a href="contato.html#formulario" class="btn btn-outline">Solicitar Orçamento</a>
            </div>
          </div>
        </div>"""

new_mesas = """<div class="products-grid">
          <div class="product-card fade-up">
            <div class="product-card-image">
              <img src="images/produtos/mesa01.png" alt="Mesa de Acúmulo Monitorizada TB MS" loading="lazy">
              <span class="product-card-badge">Mesa</span>
            </div>
            <div class="product-card-body">
              <span class="product-card-category">Mesa de Acúmulo</span>
              <h3>Monitorizada TB MS</h3>
              <p>Solução ideal para o acúmulo e transporte de vasilhames. Módulo independente de controle de rotação e compatibilidade para vários modelos de frascos.</p>
              <a href="mesa-acumulo-tb-ms.html" class="btn btn-outline btn-sm">Ver Produto <i class="fas fa-arrow-right"></i></a>
            </div>
          </div>
        </div>"""

html = html.replace(old_envolvedora, new_envolvedora)
html = html.replace(old_mesas, new_mesas)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
print("produtos.html updated successfully.")
