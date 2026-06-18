$htmlFile = 'C:\Users\Eduarda\Desktop\projeto Tb Máquinas\TB maq\Sobre – Tb Máquinas.html'
$htmlContent = [System.IO.File]::ReadAllText($htmlFile, [System.Text.Encoding]::UTF8)
$textContent = $htmlContent -replace '<[^>]+>', ' ' -replace '\s+', ' '
[System.IO.File]::WriteAllText('C:\Users\Eduarda\Desktop\projeto Tb Máquinas\TB maq\sobre_extracted.txt', $textContent, [System.Text.Encoding]::UTF8)
Write-Host "Extração Sobre concluída"

$htmlFile2 = 'C:\Users\Eduarda\Desktop\projeto Tb Máquinas\TB maq\Mesa de Acúmulo Monitorizada TB MS – Tb Máquinas.html'
$htmlContent2 = [System.IO.File]::ReadAllText($htmlFile2, [System.Text.Encoding]::UTF8)
$textContent2 = $htmlContent2 -replace '<[^>]+>', ' ' -replace '\s+', ' '
[System.IO.File]::WriteAllText('C:\Users\Eduarda\Desktop\projeto Tb Máquinas\TB maq\mesa_extracted.txt', $textContent2, [System.Text.Encoding]::UTF8)
Write-Host "Extração Mesa concluída"

$htmlFile3 = 'C:\Users\Eduarda\Desktop\projeto Tb Máquinas\TB maq\Envolvedora de Pallets TB EVP-PRÉ – Tb Máquinas.html'
$htmlContent3 = [System.IO.File]::ReadAllText($htmlFile3, [System.Text.Encoding]::UTF8)
$textContent3 = $htmlContent3 -replace '<[^>]+>', ' ' -replace '\s+', ' '
[System.IO.File]::WriteAllText('C:\Users\Eduarda\Desktop\projeto Tb Máquinas\TB maq\envolvedora_extracted.txt', $textContent3, [System.Text.Encoding]::UTF8)
Write-Host "Extração Envolvedora concluída"

$htmlFile4 = 'C:\Users\Eduarda\Desktop\projeto Tb Máquinas\TB maq\Rotuladora automática MASTER LABEL TB – BOPP – Tb Máquinas.html'
$htmlContent4 = [System.IO.File]::ReadAllText($htmlFile4, [System.Text.Encoding]::UTF8)
$textContent4 = $htmlContent4 -replace '<[^>]+>', ' ' -replace '\s+', ' '
[System.IO.File]::WriteAllText('C:\Users\Eduarda\Desktop\projeto Tb Máquinas\TB maq\rot_bopp_extracted.txt', $textContent4, [System.Text.Encoding]::UTF8)
Write-Host "Extração BOPP concluída"

$htmlFile5 = 'C:\Users\Eduarda\Desktop\projeto Tb Máquinas\TB maq\Rotuladora automática auto adesiva TB-RAA com cabine – Tb Máquinas.html'
$htmlContent5 = [System.IO.File]::ReadAllText($htmlFile5, [System.Text.Encoding]::UTF8)
$textContent5 = $htmlContent5 -replace '<[^>]+>', ' ' -replace '\s+', ' '
[System.IO.File]::WriteAllText('C:\Users\Eduarda\Desktop\projeto Tb Máquinas\TB maq\rot_raa_cabine_extracted.txt', $textContent5, [System.Text.Encoding]::UTF8)
Write-Host "Extração RAA Cabine concluída"

$htmlFile6 = 'C:\Users\Eduarda\Desktop\projeto Tb Máquinas\TB maq\Rotuladora automática auto adesiva TB-RAA – Tb Máquinas.html'
$htmlContent6 = [System.IO.File]::ReadAllText($htmlFile6, [System.Text.Encoding]::UTF8)
$textContent6 = $htmlContent6 -replace '<[^>]+>', ' ' -replace '\s+', ' '
[System.IO.File]::WriteAllText('C:\Users\Eduarda\Desktop\projeto Tb Máquinas\TB maq\rot_raa_extracted.txt', $textContent6, [System.Text.Encoding]::UTF8)
Write-Host "Extração RAA concluída"

$htmlFile7 = 'C:\Users\Eduarda\Desktop\projeto Tb Máquinas\TB maq\Rotuladora semi-automática TB-RSA 1000 – Tb Máquinas.html'
$htmlContent7 = [System.IO.File]::ReadAllText($htmlFile7, [System.Text.Encoding]::UTF8)
$textContent7 = $htmlContent7 -replace '<[^>]+>', ' ' -replace '\s+', ' '
[System.IO.File]::WriteAllText('C:\Users\Eduarda\Desktop\projeto Tb Máquinas\TB maq\rot_rsa1000_extracted.txt', $textContent7, [System.Text.Encoding]::UTF8)
Write-Host "Extração RSA 1000 concluída"
