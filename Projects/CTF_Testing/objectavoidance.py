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
    leftScanValue = 0
    rightScanValue = 0
    centreScanValue = 0
    leftScanArray = []

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

        print("Median Left Value:" + str(statistics.median(someArray)))

        return sum(someArray) / len(someArray)

    def avoidance(self):
            uValue = 70
            uValue = self.getUltrasonic()
            if(uValue <= 15):
                self.closeToObject = True
            if(uValue == 0):
                drive.stop()
            else:
                if(self.closeToObject == True):
                    if(self.centreScanValue == 0):
                        self.h.returnCenter()
                        drive.stop()
                        time.sleep(1)
                        self.centreScanValue = self.getUltrasonic()
                        print("Centre Scan Value:" + str(uValue))
                    if(self.rightScanValue == 0):
                        scanV = self.h.scanGetValues()
                        if(scanV == 2):
                            # self.leftScanValue = self.getUltrasonic()
                            self.leftScanArray.append(self.getUltrasonic())
                            # print("Left Scan Value:" + str(uValue))
                        elif(scanV == 3):
                            if(self.leftScanValue == 0):
                                self.leftScanValue = self.getAverage(self.leftScanArray)
                                # print("Left Scan Possible Values:" + str(self.leftScanArray))
                                print("Left Scan Value:" + str(self.leftScanValue))

                            self.rightScanValue = self.getUltrasonic()
                            print("Right Scan Value:" + str(uValue))
                    elif(self.positionSet == False):
                        if(self.leftScanValue - self.rightScanValue > 10):
                            print("Head Turns Left")
                            self.h.turnLeft()
                        elif(self.leftScanValue - self.rightScanValue < -10):
                            print("Head Turns Left")
                            self.h.turnRight()
                        else:
                            self.h.returnCenter()
                        self.positionSet = True
                    else:
                        if(uValue < 5):
                            drive.stop()
                        else:
                            drive.moveForward()
                    
                     

                    # # self.direction = random.randint(0, 1)
                    # if(self.direction == 0):
                    #     # drive.revPivotTurn45(0,-30)
                    #     # drive.pivotTurn45(30,0)
                    #     self.h.stop()
                    #     drive.pivotTurn90(40,-20,-1000)
                    #     self.h.turnRight()
                    #     uValue = self.getUltrasonic()
                    #     time.sleep(1)
                    # else:
                    #     self.h.stop()
                    #     drive.turnRight45()
                    #     drive.pivotTurn45(10,30)
                    #     self.h.turnLeft()   
                    #     time.sleep(1)
                    
                    # self.switcher = 1
                else:
                    drive.moveForward()
                    self.h.Scan()

    def checkObject(self):

        uValue = self.getUltrasonic()

        p = -1
        error = (uValue - 10) * p
        if(self.direction == 0):
            BP.set_motor_power(BP.PORT_A, -speed - (error * 0.8))
            BP.set_motor_power(BP.PORT_D, -speed + (error * 0.8))
        else:
            BP.set_motor_power(BP.PORT_A, -speed + (error * 0.8))
            BP.set_motor_power(BP.PORT_D, -speed - (error * 0.8))
        print(uValue)

        if(uValue > 40):
            self.switcher = 2
            self.h.returnCenter()
            drive.moveForward()

    def aroundObject(self):
        if(self.direction == 0):
            time.sleep(0.5)
            # drive.pivotTurn90(20,40)
            drive.pivotTurn90(20,40,-2400)
        else:
            time.sleep(0.5)
            drive.pivotTurn90(40,20,-2400)
        
        self.switcher = 0

    def getUltrasonic(self):
        try:
            return BP.get_sensor(BP.PORT_4)
        except brickpi3.SensorError as error:
            print(error)
            return 0