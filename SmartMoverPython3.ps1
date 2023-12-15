# Name:    SmartMoverCloudAPI
# Purpose: Execute the SmartMoverCloudAPI program

######################### Parameters ##########################
param(
    $pafid = '',
    $company = '',
    $fullname = '',
    $addressline1 = '',
    $city = '',
    $state = '',
    $postalcode = '',
    $country = '',
    $license = '', 
    [switch]$quiet = $false
    )

########################## Main ############################
Write-Host "`n===================== Melissa Smart Mover Cloud API ========================`n"

# Get license (either from parameters or user input)
if ([string]::IsNullOrEmpty($license) ) {
  $license = Read-Host "Please enter your license string"
}

# Check for License from Environment Variables 
if ([string]::IsNullOrEmpty($license) ) {
  $license = $env:MD_LICENSE
}

if ([string]::IsNullOrEmpty($license)) {
  Write-Host "`nLicense String is invalid!"
  Exit
}

# Run project
if ([string]::IsNullOrEmpty($pafid) -and [string]::IsNullOrEmpty($company) -and [string]::IsNullOrEmpty($fullname) -and [string]::IsNullOrEmpty($addressline1) -and [string]::IsNullOrEmpty($city) -and [string]::IsNullOrEmpty($state) -and [string]::IsNullOrEmpty($postal) -and [string]::IsNullOrEmpty($country)) {
  python3 SmartMoverPython3.py --license $license 
}
else {
  python3 SmartMoverPython3.py --license $license --pafid $pafid --company $company --fullname $fullname --addressline1 $addressline1 --city $city --state $state --postalcode $postalcode --country $country
}
