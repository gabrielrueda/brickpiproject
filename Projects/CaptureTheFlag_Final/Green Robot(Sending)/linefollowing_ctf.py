import time
import brickpi3
import drive

BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.

# pylint: disable=no-member
BP.set_sensor_type(BP.PORT_3, BP.SENSOR_TYPE.EV3_COLOR_REFLECTED)

speed = -30

def linefollowing():
    BP.set_sensor_type(BP.PORT_3, BP.SENSOR_TYPE.EV3_COLOR_REFLECTED)
    sensor = 0
    elapsedTime = 0
    maxTime = 17
    startTime = time.time()
    while(sensor < 90):
        try:
            sensor = BP.get_sensor(BP.PORT_3)
        except brickpi3.SensorError as error:
            print(error)
        
        elapsedTime = round(time.time() - startTime,1)
        if(elapsedTime <= maxTime):
            turning(sensor)
        else:
            drive.revPivotTurn45(-30,-15)
            drive.moveFast()
            time.sleep(0.1)
            drive.stop()
            break
        time.sleep(0.02)

def turning(sensor): # correct robot position to follow line
    p = 0.8
    error = (sensor - 30) * p
    BP.set_motor_power(BP.PORT_A, speed + (error * 0.8))
    BP.set_motor_power(BP.PORT_D, speed - (error * 0.8))