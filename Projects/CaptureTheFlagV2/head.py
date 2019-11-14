import brickpi3 
import time

BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.
leftLimit = 0
rightLimit = 0
centreEncoder = 0
speed = 60

def limits(left, right):
    centreEncoder = BP.get_motor_encoder(BP.PORT_B)
    leftLimit = BP.get_motor_encoder(BP.PORT_B) + left
    rightLimit = BP.get_motor_encoder(BP.PORT_B) - right

def returnCenter():
    print("Centre")
    currentEValue= BP.get_motor_encoder(BP.PORT_B)
    if(currentEValue > centreEncoder):
        while(currentEValue > centreEncoder):
            BP.set_motor_power(BP.PORT_B, -speed)
            currentEValue = BP.get_motor_encoder(BP.PORT_B)
            time.sleep(0.02)
    else:
        while(currentEValue < centreEncoder):
            BP.set_motor_power(BP.PORT_B, speed)
            currentEValue = BP.get_motor_encoder(BP.PORT_B)
            time.sleep(0.02)

def turnLeft():
    print("Left.")
    currentEValue= 0
    while(currentEValue < leftLimit):
        BP.set_motor_power(BP.PORT_B, speed)
        currentEValue = BP.get_motor_encoder(BP.PORT_B)
        time.sleep(0.02)

def turnRight():
    print("Left Limit:" + str(leftLimit))
    currentEValue= 0
    while(currentEValue > rightLimit):
        BP.set_motor_power(BP.PORT_B, -speed)
        currentEValue = BP.get_motor_encoder(BP.PORT_B)
        time.sleep(0.02)