import brickpi3
import time

speed = 90
grabLimit = -300
releaseLimit = 600

# BP = brickpi3.BrickPi3() # Must have this - creates instance of brickpi
BP = brickpi3.BrickPi3()

def grab():
    while(grabLimit < BP.get_motor_encoder(BP.PORT_C)):
        BP.set_motor_power(BP.PORT_C, -speed)
        time.sleep(0.02)
    BP.set_motor_power(BP.PORT_C, 0)

def release():
    while(releaseLimit > BP.get_motor_encoder(BP.PORT_C)):
        BP.set_motor_power(BP.PORT_C, speed)
        time.sleep(0.02)
    BP.set_motor_power(BP.PORT_C, 0)

try:
    before = time.time()
    # grabLimit = BP.get_motor_encoder(BP.PORT_C)
    # releaseLimit = grabLimit + 1200
    while(round(time.time() - before,1) <= 2.1):
        
        # Runs Motors A and D
        BP.set_motor_power(BP.PORT_C, -40)
        print(BP.get_motor_encoder(BP.PORT_C))

        time.sleep(0.02) 

    # release()
    # grab()
    # time.sleep(2)
    # release()
    # grab()
    
    BP.set_motor_power(BP.PORT_C, 0)

except KeyboardInterrupt: # the program gets interrupted by Ctrl+C on the keyboard.
    BP.reset_all() 