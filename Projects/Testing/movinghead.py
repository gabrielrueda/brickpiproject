import time
import brickpi3

BP = brickpi3.BrickPi3() # Must have this - creates instance of brickpi

centreEncoder = 0
speed = 60

def returnCentre():
    print("Centre")
    currentEValue = BP.get_motor_encoder(BP.PORT_B)
    if(currentEValue > centreEncoder):
        while(currentEValue > centreEncoder + 19):
            BP.set_motor_power(BP.PORT_B, -speed)
            currentEValue = BP.get_motor_encoder(BP.PORT_B)
    else:
        while(currentEValue < centreEncoder - 19):
            BP.set_motor_power(BP.PORT_B, speed)
            currentEValue = BP.get_motor_encoder(BP.PORT_B)
    BP.set_motor_power(BP.PORT_B, 0)

try:
    centreEncoder = BP.get_motor_encoder(BP.PORT_B)
    BP.set_motor_power(BP.PORT_B, -30)
    time.sleep(0.4)
    BP.set_motor_power(BP.PORT_B, 0)
    returnCentre()

except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
    BP.reset_all()

    #37