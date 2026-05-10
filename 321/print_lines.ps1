$i=1
Get-Content 'c:\Users\11\321\index.html' | Select-Object -First 40 | ForEach-Object {
    Write-Output "$i $_"
    $i++
}
