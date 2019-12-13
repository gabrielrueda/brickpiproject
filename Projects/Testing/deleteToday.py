# import paramiko
# import time

# def execute(channel, command):
#     command = 'echo $$; exec ' + command
#     (stdin, stdout, stderr) = channel.exec_command(command)
#     pid = int(stdout.readline())
#     return pid, stdin, stdout, stderr
    
# if __name__ == "__main__":
    
#     ssh = paramiko.SSHClient()
# #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# #     ssh.connect("192.168.0.100", username="pi", password="robots1234")
# #     transport = ssh.get_transport()
# #     channel = transport.open_session()
# #     while True:
# #         try:
# #             pid, _, _, _ = execute(channel, "sudo python movemotor.py")
# #         except KeyboardInterrupt:
# #             ssh.exec_command("kill %d" % pid)
# #             channel.close()
# #             break

# # import paramiko
# # import time

# # ssh_client =paramiko.SSHClient()
# # def run():
# #     # ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# #     r_ip = "192.168.0.100"
# #     r_username = "pi"
# #     r_password = "robots1234"
# #     ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# #     print("Trying to Connect...")
# #     ssh_client.connect(hostname=r_ip, username=r_username,password=r_password)
# #     # print("First Line")
# #     # stdin,stdout,stderr=ssh_client.exec_command("cd Python_Scripts/CTF_Testing")
# #     # for line in stdout:
# #     #     print('... ' + line.strip('\n'))
# #     print("Second Line")
# #     stdin,stdout,stderr=ssh_client.exec_command("sudo python movemotor.py", get_pty=True)
# #     time.sleep(2)
# #     ssh_client.close()

# # print("Starting search...")
# # run()
# import paramiko
# import select

# import time
# ltime = time.time()

# # Or use random:
# # import random
# # ltime = random.randint(0, 500)

# uname = "pi"
# client = paramiko.SSHClient()
# client.load_system_host_keys()
# client.connect('192.168.0.100', username=uname, password='robots1234')
# transport = client.get_transport()
# channel = transport.open_session()

# channel.exec_command("python movemotor.py")
# while True:
#     try:
#         rl, wl, xl = select.select([channel],[],[],0.0)
#         if len(rl) > 0:
#             # Must be stdout
#             print(channel.recv(1024))
#     except KeyboardInterrupt:
#         print("Caught control-C")
#         channel.close()
#         try:
#             # open new socket and kill the proc..
#             client.get_transport().open_session().exec_command("kill -9 `ps -fu %s | python movemotor.py' | grep -v grep | awk '{print $2}'`" % (uname, ltime))
#         except:
#             pass
    
#         client.close()
#         exit(0)


