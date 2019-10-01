import brickpi3
import time

BP = brickpi3.BrickPi3()
BP.set_sensor_type(BP.PORT_2, BP.SENSOR_TYPE.EV3_GYRO_ABS)

speed = 50
gyro = 90

try:
    while True:
        try:
            gyro = BP.get_sensor(BP.PORT_2) 
            print(gyro)  # print the gyro sensor values
        except brickpi3.SensorError as error:
            print(error)

        if(gyro > 87):
            speed = 2 *((85-gyro)/2)
        elif(gyro < 83):
            speed = 2 * ((85-gyro)/2)
        else:
            speed = 25
        
        BP.set_motor_power(BP.PORT_A, -speed)
        BP.set_motor_power(BP.PORT_D, -speed)

        time.sleep(0.02)

except KeyboardInterrupt: # the program gets interrupted by Ctrl+C on the keyboard.
    BP.reset_all() 