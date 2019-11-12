import brickpi3
import time

BP = brickpi3.BrickPi3()

speed = 30
turnSpeed = 50
encoders = [100,100]

def moveForward():
    BP.set_motor_power(BP.PORT_A, -speed)
    BP.set_motor_power(BP.PORT_D, -speed)

def moveBackward():
    BP.set_motor_power(BP.PORT_A, speed)
    BP.set_motor_power(BP.PORT_D, speed)

def turnRight90():
    motorsPos = [BP.get_motor_encoder(BP.PORT_A),BP.get_motor_encoder(BP.PORT_D)]

    while(BP.get_motor_encoder(BP.PORT_A) - motorsPos[0] > encoders[0]):
        BP.set_motor_power(BP.PORT_A, turnSpeed / 10)
        BP.set_motor_power(BP.PORT_D, turnSpeed)
        time.sleep(0.02)
    
    BP.set_motor_power(BP.PORT_A, 0)
    BP.set_motor_power(BP.PORT_D, 0)

def turnLeft90():
    motorsPos = [BP.get_motor_encoder(BP.PORT_A),BP.get_motor_encoder(BP.PORT_D)]

    while(BP.get_motor_encoder(BP.PORT_D) - motorsPos[1] < encoders[1]):
        BP.set_motor_power(BP.PORT_A, turnSpeed)
        BP.set_motor_power(BP.PORT_D, turnSpeed / 10)
        time.sleep(0.02)
    
    BP.set_motor_power(BP.PORT_A, 0)
    BP.set_motor_power(BP.PORT_D, 0)

def turnCustom(leftPower,rightPower):
    BP.set_motor_power(BP.PORT_A, leftPower)
    BP.set_motor_power(BP.PORT_D, rightPower)

def stop():
    BP.set_motor_power(BP.PORT_A, 0)
    BP.set_motor_power(BP.PORT_D, 0)