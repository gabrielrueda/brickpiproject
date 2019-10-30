import brickpi3 
import time
import drive
import config

speed = 20
uValueC = 255
uValueR = 255
encoders = [-155,155]
colour = ["none", "Black", "Blue", "Green", "Yellow", "Red", "White", "Brown"]

BP = brickpi3.BrickPi3()

# pylint: disable=no-member
BP.set_sensor_type(BP.PORT_2, BP.SENSOR_TYPE.EV3_ULTRASONIC_CM)
BP.set_sensor_type(BP.PORT_4, BP.SENSOR_TYPE.EV3_ULTRASONIC_CM)

def avoidance():
        uValueC = 70
        try:
            uValueC = BP.get_sensor(BP.PORT_2)               
        except brickpi3.SensorError as error:
            print(error)
        if(uValueC == 0):
            drive.stop()
            return False
        else:
            if(uValueC <= 5):
                drive.turnLeft90()
                return True
            else:
                drive.moveForward()
                return False

def checkObject():
    
    uValueR = 19
    try:
        uValueC = BP.get_sensor(BP.PORT_2)                   
    except brickpi3.SensorError as error:
        print(error)

    try:
        uValueR = BP.get_sensor(BP.PORT_4)                   
    except brickpi3.SensorError as error:
        print(error)

    p = -1
    error = (uValueR - 5) * p
    BP.set_motor_power(BP.PORT_A, speed + (error * 0.8))
    BP.set_motor_power(BP.PORT_D, speed - (error * 0.8))

    if(uValueR > 20):
        passingTime()
        return False
    elif(uValueC <= 5):
        drive.turnLeft90()
        return False
    else:
        return True

def passingTime():
    before = time.time()
    uValueC = 60
    while(round(time.time() - before,1) <= 2.1):
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