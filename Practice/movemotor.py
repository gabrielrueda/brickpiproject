import brickpi3
import time

speed = 20
irvalue = 100
BP = brickpi3.BrickPi3() # Must have this - creates instance of brickpi

# Sets up a infared sensor - similiar for any other sensors


try:

    while irvalue > 20:
        
        # Runs Motors A and D
        BP.set_motor_power(BP.PORT_A, speed)
        BP.set_motor_power(BP.PORT_D, (speed*0.95))

        
        
        # delay for 0.02 seconds to reduce the Raspberry Pi CPU load.
        time.sleep(0.02) 

    # Stops motors
    BP.set_motor_power(BP.PORT_A, 0)
    BP.set_motor_power(BP.PORT_D, 0)

except KeyboardInterrupt: # the program gets interrupted by Ctrl+C on the keyboard.
    BP.reset_all() 