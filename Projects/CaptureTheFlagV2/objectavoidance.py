import brickpi3
import time
import drive
import config

uValue = 255
speed = 20
rightLimit = 0
leftLimit = 0
centreEncoder = 0
currentEValue = 0
leftDistance = 0
rightDistance = 0

BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.

# pylint: disable=no-member
BP.set_sensor_type(BP.PORT_4, BP.SENSOR_TYPE.EV3_ULTRASONIC_CM)

def avoidance():
    uValue = 70
    try:
        uValue = BP.get_sensor(BP.PORT_4)               
    except brickpi3.SensorError as error:
        print(error)
    if(uValue == 0):
        drive.stop()
    elif(uValue <= 15):
        drive.stop()
        checkObject()
    else:
        drive.moveBackward()
    #print(uValue)

def checkObject():
    checkLeft()
    checkRight()
    returnCenter()
    BP.set_motor_power(BP.PORT_B, 0)

def checkLeft():
    currentEValue= 0
    while(currentEValue < leftLimit):
        BP.set_motor_power(BP.PORT_B, speed)
        currentEValue = BP.get_motor_encoder(BP.PORT_B)
        time.sleep(0.02)
        leftDistance == getUltrasonic()

def checkRight():
    currentEValue= 0
    while(currentEValue > rightLimit):
        BP.set_motor_power(BP.PORT_B, -speed)
        currentEValue = BP.get_motor_encoder(BP.PORT_B)
        time.sleep(0.02)
        rightDistance == getUltrasonic()

def returnCenter():
    currentEValue= 0
    while(currentEValue < centreEncoder):
        BP.set_motor_power(BP.PORT_B, speed)
        currentEValue = BP.get_motor_encoder(BP.PORT_B)
        time.sleep(0.02)
    print(leftDistance)
    print(rightDistance)

def getUltrasonic():
    try:
        return BP.get_sensor(BP.PORT_4)
    except brickpi3.SensorError as error:
        print(error)
        return 0

try:
    centreEncoder = BP.get_motor_encoder(BP.PORT_B)
    rightLimit = centreEncoder - 90
    leftLimit = centreEncoder + 90
    print("Limits are made.")
    config.configUltrasonic()
    while(True):
        avoidance()

except KeyboardInterrupt:
    BP.reset_all() 