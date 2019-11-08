import time
import brickpi3

speed = 20
rightLimit = 0
leftLimit = 0
centreEncoder = 0
currentEValue= 0

BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.

# pylint: disable=no-member
BP.set_sensor_type(BP.PORT_4, BP.SENSOR_TYPE.EV3_ULTRASONIC_CM)
def configUltra():    
    try:
        BP.get_sensor(BP.PORT_4)
    except brickpi3.SensorError:
        print("Configuring...")
        error = True
        while error:
            time.sleep(0.1)
            try:
                BP.get_sensor(BP.PORT_4)
                error = False
            except brickpi3.SensorError:
                error = True
    print("Configured Utrasonic Sensor")

try:
    centreEncoder = BP.get_motor_encoder(BP.PORT_B)
    rightLimit = centreEncoder - 90
    leftLimit = centreEncoder + 90
    configUltra()
    while(currentEValue < leftLimit):
        BP.set_motor_power(BP.PORT_B, speed)
        currentEValue = BP.get_motor_encoder(BP.PORT_B)
        print(currentEValue)
        time.sleep(0.02)

    while(currentEValue > rightLimit):
        BP.set_motor_power(BP.PORT_B, -speed)
        currentEValue = BP.get_motor_encoder(BP.PORT_B)
        print(currentEValue)
        time.sleep(0.02)

    while(True):
        BP.set_motor_power(BP.PORT_B,0)

except KeyboardInterrupt: # the program gets interrupted by Ctrl+C on the keyboard.
    BP.reset_all() 