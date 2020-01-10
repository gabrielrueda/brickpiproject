import time     # import the time library for the sleep function
import brickpi3 # import the BrickPi3 drivers

BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.

try:
    while True:
        print("Battery voltage: %6.3f" % (BP.get_voltage_battery())) # read and display the current voltages
        
        time.sleep(0.02)

except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
    BP.reset_all()