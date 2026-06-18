$template = Get-Content -Path "C:\Users\Eduarda\Desktop\projeto Tb Máquinas\tb-maquinas-site\product-template.html" -Raw -Encoding UTF8

function BuildPage($file, $title, $image, $desc, $features) {
    $urlTitle = [uri]::EscapeDataString($title)
    $featHtml = ($features | ForEach-Object { "<li><i class=`"fas fa-check-circle`"></i> $_</li>" }) -join "
              "
    
    $html = $template.Replace("__TITLE__", $title).Replace("__IMAGE__", $image).Replace("__DESC__", $desc).Replace("__FEATURES__", $featHtml).Replace("__TITLE_URL__", $urlTitle)
    
    Set-Content -Path "C:\Users\Eduarda\Desktop\projeto Tb Máquinas\tb-maquinas-site\$file" -Value $html -Encoding UTF8
}

BuildPage "envolvedora-tb-evp-pre.html" "Envolvedora de Pallets TB EVP-PRÉ" "images/maq1.jpg" "Equipamento com ótima produtividade. Produtividade acima de 30 pallets por hora." @(
    "Até 2.500Kg.",
    "Diâmetro do disco, 1500/1800mm.",
    "Altura da torre, 2400/3000mm.",
    "Controle de Estiramento filme strecth.",
    "Pré-estiro monitorizado.",
    "Rampa de acesso.",
    "Alimentação 220v/60Hz. Consumo 1,2w/h.",
    "Ajuste de altura de carga de sensor."
)

BuildPage "mesa-acumulo-tb-ms.html" "Mesa de Acúmulo Monitorizada TB MS" "images/maq5.jpg" "Utilizado para o acumulo e transporte de vasilhames durante produção." @(
    "Mesa de Acúmulo para vários modelos de frascos.",
    "Módulo independente de controle.",
    "Máquina com controle de rotação independente.",
    "Painel de comando.",
    "Diâmetro de disco de 1000mm a 1200mm.",
    "Sistema de regulagem de entrada do frasco."
)

BuildPage "rotuladora-tb-raa-cabine.html" "Rotuladora automática auto adesiva TB-RAA com cabine" "images/maq2-1.jpg" "Equipamento com ótima produtividade. Utilizado para rotulagem automática com rótulo, contra-rótulo, rótulo envolvente, gargatilha e selo adesivo." @(
    "Sistema de ajuste programação via remoto.",
    "Controle programável de distância entre rótulos.",
    "Produtividade de 1.000 a 12.000 frascos por hora.",
    "Cabeçotes com regulagem de altura para diversos tamanhos de frascos.",
    "Sensor para rótulo transparente.",
    "01 a 04 cabeçotes de aplicação.",
    "CLP-TB contador de produção.",
    "Diâmetro externo bobina 300 mm, diâmetro interno bobina 76 mm.",
    "Máquina equipada com IHM ou display visor de controle.",
    "Para frascos cilindros, quadrados, retangulares e cônicos.",
    "Cabine de enclausuramento NR12.",
    "Baixo custo de manutenção.",
    "Permite integração com as tecnologias de codificação (Hotstamp, Inkjet, Laser e termotransferência)."
)

BuildPage "rotuladora-tb-raa.html" "Rotuladora automática auto adesiva TB-RAA" "images/maq2-1.jpg" "Equipamento com ótima produtividade. Utilizado para rotulagem automática com rótulo, contra-rótulo, rótulo envolvente, gargatilha e selo adesivo." @(
    "Sistema de ajuste programação via remoto.",
    "Controle programável de distância entre rótulos.",
    "Produtividade de 1.000 a 12.000 frascos por hora.",
    "Cabeçotes com regulagem de altura para diversos tamanhos de frascos.",
    "Sensor para rótulo transparente.",
    "01 a 04 cabeçotes de aplicação.",
    "CLP-TB contador de produção.",
    "Diâmetro externo bobina 300 mm, diâmetro interno bobina 76 mm.",
    "Máquina equipada com IHM ou display visor de controle.",
    "Para frascos cilindros, quadrados, retangulares e cônicos.",
    "Cabine de enclausuramento NR12.",
    "Baixo custo de manutenção.",
    "Permite integração com as tecnologias de codificação (Hotstamp, Inkjet, Laser e termotransferência)."
)

BuildPage "rotuladora-master-label-bopp.html" "Rotuladora automática MASTER LABEL TB - BOPP" "images/maq2-1.jpg" "Equipamento com ótima produtividade. Utilizado para rotulagem automática com rótulo, contra-rótulo, rótulo envolvente, gargatilha e selo adesivo." @(
    "CLP com IHM Touch Screen.",
    "Acompanha sistema de set up rápido.",
    "Sistema de aplicação hot melt.",
    "Sistema de segurança atendendo norma NR12.",
    "Sistema caracol de entrada.",
    "Diâmetro externo bobina - 600mm.",
    "Diâmetro interno bobina - 150mm.",
    "Pista de leitura de 3 a 5 mm.",
    "Fotocélula - 5 mm.",
    "220V / 380V trifásico.",
    "Acesso remoto.",
    "Fabricação 100% nacional."
)

BuildPage "rotuladora-tb-rsa-1000.html" "Rotuladora semi-automática TB-RSA 1000" "images/maq2-1.jpg" "Equipamento com ótima produtividade. Utilizado para rotulagem semi-automática com rótulo, contra-rótulo e rótulo envolvente." @(
    "Aplicação - rótulo, contra-rótulo e rótulo envolvente.",
    "Sistema de ajuste programação via remoto.",
    "Datador hot stamp 3 linhas. (orçar separadamente).",
    "Sensor para rótulo transparente.(orçar separadamente).",
    "Produtividade de 1.000 frascos por hora.",
    "Sistema de pedestal com rodizio.(orçar separadamente).",
    "Para frascos cilindros.",
    "220v monofásico.",
    "Controle ajustável de distância entre rótulo e contra rótulo.",
    "CLP-TB contador de produção."
)
