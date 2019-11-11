import brickpi3
import time
import config

BP = brickpi3.BrickPi3()
BP.set_sensor_type(BP.PORT_4, BP.SENSOR_TYPE.EV3_ULTRASONIC_CM)

uValue = 255
Hspeed = 15

def getUltrasonic():
    try:
        return BP.get_sensor(BP.PORT_4)
    except brickpi3.SensorError as error:
        print(error)
        return 0

def main():
    centreEncoder = BP.get_motor_encoder(BP.PORT_B)
    rightLimit = centreEncoder - 20
    leftLimit = centreEncoder + 40
    while(True):
        currentEValue = BP.get_motor_encoder(BP.PORT_B)
        while(currentEValue < leftLimit):
            BP.set_motor_power(BP.PORT_B, Hspeed)
            currentEValue = BP.get_motor_encoder(BP.PORT_B)
            uValue = getUltrasonic()
            time.sleep(0.02)
            if(uValue < 30):
                break

        while(currentEValue > rightLimit):
            BP.set_motor_power(BP.PORT_B, -Hspeed)
            currentEValue = BP.get_motor_encoder(BP.PORT_B)
            uValue = getUltrasonic()
            time.sleep(0.02)
            if(uValue < 30):
                break
        
        BP.reset_all()

try:
    config.configAll()
    main()
except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
    BP.reset_all()