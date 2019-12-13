import paramiko
import time
import testingSSH2

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
r_ip = "192.168.0.100"
r_username = "pi"
r_password = "robots1234"
print("Trying to Connect...")
ssh.connect(hostname=r_ip, username=r_username,password=r_password)
ssh.exec_command('python test.py', get_pty=False)
time.sleep(5)  # could do something with in/out/err
ssh.close()
testingSSH2.endConnection()
