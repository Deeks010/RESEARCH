$ErrorActionPreference = 'Stop'
$researchRoot = $PSScriptRoot
$prospectFiles = @('prospects_chennai_rubber.json', 'prospects_chennai_other.json', 'prospects_tn.json', 'prospects_south.json')
$mailDomains = @()
foreach ($prospectFile in $prospectFiles) {
    $entries = Get-Content -LiteralPath (Join-Path $researchRoot $prospectFile) -Raw -Encoding UTF8 | ConvertFrom-Json
    foreach ($entry in $entries) {
        if ($entry.email -match '@([^\s@]+)$') { $mailDomains += $Matches[1].ToLowerInvariant() }
    }
}
$mailDomains = $mailDomains | Sort-Object -Unique
$results = @()
foreach ($mailDomain in $mailDomains) {
    try {
        $records = @(Resolve-DnsName -Name $mailDomain -Type MX -DnsOnly -QuickTimeout -ErrorAction Stop | Where-Object { $_.Type -eq 'MX' })
        if ($records.Count -gt 0) {
            $hosts = @($records | ForEach-Object { $_.NameExchange })
            $status = if ($hosts -contains '.') { 'Null MX: domain declares no mail service' } else { 'MX mail-routing records found' }
            $results += [PSCustomObject]@{domain=$mailDomain;status=$status;mail_hosts=$hosts;checked_date='2026-09-15'}
        } else {
            $results += [PSCustomObject]@{domain=$mailDomain;status='No MX returned; confirm by phone before email';mail_hosts=@();checked_date='2026-09-15'}
        }
    } catch {
        $results += [PSCustomObject]@{domain=$mailDomain;status='DNS lookup failed or no MX found; confirm by phone';mail_hosts=@();checked_date='2026-09-15';error=$_.Exception.Message}
    }
}
$json = ConvertTo-Json -InputObject @($results) -Depth 5
[System.IO.File]::WriteAllText((Join-Path $researchRoot 'prospect_mail_domains.json'), $json, [System.Text.UTF8Encoding]::new($false))
$results | Group-Object status | Select-Object Count,Name
