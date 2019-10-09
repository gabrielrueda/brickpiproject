import script
import time
import brickpi3

BP = brickpi3.BrickPi3()

script.config()
try:
    while(True):
        script.moveForward()
        print(script.sensorValue())
        time.sleep(0.02) 

except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
    BP.reset_all()