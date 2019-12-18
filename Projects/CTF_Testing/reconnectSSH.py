import paramiko
import brickpi3

BP = brickpi3.BrickPi3()

ssh_client =paramiko.SSHClient()

def powerOff():
    # ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    r_ip = "192.168.0.100"
    r_username = "pi"
    r_password = "robots1234"
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print("Reconnecting...")
    ssh_client.connect(hostname=r_ip, username=r_username,password=r_password)
    print("Powering Down")
    stdin,stdout,stderr=ssh_client.exec_command("sudo poweroff")