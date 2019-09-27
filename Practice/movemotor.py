import brickpi3
import time

speed = 20
irvalue = 100
BP = brickpi3.BrickPi3() # Must have this - creates instance of brickpi

#Sets up a infared sensor - similiar for any other sensors
BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.EV3_INFRARED_PROXIMITY)

time.sleep(0.5)
try:

    while irvalue > 20:
        
        #Runs Motors A and D
        BP.set_motor_power(BP.PORT_A,-speed)
        BP.set_motor_power(BP.PORT_D, -speed)

        try:
            irvalue = BP.get_sensor(BP.PORT_1)
        except brickpi3.SensorError as error:
            print("Error")
        
        # delay for 0.02 seconds to reduce the Raspberry Pi CPU load.
        time.sleep(0.02) 

    #Stops motors
    BP.set_motor_power(BP.PORT_A, 0)
    BP.set_motor_power(BP.PORT_D, 0)

except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
    BP.reset_all() 