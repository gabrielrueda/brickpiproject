import time     # import the time library for the sleep function
import brickpi3 # import the BrickPi3 drivers

BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.

BP.set_sensor_type(BP.PORT_3, BP.SENSOR_TYPE.EV3_COLOR_REFLECTED)
BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.EV3_COLOR_REFLECTED)

speed = 20


def linefollowing():
    sOff = 0
    sCenter = 0
    error = 0
    
    try:
        sCenter = BP.get_sensor(BP.PORT_3)
        print(sCenter)                # print the color
    except brickpi3.SensorError as error:
        print(error)
    
    try:
        sOff = BP.get_sensor(BP.PORT_1)
        #print(sOff)                # print the color
    except brickpi3.SensorError as error:
        print(error)

    if(sCenter >= 11 and sOff >=50):
        BP.set_motor_power(BP.PORT_A, 20)
        BP.set_motor_power(BP.PORT_D, 20)
    elif(sCenter >= 11):
        BP.set_motor_power(BP.PORT_A, 20)
        BP.set_motor_power(BP.PORT_D, 20)
    elif(sCenter < 11):
        turning(sCenter,sOff)
    else:
        BP.set_motor_power(BP.PORT_A, 0)
        BP.set_motor_power(BP.PORT_D, 0)

def turning(sCenter, sOff):
    p = 0.9
    error = (sCenter - 31) * p
    if(sOff >= 50):
        BP.set_motor_power(BP.PORT_A, speed - (error * 0.8))
        BP.set_motor_power(BP.PORT_D, speed + (error * 0.8))
    elif(sOff < 25):
        BP.set_motor_power(BP.PORT_A, speed + (error * 0.8))
        BP.set_motor_power(BP.PORT_D, speed - (error * 0.8))
    else:
        pass

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
    print("Configured Sensor 1.")

    try:
        BP.get_sensor(BP.PORT_1)
    except brickpi3.SensorError:
        print("Configuring...")
        error = True
        while error:
            time.sleep(0.1)
            try:
                BP.get_sensor(BP.PORT_1)
                error = False
            except brickpi3.SensorError:
                error = True
    print("Configured Sensor 2.")

try:
    config()
    while True:
        linefollowing()
        time.sleep(0.02)  # delay for 0.02 seconds (20ms) to reduce the Raspberry Pi CPU load.

except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
    BP.reset_all()