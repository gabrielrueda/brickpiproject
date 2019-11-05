import drive
import config
import time     
import brickpi3

BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.

#Sensors
# pylint: disable=no-member
BP.set_sensor_type(BP.PORT_3, BP.SENSOR_TYPE.EV3_COLOR_REFLECTED)
BP.set_sensor_type(BP.PORT_2, BP.SENSOR_TYPE.EV3_ULTRASONIC_CM)
BP.set_sensor_type(BP.PORT_4, BP.SENSOR_TYPE.EV3_ULTRASONIC_CM)

wallfollowing = False
colour = ["none", "Black", "Blue", "Green", "Yellow", "Red", "White", "Brown"]

def main():
    wallfollowing = False
    drive.turnLeft90()
    drive.turnRight90()
    while True:
        drive.moveForward()
        time.sleep(0.02)

try:
    config.configAll()
    main()

except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
    BP.reset_all()