# Automating_file_transfer

A Python script that connects to an FTP server and downloads files from a specified directory. It also moves the downloaded files to a destination on the internal network. The script runs on a schedule and logs its progress in a log file.  
  
**Requirements**
- Python   
- ftplib  
- os  
- logging  
- schedule  
- shutil  
  
**Usage**
1) Clone the repository  
2) Replace the FTP server, username, password, remote directory, local directory, and destination   with the desired values.  
3) Run the script using the command python3 ftp_downloader.py  
  
**Schedule**
The script is set to run every day at 10:30. The schedule can be modified in the script_schedule function.  
  
**Logging**
The script logs its progress in the download.log file. The log file includes information about the successful connection to the FTP server, file download progress, and the movement of files to the destination. In case of any errors, the error messages are logged in the file as well.  
  
**Note**
The script prompts the user to enter the FTP server, username, password, remote directory, local directory, and destination. The code can be modified to use fixed values instead of the user input.  
  