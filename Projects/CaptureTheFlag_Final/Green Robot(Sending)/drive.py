import brickpi3
import time

BP = brickpi3.BrickPi3()

speed = 30
turnSpeed = 50
encoders = [-705,705,-2400,-2400,-375,375,-900,-900]


def moveForward():
    BP.set_motor_power(BP.PORT_A, -speed)
    BP.set_motor_power(BP.PORT_D, -speed)

def moveFast(): 
    BP.set_motor_power(BP.PORT_A, -100) 
    BP.set_motor_power(BP.PORT_D, -100) 

def moveBackward():
    BP.set_motor_power(BP.PORT_A, speed)
    BP.set_motor_power(BP.PORT_D, speed)

def turnLeft90():
    motorsPos = [BP.get_motor_encoder(BP.PORT_A),BP.get_motor_encoder(BP.PORT_D)]
    while(BP.get_motor_encoder(BP.PORT_A) - motorsPos[0] > encoders[0]):
        BP.set_motor_power(BP.PORT_A, -turnSpeed)
        BP.set_motor_power(BP.PORT_D, turnSpeed)
        time.sleep(0.02)
    
    BP.set_motor_power(BP.PORT_A, 0)
    BP.set_motor_power(BP.PORT_D, 0)

def turnLeft45():
    motorsPos = [BP.get_motor_encoder(BP.PORT_A),BP.get_motor_encoder(BP.PORT_D)]
    while(BP.get_motor_encoder(BP.PORT_A) - motorsPos[0] > encoders[4]):
        BP.set_motor_power(BP.PORT_A, -turnSpeed)
        BP.set_motor_power(BP.PORT_D, turnSpeed)
        time.sleep(0.02)
    
    BP.set_motor_power(BP.PORT_A, 0)
    BP.set_motor_power(BP.PORT_D, 0)

def turnRight90():
    motorsPos = [BP.get_motor_encoder(BP.PORT_A),BP.get_motor_encoder(BP.PORT_D)]
    while(BP.get_motor_encoder(BP.PORT_A) - motorsPos[0] < encoders[1]):
        BP.set_motor_power(BP.PORT_A, turnSpeed)
        BP.set_motor_power(BP.PORT_D, -turnSpeed)
        time.sleep(0.02)
    
    BP.set_motor_power(BP.PORT_A, 0)
    BP.set_motor_power(BP.PORT_D, 0)

def turnRight45():
    motorsPos = [BP.get_motor_encoder(BP.PORT_A),BP.get_motor_encoder(BP.PORT_D)]
    while(BP.get_motor_encoder(BP.PORT_A) - motorsPos[0] < encoders[5]):
        BP.set_motor_power(BP.PORT_A, turnSpeed)
        BP.set_motor_power(BP.PORT_D, -turnSpeed)
        time.sleep(0.02)
    
    BP.set_motor_power(BP.PORT_A, 0)
    BP.set_motor_power(BP.PORT_D, 0)


def turnCustom(leftPower,rightPower):
    BP.set_motor_power(BP.PORT_A, -leftPower)
    BP.set_motor_power(BP.PORT_D, -rightPower)

def pivotTurn45(leftPower,rightPower):
    if(leftPower > rightPower):
        motorPos = BP.get_motor_encoder(BP.PORT_A)
        while(BP.get_motor_encoder(BP.PORT_A) - motorPos > encoders[6]):
            BP.set_motor_power(BP.PORT_A, -leftPower)
            BP.set_motor_power(BP.PORT_D, -rightPower)
    else:
        motorPos = BP.get_motor_encoder(BP.PORT_D)
        while(BP.get_motor_encoder(BP.PORT_D) - motorPos > encoders[7]):
            BP.set_motor_power(BP.PORT_A, -leftPower)
            BP.set_motor_power(BP.PORT_D, -rightPower)
    BP.set_motor_power(BP.PORT_A, 0)
    BP.set_motor_power(BP.PORT_D, 0)

def revPivotTurn45(leftPower,rightPower):
    if(leftPower < rightPower):
        motorPos = BP.get_motor_encoder(BP.PORT_A)
        while(BP.get_motor_encoder(BP.PORT_A) - motorPos < -encoders[6]):
            BP.set_motor_power(BP.PORT_A, -leftPower)
            BP.set_motor_power(BP.PORT_D, -rightPower)
    else:
        motorPos = BP.get_motor_encoder(BP.PORT_D)
        while(BP.get_motor_encoder(BP.PORT_D) - motorPos < -encoders[7]):
            BP.set_motor_power(BP.PORT_A, -leftPower)
            BP.set_motor_power(BP.PORT_D, -rightPower)
    BP.set_motor_power(BP.PORT_A, 0)
    BP.set_motor_power(BP.PORT_D, 0)

def pivotTurn90(leftPower,rightPower,encoder):
    if(leftPower > rightPower):
        motorPos = BP.get_motor_encoder(BP.PORT_A)
        while(BP.get_motor_encoder(BP.PORT_A) - motorPos > encoder):
            BP.set_motor_power(BP.PORT_A, -leftPower)
            BP.set_motor_power(BP.PORT_D, -rightPower)
    else:
        motorPos = BP.get_motor_encoder(BP.PORT_D)
        while(BP.get_motor_encoder(BP.PORT_D) - motorPos > encoder):
            BP.set_motor_power(BP.PORT_A, -leftPower)
            BP.set_motor_power(BP.PORT_D, -rightPower)
    BP.set_motor_power(BP.PORT_A, 0)
    BP.set_motor_power(BP.PORT_D, 0)

def stop():
    BP.set_motor_power(BP.PORT_A, 0)
    BP.set_motor_power(BP.PORT_D, 0)