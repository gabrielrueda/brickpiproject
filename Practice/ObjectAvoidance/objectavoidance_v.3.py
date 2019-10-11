import brickpi3 
import time

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
            # print("Center: " + str(uValueC))                        
        except brickpi3.SensorError as error:
            print(error)
        if(uValueC < 15):
            turnLeft()
        else:
            BP.set_motor_power(BP.PORT_A, speed)
            BP.set_motor_power(BP.PORT_D, speed)
    time.sleep(0.02)

def checkObject():
    try:
        uValueR = BP.get_sensor(BP.PORT_4)
        # print("Right: " + str(uValueR))                        
    except brickpi3.SensorError as error:
        print(error)

    while(uValueR < 30):
        p = 0.9
        error = (uValueR - 15) * p
        BP.set_motor_power(BP.PORT_A, speed + (error * 0.8))
        BP.set_motor_power(BP.PORT_D, speed - (error * 0.8))
        try:
            uValueR = BP.get_sensor(BP.PORT_4)
            # print("Center: " + str(uValueR))                        
        except brickpi3.SensorError as error:
            print(error)
        print("In the while")

    BP.set_motor_power(BP.PORT_A, 0)
    BP.set_motor_power(BP.PORT_D, 0)
    turnRight()

def turnRight():
    motorsPos = [BP.get_motor_encoder(BP.PORT_A),BP.get_motor_encoder(BP.PORT_D)]

    while(BP.get_motor_encoder(BP.PORT_A) - motorsPos[0] > encoders[0]):
        BP.set_motor_power(BP.PORT_A, -speed)
        BP.set_motor_power(BP.PORT_D, speed)
        time.sleep(0.02)
    
    BP.set_motor_power(BP.PORT_A, 0)
    BP.set_motor_power(BP.PORT_D, 0)

def turnLeft():
    motorsPos = [BP.get_motor_encoder(BP.PORT_A),BP.get_motor_encoder(BP.PORT_D)]

    while(BP.get_motor_encoder(BP.PORT_A) - motorsPos[0] < encoders[1]):
        BP.set_motor_power(BP.PORT_A, speed)
        BP.set_motor_power(BP.PORT_D, -speed)
        time.sleep(0.02)
        # print(BP.get_motor_encoder(BP.PORT_A) - motorsPos[0])
    
    BP.set_motor_power(BP.PORT_A, 0)
    BP.set_motor_power(BP.PORT_D, 0)


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

