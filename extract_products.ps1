$files = Get-ChildItem -Path "C:\Users\Eduarda\Desktop\projeto Tb Máquinas\TB maq" -Filter "*.html"
foreach ($f in $files) {
  $content = Get-Content $f.FullName -Raw -Encoding UTF8
  if ($content -match '<h1 class="product_title entry-title">(.*?)</h1>') {
    $title = $matches[1]
    Write-Host "Title: $title"
    if ($content -match '(?s)<div class="woocommerce-product-details__short-description">(.*?)</div>') {
      $desc = $matches[1] -replace '<.*?>', ' ' -replace '\s+', ' '
      Write-Host "Desc: $desc"
    }
    Write-Host "----------------"
  }
}
