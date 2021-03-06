import os
import sys
from multiprocessing import Process
import brickpi3

BP = brickpi3.BrickPi3()

def RobotScript():
    os.system("./Robot.py")     
def SSHScript():
    os.system("./connectSSH.py") 
    
try:
    a = Process(target=RobotScript)
    b = Process(target=SSHScript)
    a.start()
    b.start()
    a.join()
    b.join()
except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
    pass
    # BP.reset_all()