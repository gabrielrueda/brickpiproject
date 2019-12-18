import os
import sys
from multiprocessing import Process
import connectSSH
import reconnectSSH
import brickpi3

BP = brickpi3.BrickPi3()

def RobotScript():
    os.system("./Robot.py")     
def SSHScript():
    os.system("./connectSSH.py") 

# if __name__ == '__main__':
#     a = Process(target=Robot)
#     b = Process(target=connectSSH)
#     a.start()
#     b.start()
#     a.join()
#     b.join()

try:
    a = Process(target=RobotScript)
    b = Process(target=SSHScript)
    a.start()
    b.start()
    a.join()
    b.join()
except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
    connectSSH.close()
    print("disconnected")
    reconnectSSH.powerOff()
    BP.reset_all()