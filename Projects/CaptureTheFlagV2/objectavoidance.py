import brickpi3 
import time
import drive
import config
import head
import random

speed = 20
uValue = 255
encoders = [-155,155]
colour = ["none", "Black", "Blue", "Green", "Yellow", "Red", "White", "Brown"]

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
                if(uValue <= 5):
                    self.direction = random.randint(0, 1)
                    if(self.direction == 0):
                        drive.turnLeft90()
                        self.h.turnRight()
                    else:
                        drive.turnRight90()
                        self.h.turnLeft()  
                    
                    self.switcher = 1
                else:
                    drive.moveForward()

    def checkObject(self):

        uValue = self.getUltrasonic()

        p = -1
        error = (uValue - 17) * p
        BP.set_motor_power(BP.PORT_A, -speed - (error * 0.8))
        BP.set_motor_power(BP.PORT_D, -speed + (error * 0.8))
        print(uValue)

        if(uValue > 30):
            self.switcher = 2

    def aroundObject(self):
        if(self.direction == 0):
            drive.turnCustom(20,60)
        else:
            drive.turnCustom(60,20)

    def getUltrasonic(self):
        try:
            return BP.get_sensor(BP.PORT_4)
        except brickpi3.SensorError as error:
            print(error)
            return 0