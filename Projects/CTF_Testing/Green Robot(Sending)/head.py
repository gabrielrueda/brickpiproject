import brickpi3 
import time

BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.

leftLimits = [0,0,0]
rightLimits = [0,0,0]
centreEncoder = 0
speed = 60
direction = [0,0]

class Head:
    def __init__(self, leftLimit, rightLimit):
        self.centreEncoder = BP.get_motor_encoder(BP.PORT_B)
        self.direction = [0,0]
        encoderValue = BP.get_motor_encoder(BP.PORT_B)
        self.leftLimits = [encoderValue + (leftLimit*0.7), encoderValue + (leftLimit*0.5), encoderValue + (leftLimit)]
        self.rightLimits = [encoderValue - (rightLimit*0.65), encoderValue - (rightLimit*0.5), encoderValue - (rightLimit)]


    def returnCentre(self):
        print("Centre")
        currentEValue = BP.get_motor_encoder(BP.PORT_B)
        if(currentEValue > self.centreEncoder):
            while(currentEValue > self.centreEncoder + 19):
                BP.set_motor_power(BP.PORT_B, -speed)
                currentEValue = BP.get_motor_encoder(BP.PORT_B)
                # time.sleep(0.02)
        else:
            while(currentEValue < self.centreEncoder - 19):
                BP.set_motor_power(BP.PORT_B, speed)
                currentEValue = BP.get_motor_encoder(BP.PORT_B)
                # time.sleep(0.02)
        BP.set_motor_power(BP.PORT_B, 0)

    def turnLeft(self):
        currentEValue = BP.get_motor_encoder(BP.PORT_B)
        while(currentEValue < self.leftLimits[2]):
            BP.set_motor_power(BP.PORT_B, speed)
            currentEValue = BP.get_motor_encoder(BP.PORT_B)
            time.sleep(0.02)
        BP.set_motor_power(BP.PORT_B, 0)

    def turnRight(self):
        currentEValue = BP.get_motor_encoder(BP.PORT_B)
        while(currentEValue > self.rightLimits[2]):
            BP.set_motor_power(BP.PORT_B, -speed)
            currentEValue = BP.get_motor_encoder(BP.PORT_B)
            time.sleep(0.02)
        BP.set_motor_power(BP.PORT_B, 0)
    
    def turnLeftScan(self):
        currentEValue = BP.get_motor_encoder(BP.PORT_B)
        if(currentEValue < self.leftLimits[1]):
            BP.set_motor_power(BP.PORT_B, (speed*0.40))
            return 0
        else:
            BP.set_motor_power(BP.PORT_B, 0)
            return 1
    
    def turnRightScan(self):
        currentEValue = BP.get_motor_encoder(BP.PORT_B)
        if(currentEValue > self.rightLimits[1]):
            BP.set_motor_power(BP.PORT_B, -(speed*0.40))
            return 1
        else:
            BP.set_motor_power(BP.PORT_B, 0)
            return 0

    def Scan(self):
        if(self.direction[1] == 0):
            self.direction[1] = self.turnLeftScan()
            return 1
        else:
            self.direction[1] = self.turnRightScan()
            if(self.direction[1] == 1):
                return 2
            else:
                return 3
        BP.set_motor_power(BP.PORT_B, 0)

    def turnLeftScanNew(self):
        currentEValue = BP.get_motor_encoder(BP.PORT_B)
        if(currentEValue < self.leftLimits[0]):
            BP.set_motor_power(BP.PORT_B, (speed*0.40))
            return 0
        else:
            BP.set_motor_power(BP.PORT_B, 0)
            return 1
    
    def turnRightScanNew(self):
        currentEValue = BP.get_motor_encoder(BP.PORT_B)
        if(currentEValue > self.rightLimits[0]):
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