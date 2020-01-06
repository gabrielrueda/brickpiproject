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

# Blue Robot Mac Address Bluetooth: B8:27:EB:9A:F6:F0
# Green Robot Mac Address Bluetooth: B8:27:EB:55:C0:33

# serverMACAddress = 'B8:27:EB:9A:F6:F0'
# port = 3
# s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
# s.connect((serverMACAddress, port))
# devices = bluetooth.discover_devices(lookup_names=True)
# for device in devices:
#     print([_ for _ in find_service(address=device) if 'RFCOMM' in _['protocol'] ])
# # now manually select the desired device or hardcode its name/mac whatever in the script
# bt_addr = input()
# port = [_ for _ in find_service(address=bt_addr) if 'RFCOMM' in _['protocol']][0]['port']
# s = BluetoothSocket(RFCOMM)
# s.connect((bt_addr, port))

colour = ["none", "Black", "Blue", "Green", "Yellow", "Red", "White", "Brown"]
uValue = 255

def mainFunction():
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
   
try:
    config.configAll()
    mainFunction()

except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
    # s.send("end")
    # print("Finishing Program....")
    # time.sleep(3)
    # print("Finished Program")
    # s.close()
    BP.reset_all()