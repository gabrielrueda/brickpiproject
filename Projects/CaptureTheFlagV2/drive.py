import brickpi3
import time

BP = brickpi3.BrickPi3()

speed = 30
turnSpeed = 50
encoders = [-750,750,-1700,-1700]

def moveForward():
    BP.set_motor_power(BP.PORT_A, -speed)
    BP.set_motor_power(BP.PORT_D, -speed)

def moveBackward():
    BP.set_motor_power(BP.PORT_A, speed)
    BP.set_motor_power(BP.PORT_D, speed)

def turnLeft90():
    motorsPos = [BP.get_motor_encoder(BP.PORT_A),BP.get_motor_encoder(BP.PORT_D)]
    while(BP.get_motor_encoder(BP.PORT_A) - motorsPos[0] > encoders[0]):
        print(BP.get_motor_encoder(BP.PORT_A))
        BP.set_motor_power(BP.PORT_A, -turnSpeed)
        BP.set_motor_power(BP.PORT_D, turnSpeed)
        time.sleep(0.02)
    
    BP.set_motor_power(BP.PORT_A, 0)
    BP.set_motor_power(BP.PORT_D, 0)

def turnRight90():
    motorsPos = [BP.get_motor_encoder(BP.PORT_A),BP.get_motor_encoder(BP.PORT_D)]
    while(BP.get_motor_encoder(BP.PORT_A) - motorsPos[0] < encoders[1]):
        print(BP.get_motor_encoder(BP.PORT_A))
        BP.set_motor_power(BP.PORT_A, turnSpeed)
        BP.set_motor_power(BP.PORT_D, -turnSpeed)
        time.sleep(0.02)
    
    BP.set_motor_power(BP.PORT_A, 0)
    BP.set_motor_power(BP.PORT_D, 0)

def turnCustom(leftPower,rightPower):
    BP.set_motor_power(BP.PORT_A, -leftPower)
    BP.set_motor_power(BP.PORT_D, -rightPower)

def pivotTurn(leftPower,rightPower):
    # checks whether it will turn left or right
    if(leftPower > rightPower):
        motorPos = BP.get_motor_encoder(BP.PORT_A)
        # while motor has not reached encoder postion - Port A is left side
        while(BP.get_motor_encoder(BP.PORT_A) - motorPos > encoders[2]):
            BP.set_motor_power(BP.PORT_A, -leftPower)
            BP.set_motor_power(BP.PORT_D, -rightPower)
            print(BP.get_motor_encoder(BP.PORT_A))
    else:
        motorPos = BP.get_motor_encoder(BP.PORT_D)
        # while motor has not reached encoder postion - Port D is right side
        while(BP.get_motor_encoder(BP.PORT_D) - motorPos > encoders[3]):
            BP.set_motor_power(BP.PORT_A, -leftPower)
            BP.set_motor_power(BP.PORT_D, -rightPower)
            print(BP.get_motor_encoder(BP.PORT_D))
    BP.set_motor_power(BP.PORT_A, 0)
    BP.set_motor_power(BP.PORT_D, 0)

def stop():
    BP.set_motor_power(BP.PORT_A, 0)
    BP.set_motor_power(BP.PORT_D, 0)