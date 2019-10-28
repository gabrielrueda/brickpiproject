import brickpi3
import time

speed = 30
irvalue = 100
BP = brickpi3.BrickPi3() # Must have this - creates instance of brickpi

try:

    while irvalue > 20:

        BP.set_motor_power(BP.PORT_A, speed * 0.9)
        BP.set_motor_power(BP.PORT_D, speed)
        time.sleep(0.02) 

    # Stops motors
    BP.set_motor_power(BP.PORT_A, 0)
    BP.set_motor_power(BP.PORT_D, 0)

except KeyboardInterrupt: # the program gets interrupted by Ctrl+C on the keyboard.
    BP.reset_all() 