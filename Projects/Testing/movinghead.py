import time
import brickpi3

speed = 20
rightLimit = 0
leftLimit = 0
centreEncoder = 0

BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.

# pylint: disable=no-member
BP.set_sensor_type(BP.PORT_4, BP.SENSOR_TYPE.EV3_ULTRASONIC_CM)

try:

    centreEncoder = BP.get_motor_encoder(BP.PORT_B)
    rightLimit = centreEncoder - 50
    leftLimit = centreEncoder + 50

    while BP.get_motor_encoder(BP.PORT_B) < leftLimit:
        BP.set_motor_power(BP.PORT_B, speed)
        time.sleep(0.02)
        print(BP.get_motor_encoder(BP.PORT_B))

except KeyboardInterrupt: # the program gets interrupted by Ctrl+C on the keyboard.
    BP.reset_all() 