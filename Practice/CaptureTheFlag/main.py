import drive
import clamp
import config
import time     
import brickpi3
import objectavoidance_ctf

BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.

#Sensors
# pylint: disable=no-member
BP.set_sensor_type(BP.PORT_3, BP.SENSOR_TYPE.EV3_COLOR_REFLECTED)
BP.set_sensor_type(BP.PORT_2, BP.SENSOR_TYPE.EV3_ULTRASONIC_CM)
BP.set_sensor_type(BP.PORT_4, BP.SENSOR_TYPE.EV3_ULTRASONIC_CM)
wallfollowing = False

def main():
    wallfollowing = False
    while True:
        try:
            lightValue = BP.get_sensor(BP.PORT_3)
        except brickpi3.SensorError as error:
            print(error)

        # if(lightValue < 45):
        #     clamp.flagGrab()

        if(wallfollowing):
            if(objectavoidance_ctf.checkObject() == False):
                pass
            else:
                wallfollowing == False
        else:
            wallfollowing = objectavoidance_ctf.avoidance()
        
       
        time.sleep(0.02)

try:
    config.configAll()
    main()


except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
    BP.reset_all()