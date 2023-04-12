from Button import Button

class ButtonTest:
    def __init__(self, button: Button):
        self.button = button
        self.pressedDisplay = False
        self.pressedSerialPort = False
        
    def setButton(self, button):
        self.button = button

    #valor detetado pelo CV ao premir o botão
    def pressTest_SP(self, pressCV):
        self.pressedDisplay = pressCV
        
    def testButton_SP(self):
        return self.pressedDisplay
    
    #valor detetado pelo Serial Port ao premir o botão
    def pressTest_SP(self, pressSP):
        self.pressedSerialPort = pressSP
        
    def testButton_SP(self):
        return self.pressedSerialPort
