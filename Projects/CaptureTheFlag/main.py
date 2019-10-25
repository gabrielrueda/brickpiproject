import drive
import clamp
import config
import time     
import brickpi3
import objectavoidance_ctf
import linefollowing_ctf

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
    lineCounter = 0
    while True:
        try:
            BP.set_sensor_type(BP.PORT_3, BP.SENSOR_TYPE.EV3_COLOR_REFLECTED)
            time.sleep(0.02)
            reflectedValue = BP.get_sensor(BP.PORT_3)

            BP.set_sensor_type(BP.PORT_3, BP.SENSOR_TYPE.EV3_COLOR_COLOR)  
            time.sleep(0.02)
            colourValue = BP.get_sensor(BP.PORT_3)

        except brickpi3.SensorError as error:
            print(error)
        
        try:
            uValueR = BP.get_sensor(BP.PORT_4)                   
        except brickpi3.SensorError as error:
            print(error)

        if(reflectedValue < 27):
            linefollowing_ctf.linefollowing()
            lineCounter += 1
        
        if(colour[colourValue] == "Yellow"):
            if(lineCounter % 2 == 1):
                clamp.flagGrab()
            else:
                clamp.flagRelease()

        if(colour[colourValue] == "Red"):
            if(uValueR < 70):
                drive.turnLeft90()
            else:
                drive.turnRight90()
                
        if(wallfollowing):
            wallfollowing = objectavoidance_ctf.checkObject()
        else:
            wallfollowing = objectavoidance_ctf.avoidance()
        
        # print(reflectedValue)
        # clamp.holdflag()
        time.sleep(0.02)

try:
    config.configAll()
    main()

except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
    BP.reset_all()