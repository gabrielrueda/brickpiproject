import drive
import config
import time     
import brickpi3
import linefollowing_ctf
import objectavoidance
import head
import clamp
import testSSH

BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.

#Sensors
# pylint: disable=no-member
BP.set_sensor_type(BP.PORT_3, BP.SENSOR_TYPE.EV3_COLOR_REFLECTED)
BP.set_sensor_type(BP.PORT_4, BP.SENSOR_TYPE.EV3_ULTRASONIC_CM)

colour = ["none", "Black", "Blue", "Green", "Yellow", "Red", "White", "Brown"]

def main():
    o = objectavoidance.avoidanceofObjects()
    while(True):
        o.main()
        if(colour[getColour()] == "Yellow"):
            clamp.flagGrab()
        if(getReflected() < 27):
            BP.set_motor_power(BP.PORT_B, 0)
            linefollowing_ctf.linefollowing()
            
        time.sleep(0.02)

    BP.reset_all()

def getColour():
    try:
        BP.set_sensor_type(BP.PORT_3, BP.SENSOR_TYPE.EV3_COLOR_COLOR)  
        time.sleep(0.02)
        return BP.get_sensor(BP.PORT_3)

    except brickpi3.SensorError as error:
        print(error)

def getReflected():
    try:
        BP.set_sensor_type(BP.PORT_3, BP.SENSOR_TYPE.EV3_COLOR_REFLECTED)
        time.sleep(0.02)
        return BP.get_sensor(BP.PORT_3)
    except brickpi3.SensorError as error:
        print(error)
    
try:
    # testSSH.run()
    config.configAll()
    main()

except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
    BP.reset_all()