# pyautogui.moveTo(100, 150)
# pyautogui.moveRel(0, 10)  # move mouse 10 pixels down
# pyautogui.dragTo(100, 150)
# pyautogui.dragRel(0, 10)  # drag mouse 10 pixels down

import pyautogui
import serial
import time

ser = serial.Serial(
    port='COM10',\
    baudrate=9600)

ser.flushInput()
print("connected to: " + ser.portstr)

centerX = 960
centerY = 540

pyautogui.moveTo( centerX, centerY )

# axX = 960
# axY = 540

# axDiff = 1
# axSignal = 1

previousMpuX = 0
previousMpuY = 0

mouseSensitivityX = 30
mouseSensitivityY = 30

while True:
    # time.sleep( 0.5 )
    ser_bytes = str(ser.readline())
    ser_bytes = ser_bytes.replace("b'", "").replace(r"\r\n'", "")
    coordinates = ser_bytes.split(",")
    
    try:
        mpuX = int( coordinates[0] )
        mpuY = int( float( coordinates[1] ) )
        mpuZ = int( float( coordinates[2] ) )
        
        mouseX, mouseY = pyautogui.position()

   
        print(  mpuY )


        if ( mpuX > 5 ) :
            if mouseX != ( centerX + 30 ) :
                pyautogui.moveTo( centerX + 30, centerY )
                
        elif ( mpuX < 5 ) :
            if mouseX != ( centerX - 30 ) :
                pyautogui.moveTo( centerX - 30, centerY)
        
        # elif ( mpuX < 5 and mpuX > -5 ) :
        #     if ( mouseX != centerX ) :
        #         pyautogui.moveTo( centerX, centerY )


            
        # if ( mpuX > 10 or mpuX < -10 ) :
        #     if mouseX != ( centerX + mpuX ) :
        #         pyautogui.moveTo( centerX + mpuX, centerY )
        #         time.sleep( 0.1 )
            
        # elif ( mpuX < 10 and mpuX > -10 ) :
        #     if ( mouseX != centerX ) :
        #         pyautogui.moveTo( centerX, centerY )
        #         time.sleep( 0.1 )

            
        # print( mpuX )

        # time.sleep( 0.1 )

    except ValueError:
        pass 
    
    
    # mouseX, mouseY = pyautogui.position()
          
    # if mpuX > previousMpuX :
    #     mouseX -= mouseSensitivityX
  
    # if mpuX < previousMpuX :
    #     mouseX += mouseSensitivityX
  
    # if mpuY > previousMpuY :
    #     mouseY -= mouseSensitivityY
  
    # if mpuY < previousMpuY :
    #     mouseY += mouseSensitivityY

    # previousMpuX = mpuX
    # previousMpuY = mpuY

    # pyautogui.moveTo( mouseX, mouseY )

########################

    # print( mpuX + " " + mpuY + " " + mpuZ)
    # print( "x= " + str(x) + " y=" + str(y) )

    # pyautogui.moveTo( axX + axDiff, axY )

    # if axDiff > 5 or axDiff < 0 :
        # axSignal = -axSignal

    # axDiff += axSignal
  

    
