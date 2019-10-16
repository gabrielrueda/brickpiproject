import brickpi3 
import time
import drive

speed = 20
uValueC = 255
uValueR = 255
encoders = [-155,155]

BP = brickpi3.BrickPi3()

BP.set_sensor_type(BP.PORT_2, BP.SENSOR_TYPE.EV3_ULTRASONIC_CM)
BP.set_sensor_type(BP.PORT_4, BP.SENSOR_TYPE.EV3_ULTRASONIC_CM)

def main():
    while True:
        try:
            uValueC = BP.get_sensor(BP.PORT_2)               
        except brickpi3.SensorError as error:
            print(error)
        if(uValueC < 5):
            drive.turnLeft90()
            checkObject()
        else:
            drive.moveForward()
    time.sleep(0.02)

def checkObject():
    uValueR = 19
    while(uValueR < 60):
        p = -1
        error = (uValueR - 5) * p
        BP.set_motor_power(BP.PORT_A, speed + (error * 0.8))
        BP.set_motor_power(BP.PORT_D, speed - (error * 0.8))
        try:
            uValueR = BP.get_sensor(BP.PORT_4)                   
        except brickpi3.SensorError as error:
            print(error)
    
    passingTime()
    BP.set_motor_power(BP.PORT_A, 0)
    BP.set_motor_power(BP.PORT_D, 0)
    drive.turnRight90()

def passingTime():
    before = time.time()
    uValueC = 60
    while(round(time.time() - before,1) <= 2.1):
        if(uValueC <= 4):
            break
        try:
            uValueC = BP.get_sensor(BP.PORT_2)               
        except brickpi3.SensorError as error:
            print(error)
        drive.moveForward()

    # while(round(time.time() - before,1) <= 2.0 or uValueC != 255 or uValueC >= 8):
    #     drive.moveForward()
    #     time.sleep(0.02)
    #     print(round(time.time() - before,1))
    #     print(uValueC)
    #     try:
    #         uValueC = BP.get_sensor(BP.PORT_2)               
    #     except brickpi3.SensorError as error:
    #         print(error)

def config():
    try:
        BP.get_sensor(BP.PORT_2)
    except brickpi3.SensorError:
        print("Configuring...")
        error = True
        while error:
            time.sleep(0.1)
            try:
                BP.get_sensor(BP.PORT_2)
                error = False
            except brickpi3.SensorError:
                error = True
    print("Configured Center Utrasonic Sensor")
    
    try:
        BP.get_sensor(BP.PORT_4)
    except brickpi3.SensorError:
        print("Configuring...")
        error = True
        while error:
            time.sleep(0.1)
            try:
                BP.get_sensor(BP.PORT_4)
                error = False
            except brickpi3.SensorError:
                error = True
    print("Configured Right Utrasonic Sensor")

try:
    config()
    main()

except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
    BP.reset_all()   