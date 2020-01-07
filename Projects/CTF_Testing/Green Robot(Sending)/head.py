import brickpi3 
import time

BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.
leftLimit = 0
rightLimit = 0
leftLimitS = 0
rightLimitS = 0
centreEncoder = 0
directionOther = 0
speed = 60
direction = 0

class Head:
    def __init__(self, leftLimit, rightLimit):
        self.centreEncoder = BP.get_motor_encoder(BP.PORT_B)
        self.direction = 0
        self.directionOther = 0
        self.leftLimit = BP.get_motor_encoder(BP.PORT_B) + (leftLimit*0.7)
        self.rightLimit = BP.get_motor_encoder(BP.PORT_B) - (rightLimit*0.7)
        self.leftLimitS = BP.get_motor_encoder(BP.PORT_B) + (rightLimit*0.5)
        self.rightLimitS = BP.get_motor_encoder(BP.PORT_B) - (rightLimit*0.5)

    def returnCentre(self):
        print("Centre")
        currentEValue = BP.get_motor_encoder(BP.PORT_B)
        if(currentEValue > self.centreEncoder):
            while(currentEValue > self.centreEncoder):
                BP.set_motor_power(BP.PORT_B, -speed)
                currentEValue = BP.get_motor_encoder(BP.PORT_B)
                time.sleep(0.02)
        else:
            while(currentEValue < self.centreEncoder):
                BP.set_motor_power(BP.PORT_B, speed)
                currentEValue = BP.get_motor_encoder(BP.PORT_B)
                time.sleep(0.02)
        BP.set_motor_power(BP.PORT_B, 0)

    def turnLeft(self):
        currentEValue = BP.get_motor_encoder(BP.PORT_B)
        while(currentEValue < self.leftLimit):
            BP.set_motor_power(BP.PORT_B, speed)
            currentEValue = BP.get_motor_encoder(BP.PORT_B)
            time.sleep(0.02)
        BP.set_motor_power(BP.PORT_B, 0)

    def turnRight(self):
        currentEValue = BP.get_motor_encoder(BP.PORT_B)
        while(currentEValue > self.rightLimit):
            BP.set_motor_power(BP.PORT_B, -speed)
            currentEValue = BP.get_motor_encoder(BP.PORT_B)
            time.sleep(0.02)
        BP.set_motor_power(BP.PORT_B, 0)
    
    def turnLeftScan(self):
        currentEValue = BP.get_motor_encoder(BP.PORT_B)
        if(currentEValue < self.leftLimitS):
            BP.set_motor_power(BP.PORT_B, (speed*0.40))
            return 0
        else:
            BP.set_motor_power(BP.PORT_B, 0)
            return 1
    
    def turnRightScan(self):
        currentEValue = BP.get_motor_encoder(BP.PORT_B)
        if(currentEValue > self.rightLimitS):
            BP.set_motor_power(BP.PORT_B, -(speed*0.40))
            return 1
        else:
            BP.set_motor_power(BP.PORT_B, 0)
            return 0

    def Scan(self):
        if(self.directionOther == 0):
            self.directionOther = self.turnLeftScan()
            return 1
        else:
            self.directionOther = self.turnRightScan()
            if(self.directionOther == 1):
                return 2
            else:
                return 3
        BP.set_motor_power(BP.PORT_B, 0)

    def turnLeftScanNew(self):
        currentEValue = BP.get_motor_encoder(BP.PORT_B)
        if(currentEValue < self.leftLimit):
            BP.set_motor_power(BP.PORT_B, (speed*0.40))
            return 0
        else:
            BP.set_motor_power(BP.PORT_B, 0)
            return 1
    
    def turnRightScanNew(self):
        currentEValue = BP.get_motor_encoder(BP.PORT_B)
        if(currentEValue > self.rightLimit):
            BP.set_motor_power(BP.PORT_B, -(speed*0.40))
            return 1
        else:
            BP.set_motor_power(BP.PORT_B, 0)
            return 0

    def scanGetValues(self):
        if(self.direction == 0):
            self.direction = self.turnLeftScanNew()
            return 1
        else:
            self.direction = self.turnRightScanNew()
            if(self.direction == 1):
                return 2
            else:
                return 3
        BP.set_motor_power(BP.PORT_B, 0)

    def stop(self):
        BP.set_motor_power(BP.PORT_B, 0)
    
    def getEncoder(self):
        return BP.get_motor_encoder(BP.PORT_B)
