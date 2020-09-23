$name = Read-Host -Prompt 'Give the rule a name: '
$direction = Read-Host -Prompt 'Inbound or Outbound: '
$port = Read-Host -Prompt 'Enter a Port you want to open: '
$option = Read-Host -Prompt 'Allow or Block: '

New-NetFirewallRule -DisplayName $name -Direction $direction -LocalPort $port -Protocol TCP -Action $option