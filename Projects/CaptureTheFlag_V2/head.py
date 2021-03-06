import brickpi3 
import time

BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.
leftLimit = 0
rightLimit = 0
centreEncoder = 0
speed = 60
class Head:
    def __init__(self, leftLimit, rightLimit):
        self.centreEncoder = BP.get_motor_encoder(BP.PORT_B)
        self.leftLimit = BP.get_motor_encoder(BP.PORT_B) + leftLimit
        self.rightLimit = BP.get_motor_encoder(BP.PORT_B) - rightLimit

    def returnCenter(self):
        print("Centre")
        currentEValue= BP.get_motor_encoder(BP.PORT_B)
        if(currentEValue > self.centreEncoder):
            while(currentEValue > self.centreEncoder):
                BP.set_motor_power(BP.PORT_B, -speed)
                currentEValue = BP.get_motor_encoder(BP.PORT_B)
                time.sleep(0.02)
        else:
            while(currentEValue < centreEncoder):
                BP.set_motor_power(BP.PORT_B, speed)
                currentEValue = BP.get_motor_encoder(BP.PORT_B)
                time.sleep(0.02)
        BP.set_motor_power(BP.PORT_B, 0)

    def turnLeft(self):
        currentEValue= BP.get_motor_encoder(BP.PORT_B)
        while(currentEValue < self.leftLimit):
            BP.set_motor_power(BP.PORT_B, speed)
            currentEValue = BP.get_motor_encoder(BP.PORT_B)
            time.sleep(0.02)
        BP.set_motor_power(BP.PORT_B, 0)

    def turnRight(self):
        currentEValue= BP.get_motor_encoder(BP.PORT_B)
        while(currentEValue > self.rightLimit):
            BP.set_motor_power(BP.PORT_B, -speed)
            currentEValue = BP.get_motor_encoder(BP.PORT_B)
            time.sleep(0.02)
        BP.set_motor_power(BP.PORT_B, 0)