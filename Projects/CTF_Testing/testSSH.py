#!/usr/bin/env python
import paramiko
import brickpi3

BP = brickpi3.BrickPi3()

ssh_client =paramiko.SSHClient()
def run():
    # ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    r_ip = "192.168.0.100"
    r_username = "pi"
    r_password = "robots1234"
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print("Trying to Connect...")
    ssh_client.connect(hostname=r_ip, username=r_username,password=r_password)
    print("First Line")
    stdin,stdout,stderr=ssh_client.exec_command("cd Python_Scripts/CTF_Testing")
    for line in stdout:
        print('... ' + line.strip('\n'))
    print("Second Line")
    stdin,stdout,stderr=ssh_client.exec_command("sudo python main.py")
    for line in stderr:
        print('... ' + line.strip('\n'))
    # ssh_client.close()

def stop():
    ssh_client.close()

try:
    print("Starting Search....")
    run()

except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
    stop()
    BP.reset_all()