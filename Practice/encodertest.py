import brickpi3
import time

BP = brickpi3.BrickPi3()

BP.set_sensor_type(BP.PORT_4, BP.SENSOR_TYPE.EV3_ULTRASONIC_CM)

encoders = [-155,155,1,1]

speed = 20

def turnRight():
    motorsPos = [BP.get_motor_encoder(BP.PORT_A),BP.get_motor_encoder(BP.PORT_D)]

    while(BP.get_motor_encoder(BP.PORT_A) - motorsPos[0] > encoders[0]):
        BP.set_motor_power(BP.PORT_A, -speed)
        BP.set_motor_power(BP.PORT_D, speed)
        print(BP.get_motor_encoder(BP.PORT_A))
        time.sleep(0.02)
    
    BP.set_motor_power(BP.PORT_A, 0)
    BP.set_motor_power(BP.PORT_D, 0)

def turn45right():
    motorsPos = [BP.get_motor_encoder(BP.PORT_A),BP.get_motor_encoder(BP.PORT_D)]

    while(BP.get_motor_encoder(BP.PORT_A) - motorsPos[0] > encoders[2]):
        BP.set_motor_power(BP.PORT_A, -speed)
        BP.set_motor_power(BP.PORT_D, speed)
        time.sleep(0.02)
    
    BP.set_motor_power(BP.PORT_A, 0)
    BP.set_motor_power(BP.PORT_D, 0)


try:
    while True:
        turnRight()
        time.sleep(1)
except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
    BP.reset_all()   