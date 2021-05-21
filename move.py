# pyautogui.moveTo(100, 150)
# pyautogui.moveRel(0, 10)  # move mouse 10 pixels down
# pyautogui.dragTo(100, 150)
# pyautogui.dragRel(0, 10)  # drag mouse 10 pixels down

import pyautogui
import serial

ser = serial.Serial(
    port='COM9',\
    baudrate=9600)

ser.flushInput()
print("connected to: " + ser.portstr)

axX = 0
axY = 300

while True:
    ser_bytes = ser.readline()
    coordinates = str(ser_bytes).split(" ")
    mpuX = coordinates[0].replace("b'x=", "")
    mpuY = coordinates[1].replace("y=", "")
    mpuZ = coordinates[2].replace("z=", "").replace("\\r\\n'", "")
    
    axX += 5
    if axX > 1400 : 
        axX = 1400
    

    pyautogui.moveTo( axX, axY )

    # print( mpuX + " " + mpuY + " " + mpuZ)
    
