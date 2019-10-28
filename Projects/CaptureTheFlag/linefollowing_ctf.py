import time
import brickpi3

BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.

# pylint: disable=no-member
BP.set_sensor_type(BP.PORT_3, BP.SENSOR_TYPE.EV3_COLOR_REFLECTED)

speed = 30

def linefollowing():
    BP.set_sensor_type(BP.PORT_3, BP.SENSOR_TYPE.EV3_COLOR_REFLECTED)
    sensor = 0
    while(sensor < 45):
        try:
            sensor = BP.get_sensor(BP.PORT_3)
            print(sensor)
        except brickpi3.SensorError as error:
            print(error)
    
        turning(sensor)

def turning(sensor):
    p = 0.6
    error = (sensor - 27) * p
    BP.set_motor_power(BP.PORT_A, speed + (error * 0.8))
    BP.set_motor_power(BP.PORT_D, speed - (error * 0.8))