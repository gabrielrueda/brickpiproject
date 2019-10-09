import time
import brickpi3

BP = brickpi3.BrickPi3()

BP.set_sensor_type(BP.PORT_3, BP.SENSOR_TYPE.EV3_COLOR_REFLECTED)

def config():
    try:
        BP.get_sensor(BP.PORT_3)
    except brickpi3.SensorError:
        print("Configuring...")
        error = True
        while error:
            time.sleep(0.1)
            try:
                BP.get_sensor(BP.PORT_3)
                error = False
            except brickpi3.SensorError:
                error = True
    print("Configured Sensor")

def sensorValue():
    try:
        sensor = BP.get_sensor(BP.PORT_3)
        # print(sensor)                # print the color
    except brickpi3.SensorError as error:
        print(error)
    return sensor

def moveForward():
    BP.set_motor_power(BP.PORT_A, 20)
    BP.set_motor_power(BP.PORT_D, 20)

