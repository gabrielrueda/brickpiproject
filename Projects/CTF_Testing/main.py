import os
from multiprocessing import Process

def Robot():
    os.system("./Robot.py")     
def testSSH():
    os.system("./testSSH.py") 

# os.chdir("/home/pi/Python_Scripts/CTF_Testing")
if __name__ == '__main__':
    a = Process(target=Robot)
    b = Process(target=testSSH)
    a.start()
    b.start()
    a.join()
    b.join()

#pushback