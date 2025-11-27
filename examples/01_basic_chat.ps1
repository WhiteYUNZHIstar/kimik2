# 示例：01_basic_chat.ps1
$env:KIMI_API_KEY = Read-Host "请输入你的 KIMI API Key"
python -c "import kimik2 as kk; print(kk.Client().chat('1+1=?, 请直接给数字'))"
