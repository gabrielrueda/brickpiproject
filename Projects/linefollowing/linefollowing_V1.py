import time     # import the time library for the sleep function
import brickpi3 # import the BrickPi3 drivers

BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.

BP.set_sensor_type(BP.PORT_3, BP.SENSOR_TYPE.EV3_COLOR_COLOR)

speed = 30
colour = ["none", "Black", "Blue", "Green", "Yellow", "Red", "White", "Brown"]

def linefollowing():
    value = 0
    try:
        value = BP.get_sensor(BP.PORT_3)
        print(colour[value])                # print the color
    except brickpi3.SensorError as error:
        print(error)

    if(colour[value] == "Blue" or colour[value] == "White"):
        BP.set_motor_power(BP.PORT_A, 30)
        BP.set_motor_power(BP.PORT_D, 0)
    elif(colour[value] == "Brown" or colour[value] == "Black"): 
        BP.set_motor_power(BP.PORT_A, 0)
        BP.set_motor_power(BP.PORT_D, 30)
    else:
        BP.set_motor_power(BP.PORT_A, 0)
        BP.set_motor_power(BP.PORT_D, 0)

try:
    while True:
        linefollowing()
        time.sleep(0.02)  # delay for 0.02 seconds (20ms) to reduce the Raspberry Pi CPU load.

except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
    BP.reset_all()