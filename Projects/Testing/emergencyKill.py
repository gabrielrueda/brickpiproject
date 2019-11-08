import brickpi3
import time

# BP = brickpi3.BrickPi3() # Must have this - creates instance of brickpi
BP = brickpi3.BrickPi3()

try:
    while (True):
        print("PRESS CONTROL + C TO KILL")
except KeyboardInterrupt: # the program gets interrupted by Ctrl+C on the keyboard.
    BP.reset_all() 