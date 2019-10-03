import brickpi3 
import time

speed = 20
ultravalue = 255
motorDif = [-340,340,-140,140]

BP = brickpi3.BrickPi3()

BP.set_sensor_type(BP.PORT_4, BP.SENSOR_TYPE.EV3_ULTRASONIC_CM)

def turnRight():
    motorsPos = [BP.get_motor_encoder(BP.PORT_A),BP.get_motor_encoder(BP.PORT_D)]

    while(BP.get_motor_encoder(BP.PORT_A) - motorsPos[0] > motorDif[0]):
        BP.set_motor_power(BP.PORT_A, -speed)
        BP.set_motor_power(BP.PORT_D, speed)
    
    BP.set_motor_power(BP.PORT_A, 0)
    BP.set_motor_power(BP.PORT_D, 0)

def turnLeft():
    motorsPos = [BP.get_motor_encoder(BP.PORT_A),BP.get_motor_encoder(BP.PORT_D)]

    while(BP.get_motor_encoder(BP.PORT_A) - motorsPos[0] < motorDif[1]):
        BP.set_motor_power(BP.PORT_A, speed)
        BP.set_motor_power(BP.PORT_D, -speed)
        # print(BP.get_motor_encoder(BP.PORT_A) - motorsPos[0])
    
    BP.set_motor_power(BP.PORT_A, 0)
    BP.set_motor_power(BP.PORT_D, 0)

def turn45right():
    motorsPos = [BP.get_motor_encoder(BP.PORT_A),BP.get_motor_encoder(BP.PORT_D)]

    while(BP.get_motor_encoder(BP.PORT_A) - motorsPos[0] > motorDif[2]):
        BP.set_motor_power(BP.PORT_A, -speed)
        BP.set_motor_power(BP.PORT_D, speed)
    
    BP.set_motor_power(BP.PORT_A, 0)
    BP.set_motor_power(BP.PORT_D, 0)

def turn45left():
    motorsPos = [BP.get_motor_encoder(BP.PORT_A),BP.get_motor_encoder(BP.PORT_D)]

    while(BP.get_motor_encoder(BP.PORT_A) - motorsPos[0] < motorDif[3]):
        BP.set_motor_power(BP.PORT_A, speed)
        BP.set_motor_power(BP.PORT_D, -speed)
        # print(BP.get_motor_encoder(BP.PORT_A) - motorsPos[0])
    
    BP.set_motor_power(BP.PORT_A, 0)
    BP.set_motor_power(BP.PORT_D, 0)

def checkObject():
    loop = True
    while(loop):
        print("repeating..")
        BP.set_motor_power(BP.PORT_A, -speed)
        BP.set_motor_power(BP.PORT_D, -speed)
        time.sleep(1.5)
        BP.set_motor_power(BP.PORT_A, 0)
        BP.set_motor_power(BP.PORT_D, 0)
        turnRight()
        try:
            uvalue = BP.get_sensor(BP.PORT_4) # print the distance in CM
        except brickpi3.SensorError as error:
            print(error)

        print(uvalue)  
        if(uvalue < 30 or uvalue == 255.0):
             turnLeft()
        else:  
            turn45right()
            try:
                uvalue2 = BP.get_sensor(BP.PORT_4) # print the distance in CM
            except brickpi3.SensorError as error:
                print(error)
            print(uvalue2)
            if(uvalue2 < 80 or uvalue2 == 255.0):
                print("You are in the if")
                turnLeft()
            else:
                loop = False
                print("You are in the else")

            turn45left()
        
try:
    while True:
        try:
            ultravalue = BP.get_sensor(BP.PORT_4)
            # print(ultravalue)                         # print the distance in CM
        except brickpi3.SensorError as error:
            print(error)

        if(ultravalue <= 20):
            turnLeft()
            checkObject()
            print("you are now back here")
        else:
            BP.set_motor_power(BP.PORT_A, -speed)
            BP.set_motor_power(BP.PORT_D, -speed)
       
        time.sleep(0.02)  # delay for 0.02 seconds (20ms) to reduce the Raspberry Pi CPU load.

except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
    BP.reset_all()   

