from pexpect import pxssh
import getpass

def run():
    try:
        s = pxssh.pxssh()
        s.force_password = True                                                   
        hostname = "192.168.0.100"
        username = "pi"
        password = getpass.getpass('password: ')
        s.PROMPT= 'SSH> '
        s.login (hostname, username, password, auto_prompt_reset=False)
        s.sendline ('uptime')   # run a command
        s.prompt()             # match the prompt
        print(s.before)          # print everything before the prompt.
        s.sendline ('cd Python_Scripts/CTF\ -\ Testing/')
        s.prompt()
        print(s.before)
        s.sendline('sudo python main.py')
        s.prompt()
        print(s.before)
    except pxssh.ExceptionPxssh as error:
        print("pxssh failed on login.")
        print(error)