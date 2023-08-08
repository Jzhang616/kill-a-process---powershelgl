#Jason Zhang
#JASZHANG
#ID: 112920652

param(
    [Parameter(Mandatory=$true)]
    [string]$processName
)

$processes = Get-Process -Name $processName -ErrorAction SilentlyContinue

if ($processes.Count -eq 0) {
    Write-Host "No such process is running."
    exit
}

$processes | ForEach-Object { $_.Kill() }
Get-Process
