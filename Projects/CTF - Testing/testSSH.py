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

import paramiko
ssh_client =paramiko.SSHClient()
# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
r_ip = "192.168.0.168"
r_username = "pi"
r_password = "robots1234"
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=r_ip, username=r_username,password=r_password)
# stdin,stdout,stderr=ssh_client.exec_command("ls")
# print(stdout)
# ssh_client.close()