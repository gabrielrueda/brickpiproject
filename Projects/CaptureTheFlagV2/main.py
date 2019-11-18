import drive
import config
import time     
import brickpi3
import linefollowing_ctf
import objectavoidance
import head

BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.

#Sensors
# pylint: disable=no-member
BP.set_sensor_type(BP.PORT_3, BP.SENSOR_TYPE.EV3_COLOR_REFLECTED)
BP.set_sensor_type(BP.PORT_4, BP.SENSOR_TYPE.EV3_ULTRASONIC_CM)


colour = ["none", "Black", "Blue", "Green", "Yellow", "Red", "White", "Brown"]

def main():
    # linefollowing_ctf.linefollowing()
    o = objectavoidance.avoidanceofObjects()
    while(True):
        o.main()
    BP.reset_all()
try:
    config.configAll()
    main()

except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
    BP.reset_all()