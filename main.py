from Display import *
import time
import serial
import json
from graphics import *

controller = Controller.CreateController()

leftJoyStickCenterPos = controller.leftJoyStickCenterPos
rightJoyStickCenterPos = controller.rightJoyStickCenterPos

port = '/dev/ttyUSB0'                  # Replace with your port name
baud_rate = 115200                     # Replace with the baud rate you chose in Arduino

serialConn = serial.Serial(port, baud_rate, timeout=1)

print(f"Connected to {port} at {baud_rate} baud.")
time.sleep(2)

while True:

    key = win.checkKey()            #if escape key is pressed, close application
    if key == "Escape":             
        break
    else:
        if serialConn.in_waiting > 0:
            response = serialConn.readline().decode('utf-8').rstrip()
            #print(f"Received: {response}")
            
            ArduinoData = None
            try:
                ArduinoData = json.loads(response)
            except:
                print("failed to parse json: " + response)
                pass
            
            if (type(ArduinoData) is not json):
                pass
            
            # loop through the arduino data
            try:
                for ArduinocomponentName, ArduinoState in ArduinoData.items():
                
                    # loop through the python-based controller components
                    for component in controller.Components:
                    
                        # find the component that matches
                        if component.Name == ArduinocomponentName:
                        
                            # The value of the component can be a bool, int, arr

                            # buttons
                            if (type(ArduinoState) is bool):
                                if (ArduinoState):
                                    component.Drawing.setFill("red")
                                else:
                                    component.Drawing.setFill("white")

                            # Triggers ( L2 or R2 )
                            if (type(ArduinoState) is int):
                                val = 255 - ArduinoState
                                component.Drawing.setFill(color_rgb(255, val, val))

                                if component.Name == "L2":
                                    controller.L2Label.setText( str(ArduinoState) + " / 255")
                                else:
                                    controller.R2Label.setText( str(ArduinoState) + " / 255")

                            # joysticks
                            elif (isinstance(ArduinoState, list)):

                                x = ArduinoState[0]
                                y = ArduinoState[1]

                                component.Drawing.undraw()
                                if component.Name == "LStickPos":
                                    component.Drawing = Circle(Point(leftJoyStickCenterPos.x + x * 0.25, leftJoyStickCenterPos.y - y * 0.25), 2)
                                    controller.LeftJoystickLabel.setText("[ " + str(x) + " , " + str(y) + " ]")
                                else:
                                    component.Drawing = Circle(Point(rightJoyStickCenterPos.x + x * 0.25, rightJoyStickCenterPos.y - y * 0.25), 2)
                                    controller.RightJoystickLabel.setText("[ " + str(x) + " , " + str(y) + " ]")
                                
                                component.Drawing.setFill("red")
                                component.Drawing.draw(win)
                                
            except Exception as error:
                print("An exception occurred:", error) 
                pass

win.close()         
