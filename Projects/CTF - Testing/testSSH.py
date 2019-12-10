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

def run():
    ssh_client =paramiko.SSHClient()
    # ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    r_ip = "192.168.0.100"
    r_username = "pi"
    r_password = "robots1234"
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=r_ip, username=r_username,password=r_password)
    print("First Line")
    stdin,stdout,stderr=ssh_client.exec_command("cd Python_Scripts/CTF\ -\ Testing/")
    for line in stdout:
        print('... ' + line.strip('\n'))
    print("Second Line")
    stdin,stdout,stderr=ssh_client.exec_command("sudo python main.py")
    for line in stderr:
        print('... ' + line.strip('\n'))
    # ssh_client.close()