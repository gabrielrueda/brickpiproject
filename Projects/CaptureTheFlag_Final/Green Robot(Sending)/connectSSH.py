#!/usr/bin/env python
import paramiko
import brickpi3

BP = brickpi3.BrickPi3()

ssh_client =paramiko.SSHClient()

def run():
    r_ip = "192.168.0.100"
    r_username = "pi"
    r_password = "robots1234"
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print("Trying to Connect...")
    ssh_client.connect(hostname=r_ip, username=r_username,password=r_password)
    sftp = ssh_client.open_sftp()
    sftp.chdir('Python_Scripts/CaptureTheFlag_Final')
    print("First Line")
    stdin,stdout,stderr=ssh_client.exec_command("python Robot.py") 
    for line in stderr:
        print('... ' + line.strip('\n'))


print("Starting Search....")
run()