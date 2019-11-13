import brickpi3 
import time
import drive
import config
import head

speed = 20
uValue = 255
encoders = [-155,155]
colour = ["none", "Black", "Blue", "Green", "Yellow", "Red", "White", "Brown"]

BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.

# pylint: disable=no-member
BP.set_sensor_type(BP.PORT_4, BP.SENSOR_TYPE.EV3_ULTRASONIC_CM)

def avoidance():
        uValue = 70
        uValue = getUltrasonic()
        if(uValue == 0):
            drive.stop()
        else:
            if(uValue <= 5):
                #INSERT DIRECTION RANDOMIZER
                drive.turnLeft90()
                head.turnRight()
                time.sleep(1)
                head.returnCenter()
            else:
                drive.moveForward()

def checkObject():

    uValue = getUltrasonic()

    # p = -1
    # error = (uValueR - 5) * p
    # BP.set_motor_power(BP.PORT_A, speed + (error * 0.8))
    # BP.set_motor_power(BP.PORT_D, speed - (error * 0.8))

    # if(uValue > 20):
    #     passingTime()
  
    # elif(uValueC <= 5):
    #     drive.turnLeft90()



def passingTime():
    before = time.time()
    uValueC = 60
    while(round(time.time() - before,1) <= 2.1):
        colourValue = 0
        try:
            BP.set_sensor_type(BP.PORT_3, BP.SENSOR_TYPE.EV3_COLOR_COLOR)  
            colourValue = BP.get_sensor(BP.PORT_3)
        except brickpi3.SensorError as error:
            print(error)

        if(uValueC <= 3 or uValueC == 255 or colour[colourValue] == "Red"):
            break
        try:
            uValueC = BP.get_sensor(BP.PORT_2)               
        except brickpi3.SensorError as error:
            print(error)
        drive.moveForward()

    BP.set_motor_power(BP.PORT_A, 0)
    BP.set_motor_power(BP.PORT_D, 0)
    drive.turnRight90()

# def avoidance():
#     uValue = 70
#     try:
#         uValue = BP.get_sensor(BP.PORT_4)               
#     except brickpi3.SensorError as error:
#         print(error)
#     if(uValue == 0):
#         drive.stop()
#     elif(uValue <= 15):
#         drive.stop()
#         checkObject()
#     else:
#         drive.moveBackward()
#     #print(uValue)

# def checkObject():
#     checkLeft()
#     checkRight()
#     returnCenter()
#     BP.set_motor_power(BP.PORT_B, 0)

# def checkLeft():
#     currentEValue= 0
#     while(currentEValue < leftLimit):
#         BP.set_motor_power(BP.PORT_B, speed)
#         currentEValue = BP.get_motor_encoder(BP.PORT_B)
#         time.sleep(0.02)
#         leftDistance == getUltrasonic()

# def checkRight():
#     currentEValue= 0
#     while(currentEValue > rightLimit):
#         BP.set_motor_power(BP.PORT_B, -speed)
#         currentEValue = BP.get_motor_encoder(BP.PORT_B)
#         time.sleep(0.02)
#         rightDistance == getUltrasonic()

# def returnCenter():
#     currentEValue= 0
#     while(currentEValue < centreEncoder):
#         BP.set_motor_power(BP.PORT_B, speed)
#         currentEValue = BP.get_motor_encoder(BP.PORT_B)
#         time.sleep(0.02)
#     print(leftDistance)
#     print(rightDistance)

def getUltrasonic():
    try:
        return BP.get_sensor(BP.PORT_4)
    except brickpi3.SensorError as error:
        print(error)
        return 0

# try:
#     centreEncoder = BP.get_motor_encoder(BP.PORT_B)
#     rightLimit = centreEncoder - 90
#     leftLimit = centreEncoder + 90
#     print("Limits are made.")
#     config.configUltrasonic()
#     while(True):
#         avoidance()

# except KeyboardInterrupt:
#     BP.reset_all() 