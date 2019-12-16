import os
import sys
from multiprocessing import Process

def Robot():
    os.system("./Robot.py")     
def connectSSH():
    os.system("./connectSSH.py") 

if __name__ == '__main__':
    a = Process(target=Robot)
    b = Process(target=connectSSH)
    a.start()
    b.start()
    a.join()
    b.join()