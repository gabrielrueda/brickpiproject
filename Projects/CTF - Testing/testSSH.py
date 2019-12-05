from pexpect import pxssh
import getpass

def run():
    try:
        s = pxssh.pxssh()                                                   
        hostname = "192.168.0.100"
        username = "pi"
        password = getpass.getpass('password: ')
        s.login (hostname, username, password)
        s.sendline ('uptime')   # run a command
        s.prompt()             # match the prompt
        print(s.before)          # print everything before the prompt.
        s.sendline ('cd Python_Scripts/CTF\ -\ Testing/')
        s.prompt()
        print(s.before)
        s.sendline('sudo python main.py')
        #s.prompt()
        #print(s.before)
    except pxssh.ExceptionPxssh:
        print("pxssh failed on login.")