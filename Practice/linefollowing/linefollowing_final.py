import time     # import the time library for the sleep function
import brickpi3 # import the BrickPi3 drivers

BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.

BP.set_sensor_type(BP.PORT_3, BP.SENSOR_TYPE.EV3_COLOR_REFLECTED)

speed = 20

def linefollowing():
    sensor = 0
    
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

try:
    config()
    while True:
        linefollowing()
        time.sleep(0.02)  # delay for 0.02 seconds (20ms) to reduce the Raspberry Pi CPU load.

except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
    BP.reset_all()