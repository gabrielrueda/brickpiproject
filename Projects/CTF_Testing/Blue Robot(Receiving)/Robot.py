#!/usr/bin/env python
import drive
import config
import time     
import brickpi3
import linefollowing_ctf
import objectavoidance
import head
import clamp
import bluetooth
# import main

BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.

#Sensors
# pylint: disable=no-member
BP.set_sensor_type(BP.PORT_3, BP.SENSOR_TYPE.EV3_COLOR_REFLECTED)
BP.set_sensor_type(BP.PORT_4, BP.SENSOR_TYPE.EV3_ULTRASONIC_CM)
# BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.TOUCH)

hostMACAddress = 'B8:27:EB:55:C0:33' # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
port = 3
backlog = 1
size = 1024
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.bind((hostMACAddress, port))
s.listen(backlog)

colour = ["none", "Black", "Blue", "Green", "Yellow", "Red", "White", "Brown"]
uValue = 255

def mainFunction():
    client, clientInfo = s.accept()
    o = objectavoidance.avoidanceofObjects()
    while(True):
        o.main()
        if(colour[getColour()] == "Yellow"):
            clamp.flagGrab()
        if(getReflected() < 27):
            BP.set_motor_power(BP.PORT_B, 0)
            linefollowing_ctf.linefollowing()
        if(colour[getColour()] == "Red"):
            if(uValue < 70):
                drive.turnLeft90()
            else:
                drive.turnRight90()
        
        data = client.recv(size)
        if(data == "end"):
            break

        time.sleep(0.02)

    BP.reset_all()

def getColour():
    try:
        BP.set_sensor_type(BP.PORT_3, BP.SENSOR_TYPE.EV3_COLOR_COLOR)  
        time.sleep(0.02)
        return BP.get_sensor(BP.PORT_3)

    except brickpi3.SensorError as error:
        print(error)

def getReflected():
    try:
        BP.set_sensor_type(BP.PORT_3, BP.SENSOR_TYPE.EV3_COLOR_REFLECTED)
        time.sleep(0.02)
        return BP.get_sensor(BP.PORT_3)
    except brickpi3.SensorError as error:
        print(error)

# def getTouch():
#     while True:
#         try:
#             # touchValue = BP.get_sensor(BP.PORT_1)
#             # print(touchValue)
#             return BP.get_sensor(BP.PORT_1)
#         except brickpi3.SensorError as error:
#             return error
        
try:
    config.configAll()
    mainFunction()

except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
    BP.reset_all()