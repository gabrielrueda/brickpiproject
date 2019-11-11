import brickpi3
import time

speed = 40
BP = brickpi3.BrickPi3() # Must have this - creates instance of brickpi

try:
    while True:

        BP.set_motor_power(BP.PORT_A, -speed)
        BP.set_motor_power(BP.PORT_D, -speed)
        time.sleep(0.02) 

except KeyboardInterrupt: # the program gets interrupted by Ctrl+C on the keyboard.
    BP.reset_all() 