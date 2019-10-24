import brickpi3
import time
import drive

speed = 90
grabLimit = -300
releaseLimit = 600

BP = brickpi3.BrickPi3() # Must have this - creates instance of brickpi
    
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

def flagGrab():
    drive.turnLeft90()
    drive.turnLeft90()
    release()
    drive.moveBackward()
    time.sleep(1)
    drive.stop()
    grab()

# def holdflag():
#     BP.set_motor_power(BP.PORT_C, -10)
    

try:
    # before = time.time()
    grabLimit = BP.get_motor_encoder(BP.PORT_C) + 50
    releaseLimit = grabLimit + 1200
    print("Limits are made.")

    # release()
    # grab()
    # time.sleep(2)
    # release()
    # grab()
    
    # BP.set_motor_power(BP.PORT_C, 0)
    pass
except KeyboardInterrupt: # the program gets interrupted by Ctrl+C on the keyboard.
    BP.reset_all() 