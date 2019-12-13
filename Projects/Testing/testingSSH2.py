import paramiko
import time

def endConnection():
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    r_ip = "192.168.0.100"
    r_username = "pi"
    r_password = "robots1234"
    print("Killing Python Script...")
    ssh.connect(hostname=r_ip, username=r_username,password=r_password)
    try:
        ssh.exec_command('python emergencykill.py', get_pty=False)
    except:
        print("Could not kill")
    ssh.close()