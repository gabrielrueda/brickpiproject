# from pexpect import pxssh
# import getpass
# def run():
#     try:
#         s = pxssh.pxssh()
#         hostname = "192.168.0.104"
#         username = "pi"
#         password = getpass.getpass('password: ')
#         s.PROMPT= 'SSH> '
#         s.login(hostname, username, password, port=22, auto_prompt_reset=False)
#         s.sendline('uptime')   # run a command
#         s.prompt()             # match the prompt
#         print(s.before)        # print everything before the prompt.
#         s.sendline('cd Python_Scripts/CTF\ -\ Testing/')
#         s.prompt()
#         print(s.before)
#         s.sendline('sudo python main.py')
#         s.prompt()
#         print(s.before)
#         s.logout()
#     except pxssh.ExceptionPxssh as error:
#         print("pxssh failed on login.")
#         print(error)

import base64
import paramiko
key = paramiko.RSAKey(data=base64.b64decode(b'AAA...'))
client = paramiko.SSHClient()
client.get_host_keys().add('ssh.example.com', 'ssh-rsa', key)
client.connect('ssh.example.com', username='strongbad', password='thecheat')
stdin, stdout, stderr = client.exec_command('ls')
for line in stdout:
    print('... ' + line.strip('\n'))
client.close()