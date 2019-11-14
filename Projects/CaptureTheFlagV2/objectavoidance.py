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

h = head.Head(107,107)
def avoidance():
        uValue = 70
        uValue = getUltrasonic()
        if(uValue == 0):
            drive.stop()
        else:
            if(uValue <= 5):
                #INSERT DIRECTION RANDOMIZER
                drive.turnLeft90()
                h.turnRight()
                time.sleep(1)
                h.returnCenter()
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

# def passingTime():
#     before = time.time()
#     uValueC = 60
#     while(round(time.time() - before,1) <= 2.1):
#         colourValue = 0
#         try:
#             BP.set_sensor_type(BP.PORT_3, BP.SENSOR_TYPE.EV3_COLOR_COLOR)  
#             colourValue = BP.get_sensor(BP.PORT_3)
#         except brickpi3.SensorError as error:
#             print(error)

#         if(uValueC <= 3 or uValueC == 255 or colour[colourValue] == "Red"):
#             break
#         try:
#             uValueC = BP.get_sensor(BP.PORT_2)               
#         except brickpi3.SensorError as error:
#             print(error)
#         drive.moveForward()

#     BP.set_motor_power(BP.PORT_A, 0)
#     BP.set_motor_power(BP.PORT_D, 0)
#     drive.turnRight90()

def getUltrasonic():
    try:
        return BP.get_sensor(BP.PORT_4)
    except brickpi3.SensorError as error:
        print(error)
        return 0