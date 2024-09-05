from graphics import *
from screeninfo import get_monitors

monitor = get_monitors()[0]

WIN_HEIGHT = monitor.height*0.8
WIN_WIDTH = monitor.width*0.9

win = GraphWin('ControllerTester', WIN_WIDTH, WIN_HEIGHT)  

def GetJoystickCenter(x , y):
    joystickCircle = Circle(Point(x,y), 36)        
    return joystickCircle.getCenter()

def GetJoystickLabel(x , y):
    label = Text(Point(x, y), "[ 0 , 0 ]")
    label.draw(win)
    return label

def GetTriggerLabels(x, y):
    txt = Text(Point(x + 30, y - 30), "0/255")
    txt.draw(win)
    return txt

class ControllerComponent():
    def __init__(self, name, drawing):
        self.Name = name
        self.Drawing = drawing
        self.Value = 0

class ControllerComponentLabel():
    def __init__(self, name, label):
        self.Name = name
        self.Label = label

class Controller:
    
    Components = []

    leftJoyStickCenterPos = GetJoystickCenter(WIN_WIDTH * 0.4, WIN_HEIGHT * 0.6)
    rightJoyStickCenterPos = GetJoystickCenter(WIN_WIDTH * 0.55, WIN_HEIGHT * 0.6)

    LeftJoystickLabel = GetJoystickLabel(WIN_WIDTH * 0.4, (WIN_HEIGHT * 0.6) + 50)
    RightJoystickLabel = GetJoystickLabel(WIN_WIDTH * 0.55, (WIN_HEIGHT * 0.6) + 50)

    L2Label = GetTriggerLabels(WIN_WIDTH * 0.325, WIN_HEIGHT * 0.15)
    R2Label = GetTriggerLabels(WIN_WIDTH * 0.575, WIN_HEIGHT * 0.15)

    def CreateController():
        leftJoystick = Controller.GetJoystick(WIN_WIDTH * 0.4, WIN_HEIGHT * 0.6)       
        leftJoystick.draw(win)

        centerOfCircle = leftJoystick.getCenter()
        LeftStickCenterPoint = Circle(centerOfCircle, 2)
        LeftStickCenterPoint.setFill("red")
        LeftStickCenterPoint.draw(win)
    
        rightJoystick = Controller.GetJoystick(WIN_WIDTH * 0.55, WIN_HEIGHT * 0.6)
        rightJoystick.draw(win)

        centerOfCircle = rightJoystick.getCenter()

        RightStickCenterPoint = Circle(centerOfCircle, 2)
        RightStickCenterPoint.setFill("red")

        RightStickCenterPoint.draw(win)
    
        touchPad = Controller.GetTouchPad(WIN_WIDTH * 0.425, WIN_HEIGHT * 0.45)
        touchPad.draw(win)
    
        traingleButton = Controller.GetShapeButtons(WIN_WIDTH * 0.59, WIN_HEIGHT * 0.46)
        traingleButton.draw(win)
    
        squareButton = Controller.GetShapeButtons(WIN_WIDTH * 0.575, WIN_HEIGHT * 0.49)
        squareButton.draw(win)
    
        crossButton = Controller.GetShapeButtons(WIN_WIDTH * 0.59, WIN_HEIGHT * 0.52)
        crossButton.draw(win)
    
        circleButton = Controller.GetShapeButtons(WIN_WIDTH * 0.605, WIN_HEIGHT * 0.49)
        circleButton.draw(win)
    
        rightButton = Controller.GetRightButton()
        rightButton.draw(win)
    
        upButton = Controller.GetUpButton()
        upButton.draw(win)
    
        downButton = Controller.GetDownButton()
        downButton.draw(win)
    
        leftButton = Controller.GetLeftButton()
        leftButton.draw(win)
    
        optionsButton = Controller.GetOptionsOrShareButton(WIN_WIDTH * 0.54, WIN_HEIGHT * 0.35)
        optionsButton.draw(win)
    
        shareButton = Controller.GetOptionsOrShareButton(WIN_WIDTH * 0.39, WIN_HEIGHT * 0.35)
        shareButton.draw(win)
    
        R1Button = Controller.GetR1OrL1Buttons(WIN_WIDTH * 0.575, WIN_HEIGHT * 0.25)
        R1Button.draw(win)
    
        L1Button = Controller.GetR1OrL1Buttons(WIN_WIDTH * 0.325, WIN_HEIGHT * 0.25)
        L1Button.draw(win)
    
        R2Button = Controller.GetR2OrL2Buttons(WIN_WIDTH * 0.575, WIN_HEIGHT * 0.15)
        R2Button.draw(win)
    
        L2Button = Controller.GetR2OrL2Buttons(WIN_WIDTH * 0.325, WIN_HEIGHT * 0.15)
        L2Button.draw(win)

        controller = Controller

        controller.Components = [
            ControllerComponent("L1", L1Button),
            ControllerComponent("L2", L2Button),
            ControllerComponent("R1", R1Button),
            ControllerComponent("R2", R2Button),
            ControllerComponent("Circle", circleButton),
            ControllerComponent("Triangle", traingleButton),
            ControllerComponent("Square", squareButton),
            ControllerComponent("Cross", crossButton),
            ControllerComponent("Up",upButton),
            ControllerComponent("Down",downButton),  
            ControllerComponent("Left",leftButton),
            ControllerComponent("Right",rightButton),
            ControllerComponent("ShareButton", shareButton),
            ControllerComponent("OptionsButton", optionsButton),
            ControllerComponent("TouchPad", touchPad),
            ControllerComponent("LStickPos", LeftStickCenterPoint),
            ControllerComponent("RStickPos", RightStickCenterPoint),
        ]

        return controller

    def GetJoystick(x , y):

        joystickCircle = Circle(Point(x,y), 36)            #point is location on window
        joystickCircle.setFill("white")
        joystickCircle.setOutline("black")
        joystickCircle.setWidth(5)

        return joystickCircle

    def GetTouchPad(x , y):

        touchpadRectangle = Rectangle(Point(x,y), Point(x + WIN_WIDTH*0.1, y + WIN_HEIGHT*0.1))
        touchpadRectangle.setOutline("black")
        touchpadRectangle.setWidth(5)

        return touchpadRectangle

    def GetShapeButtons(x, y):

        triangle = Circle(Point(x, y), radius = 10)
        triangle.setOutline("black")
        triangle.setWidth(5)

        return triangle

    def GetRightButton():

        points = [
            Point(WIN_WIDTH * 0.35, WIN_HEIGHT * 0.49),                             #triangle tip
            Point(WIN_WIDTH * 0.355, WIN_HEIGHT * 0.48),
            Point(WIN_WIDTH * 0.3675, WIN_HEIGHT * 0.48),
            Point(WIN_WIDTH * 0.3675, WIN_HEIGHT * 0.5),
            Point(WIN_WIDTH * 0.355, WIN_HEIGHT * 0.5)
        ]

        button = Polygon(points)
        button.setOutline("black")
        button.setWidth(4)
        return button

    def GetUpButton():

        points = [
            Point(WIN_WIDTH *  0.345, WIN_HEIGHT * 0.49),                             #triangle tip
            Point(WIN_WIDTH *  0.34, WIN_HEIGHT * 0.48),
            Point(WIN_WIDTH *  0.34, WIN_HEIGHT * 0.46),
            Point(WIN_WIDTH *  0.35, WIN_HEIGHT * 0.46),
            Point(WIN_WIDTH *  0.35, WIN_HEIGHT * 0.48)
        ]
        button = Polygon(points)
        button.setOutline("black")
        button.setWidth(4)
        return button

    def GetDownButton():

        points = [
            Point(WIN_WIDTH *  0.345, WIN_HEIGHT * 0.5),                             #triangle tip
            Point(WIN_WIDTH *  0.35, WIN_HEIGHT * 0.51),
            Point(WIN_WIDTH *  0.35, WIN_HEIGHT * 0.535),
            Point(WIN_WIDTH *  0.34, WIN_HEIGHT * 0.535),
            Point(WIN_WIDTH *  0.34, WIN_HEIGHT * 0.51)
        ]
        button = Polygon(points)
        button.setOutline("black")
        button.setWidth(4)
        return button

    def GetLeftButton():

        points = [
            Point(WIN_WIDTH *  0.34, WIN_HEIGHT * 0.49),                             #triangle tip
            Point(WIN_WIDTH *  0.335, WIN_HEIGHT * 0.48),
            Point(WIN_WIDTH *  0.325, WIN_HEIGHT * 0.48),
            Point(WIN_WIDTH *  0.325, WIN_HEIGHT * 0.5),
            Point(WIN_WIDTH *  0.335, WIN_HEIGHT * 0.5)
        ]
        button = Polygon(points)
        button.setOutline("black")
        button.setWidth(4)
        return button

    def GetOptionsOrShareButton(x,y):

        OptionButton = Rectangle(Point(x,y), Point(x + 20, y + 40))
        OptionButton.setOutline("black")
        OptionButton.setWidth(4)

        return OptionButton

    def GetR1OrL1Buttons(x, y):
        Button = Rectangle(Point(x,y), Point(x + 65, y+25))
        Button.setOutline("black")
        Button.setWidth(4)

        return Button

    def GetR2OrL2Buttons(x, y):

        Button = Rectangle(Point(x, y), Point(x + 65, y + 70))
        Button.setOutline("black")
        Button.setWidth(4)

        return Button
