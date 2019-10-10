import brickpi3 
import time

speed = 20
ultravalue = 255
encoders = [-177,177,-76,76]

BP = brickpi3.BrickPi3()

BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.EV3_ULTRASONIC_CM)

def turnRight():
    motorsPos = [BP.get_motor_encoder(BP.PORT_A),BP.get_motor_encoder(BP.PORT_D)]

    while(BP.get_motor_encoder(BP.PORT_A) - motorsPos[0] > encoders[0]):
        BP.set_motor_power(BP.PORT_A, -speed)
        BP.set_motor_power(BP.PORT_D, (speed*0.95))
        time.sleep(0.02)
    
    BP.set_motor_power(BP.PORT_A, 0)
    BP.set_motor_power(BP.PORT_D, 0)

def turnLeft():
    motorsPos = [BP.get_motor_encoder(BP.PORT_A),BP.get_motor_encoder(BP.PORT_D)]

    while(BP.get_motor_encoder(BP.PORT_A) - motorsPos[0] < encoders[1]):
        BP.set_motor_power(BP.PORT_A, speed)
        BP.set_motor_power(BP.PORT_D, -(speed*0.95))
        time.sleep(0.02)
        # print(BP.get_motor_encoder(BP.PORT_A) - motorsPos[0])
    
    BP.set_motor_power(BP.PORT_A, 0)
    BP.set_motor_power(BP.PORT_D, 0)

def turn45right():
    motorsPos = [BP.get_motor_encoder(BP.PORT_A),BP.get_motor_encoder(BP.PORT_D)]

    while(BP.get_motor_encoder(BP.PORT_A) - motorsPos[0] > encoders[2]):
        BP.set_motor_power(BP.PORT_A, -speed)
        BP.set_motor_power(BP.PORT_D, (speed*0.95))
        time.sleep(0.02)
    
    BP.set_motor_power(BP.PORT_A, 0)
    BP.set_motor_power(BP.PORT_D, 0)

def turn45left():
    motorsPos = [BP.get_motor_encoder(BP.PORT_A),BP.get_motor_encoder(BP.PORT_D)]

    while(BP.get_motor_encoder(BP.PORT_A) - motorsPos[0] < encoders[3]):
        BP.set_motor_power(BP.PORT_A, speed)
        BP.set_motor_power(BP.PORT_D, -(speed*0.95))
        time.sleep(0.02)
        # print(BP.get_motor_encoder(BP.PORT_A) - motorsPos[0])
    
    BP.set_motor_power(BP.PORT_A, 0)
    BP.set_motor_power(BP.PORT_D, 0)

def checkObject():
    loop = True
    while(loop):
        # print("repeating..")
        BP.set_motor_power(BP.PORT_A, speed)
        BP.set_motor_power(BP.PORT_D, (speed*0.95))
        time.sleep(1.5)
        BP.set_motor_power(BP.PORT_A, 0)
        BP.set_motor_power(BP.PORT_D, 0)
        turnRight()
        try:
            uvalue = BP.get_sensor(BP.PORT_1) # print the distance in CM
        except brickpi3.SensorError as error:
            print(error)

        print(uvalue)  
        if(uvalue < 15 or uvalue == 255.0):
             turnLeft()
        else:  
            turn45right()
            try:
                uvalue2 = BP.get_sensor(BP.PORT_1) # print the distance in CM
            except brickpi3.SensorError as error:
                print(error)
            print(uvalue2)
            if(uvalue2 < 105 or uvalue2 == 255.0):
                turnLeft()
            else:
                loop = False

            turn45left()

def config():
    try:
        BP.get_sensor(BP.PORT_1)
    except brickpi3.SensorError:
        print("Configuring...")
        error = True
        while error:
            time.sleep(0.1)
            try:
                BP.get_sensor(BP.PORT_1)
                error = False
            except brickpi3.SensorError:
                error = True
    print("Configured Sensor")

try:
    config()
    while True:
        try:
            ultravalue = BP.get_sensor(BP.PORT_1)
            # print(ultravalue)                         # print the distance in CM
        except brickpi3.SensorError as error:
            print(error)

        if(ultravalue <= 15):
            print(ultravalue)
            turnLeft()
            checkObject()
        else:
            BP.set_motor_power(BP.PORT_A, speed)
            BP.set_motor_power(BP.PORT_D, (speed*0.95))
       
        time.sleep(0.02)  # delay for 0.02 seconds (20ms) to reduce the Raspberry Pi CPU load.

except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
    BP.reset_all()   

