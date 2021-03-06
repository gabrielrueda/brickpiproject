import brickpi3 
import time
import drive
import config
import head
import random
import statistics

speed = 20
uValue = 255
encoders = [-155,155]

BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.

# pylint: disable=no-member
class avoidanceofObjects:
    BP.set_sensor_type(BP.PORT_4, BP.SENSOR_TYPE.EV3_ULTRASONIC_CM)
    switcher = 0
    direction = 0
    ScanValues = [0,0,0]
    leftScanArray = []
    rightScanArray = []
    headAngle = 0 # 0 is for centre, 1 is for left, and 2 is for right
    i = 0

    closeToObject = False
    positionSet = False
    h = head.Head(120,107)
    def main(self):
        if(self.switcher == 0):
            self.avoidance()
        elif(self.switcher == 1):
            self.checkObject()
        elif(self.switcher == 2):
            self.aroundObject()
        else:
            print("Error")

    def getAverage(self, someArray):
        print("Old Array:" + str(someArray))
        for x in someArray:
            if(x == 255.0):
                someArray.remove(x)
        print("New Array:" + str(someArray))
        return statistics.median(someArray)

    def getLowest(self, someArray):
        print("Old Array:" + str(someArray))
        return min(someArray)

    def avoidance(self):
            uValue = 70
            uValue = self.getUltrasonic()
            # print("Avoidance:" + str(uValue))
            if(uValue <= 10):
                self.closeToObject = True
            if(uValue == 0):
                drive.stop()
            else:
                if(self.closeToObject == True):
                    if(self.ScanValues[2] == 0):
                        self.h.returnCentre()
                        drive.stop()
                        time.sleep(1)
                        self.ScanValues[2] = self.getUltrasonic()
                        print("Centre Scan Value:" + str(uValue))
                    if(self.i <= 4 and self.ScanValues[1] == 0):
                        if(self.i == 0):
                            scanV = self.h.scan(0)
                        else:
                            scanV = 3
                        if(scanV == 2):
                            self.leftScanArray.append(self.getUltrasonic())
                        elif(scanV == 3):
                            if(self.ScanValues[0] == 0):
                                self.ScanValues[0] = self.getLowest(self.leftScanArray)
                                print("Left Scan Value:" + str(self.ScanValues[0]))

                            self.rightScanArray.insert(self.i,self.getUltrasonic())
                            self.i += 1
                            print("i = " + str(self.i))
                            # print("Right Scan Value:" + str(self.getUltrasonic()))
                    elif(self.ScanValues[1] == 0):
                        self.ScanValues[1] = self.getLowest(self.rightScanArray)
                        print("Right Scan Value:" + str(self.ScanValues[1]))
                        self.i=0

                    elif(self.positionSet == False):
                        if(self.ScanValues[1] > 60):
                            self.h.turnLeft(0.7)
                            self.direction = 1
                            self.headAngle = 1
                        elif(self.ScanValues[0] > 60):
                            self.h.turnRight(0.7)
                            self.direction = 0
                            self.headAngle = 2
                        else:
                            self.h.returnCentre()
                            self.direction = random.randint(0, 1)
                            self.headAngle = 0
                        self.positionSet = True
                    else:
                        if(uValue < 5):
                            if(self.headAngle == 0):
                                if(self.direction == 0):
                                    drive.turnLeft90()
                                    self.h.turnRight(1)
                                    print("Turning Left...")
                                else:
                                    drive.turnRight90()
                                    self.h.turnLeft(1)
                                    print("Turning Right...")
                            elif(self.headAngle == 1):
                                drive.turnRight45()
                                self.h.returnCentre()
                                self.h.turnLeft(1)
                            else:
                                drive.turnLeft45()
                                self.h.returnCentre()
                                self.h.turnRight(1)
                            self.switcher = 1
                        else:
                            drive.moveForward()
                else:
                    drive.moveForward()
                    self.h.scan(1)

    def checkObject(self):
        self.closeToObject = False
        self.positionSet = False
        self.ScanValues[1] = 0
        self.ScanValues[0] = 0
        self.ScanValues[2] = 0
        self.rightScanArray = []
        self.leftScanArray = []

        uValue = self.getUltrasonic()

        p = -1
        error = (uValue - 15) * p
        if(uValue > 200):
            BP.set_motor_power(BP.PORT_A, -20)
            BP.set_motor_power(BP.PORT_D, -20)
        elif(self.direction == 0):
            BP.set_motor_power(BP.PORT_A, -speed - (error * 0.8))
            BP.set_motor_power(BP.PORT_D, -speed + (error * 0.8))
        else:
            BP.set_motor_power(BP.PORT_A, -speed + (error * 0.8))
            BP.set_motor_power(BP.PORT_D, -speed - (error * 0.8))
        print(uValue)

        if(uValue > 70 and uValue < 200):
            self.switcher = 2
            self.h.returnCentre()
            drive.moveForward()

    def aroundObject(self):
        if(self.direction == 0):
            time.sleep(0.5)
            drive.pivotTurn90(25,40,-2400)
        else:
            time.sleep(0.5)
            drive.pivotTurn90(40,25,-2400)
        
        self.switcher = 0

    def getUltrasonic(self):
        try:
            return BP.get_sensor(BP.PORT_4)
        except brickpi3.SensorError as error:
            print(error)
            return 0