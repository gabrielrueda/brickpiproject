import time
import brickpi3

speed = 5
BP = brickpi3.BrickPi3() # Must have this - creates instance of brickpi

try:
        BP.set_motor_power(BP.PORT_A, -speed)
        time.sleep(4)
        BP.set_motor_power(BP.PORT_A, 0)
        time.sleep(3)
        BP.set_motor_power(BP.PORT_A, -speed)
        time.sleep(2)

except KeyboardInterrupt: # the program gets interrupted by Ctrl+C on the keyboard.
    BP.reset_all() 