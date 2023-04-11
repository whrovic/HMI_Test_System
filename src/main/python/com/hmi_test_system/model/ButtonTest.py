import Button

class ButtonTest():
    def __init__(self, button, pressedDisplay, pressedSerialPort):
        self.button = button
        self.pressedDisplay = pressedDisplay
        self.pressedSerialPort = pressedSerialPort 
        
    def setButton(self):
        self.button = Button
        
    def getName(self):
        return self.button.__name__


    def testPressedPass():
        pass

    def testPressedResult():
        return ButtonTest.pressedDisplay
