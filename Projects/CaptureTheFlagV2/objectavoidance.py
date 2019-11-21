import brickpi3 
import time
import drive
import config
import head
import random

speed = 20
uValue = 255
encoders = [-155,155]

BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.

# pylint: disable=no-member
class avoidanceofObjects:
    BP.set_sensor_type(BP.PORT_4, BP.SENSOR_TYPE.EV3_ULTRASONIC_CM)
    switcher = 0
    direction = 0
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

    def avoidance(self):
            uValue = 70
            uValue = self.getUltrasonic()
            if(uValue == 0):
                drive.stop()
            else:
                if(uValue <= 3):
                    # self.direction = random.randint(0, 1)
                    if(self.direction == 0):
                        drive.turnLeft45()
                        drive.pivotTurn45(30,10)
                        print("Done Turn")
                        self.h.turnRight()
                        time.sleep(0.5)
                    else:
                        drive.turnRight90()
                        self.h.turnLeft()   
                        time.sleep(0.5)
                    
                    self.switcher = 1
                else:
                    drive.moveForward()

    def checkObject(self):

        uValue = self.getUltrasonic()

        p = -1
        error = (uValue - 10) * p
        BP.set_motor_power(BP.PORT_A, -speed - (error * 0.8))
        BP.set_motor_power(BP.PORT_D, -speed + (error * 0.8))
        print(uValue)

        if(uValue > 60):
            self.switcher = 2
            self.h.returnCenter()
            drive.moveForward()

    def aroundObject(self):
        if(self.direction == 0):
            time.sleep(0.5)
            drive.pivotTurn90(10,30)
        else:
            time.sleep(0.5)

            drive.pivotTurn90(30,10)
        
        self.switcher = 0

    def getUltrasonic(self):
        try:
            return BP.get_sensor(BP.PORT_4)
        except brickpi3.SensorError as error:
            print(error)
            return 0