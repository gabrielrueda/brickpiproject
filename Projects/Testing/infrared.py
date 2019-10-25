import time     # import the time library for the sleep function
import brickpi3 # import the BrickPi3 drivers

BP = brickpi3.BrickPi3() 

BP.set_sensor_type(BP.PORT_2, BP.SENSOR_TYPE.EV3_INFRARED_PROXIMITY)

try:
    while True:
        try:
            print(BP.get_sensor(BP.PORT_2))   # print the infrared value
        except brickpi3.SensorError as error:
            print(error)
        
        time.sleep(0.02)  # delay for 0.02 seconds (20ms) to reduce the Raspberry Pi CPU load.

except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
    BP.reset_all()        # Unconfigure the sensors, disable the motors, and restore the LED to the control of the BrickPi3 firmware.