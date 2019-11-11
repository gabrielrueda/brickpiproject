import time
import brickpi3

BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.

# pylint: disable=no-member
BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.TOUCH)

try:
    while True:

        try:
            value = BP.get_sensor(BP.PORT_1)
            print(value)
        except brickpi3.SensorError as error:
            print(error)
        
        time.sleep(0.02)

except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
    BP.reset_all()    