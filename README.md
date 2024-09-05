# PS5ControllerTester
Connect ps5 controller to an esp32, and test it using a python application

1) run the arduino file. You need the libraries:
   https://github.com/rodneybakiskan/ps5-esp32
   ArduinoJson
2) Connect your ps5 controller to esp by holding the share and power button
3) Open the python file, put in your port and serial baud rate and run the file. Libraries:
   future      1.0.0
    graphics.py 5.0.1.post1
    iso8601     2.1.0
    pip         24.0
    pyserial    3.5
    PyYAML      6.0.2
    screeninfo  0.8.1

You probably shouldn't use this just use : https://hardwaretester.com/gamepad
