import brickpi3 
import time

BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.
l_limit = 0
r_Limit = 0
c_Encoder = 0
speed = 60

def limits(left, right):
    c_Encoder = BP.get_motor_encoder(BP.PORT_B)
    l_limit = BP.get_motor_encoder(BP.PORT_B) + left
    r_limit = BP.get_motor_encoder(BP.PORT_B) - right

def returnCenter():
    print("Centre")
    currentEValue= BP.get_motor_encoder(BP.PORT_B)
    if(currentEValue > c_Encoder):
        while(currentEValue > c_Encoder):
            BP.set_motor_power(BP.PORT_B, -speed)
            currentEValue = BP.get_motor_encoder(BP.PORT_B)
            time.sleep(0.02)
    else:
        while(currentEValue < c_Encoder):
            BP.set_motor_power(BP.PORT_B, speed)
            currentEValue = BP.get_motor_encoder(BP.PORT_B)
            time.sleep(0.02)

def turnLeft():
    print("Left.")
    currentEValue= 0
    while(currentEValue < l_limit):
        BP.set_motor_power(BP.PORT_B, speed)
        currentEValue = BP.get_motor_encoder(BP.PORT_B)
        time.sleep(0.02)

def turnRight():
    print("Left Limit:" + str(l_limit))
    currentEValue= 0
    while(currentEValue > r_limit):
        BP.set_motor_power(BP.PORT_B, -speed)
        currentEValue = BP.get_motor_encoder(BP.PORT_B)
        time.sleep(0.02)