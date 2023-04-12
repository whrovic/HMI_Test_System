class ButtonTest:
    def __init__(self, button):
        self.button = button
        self.pressedDisplay = bool
        self.pressedSerialPort = bool
        
    def setButton(self, button):
        self.button = button

    #valor detetado pelo CV ao premir o botão
    def pressTest(self, pressCV):
        self.pressedDisplay = pressCV

    def getPressedResult(self):
        return self.pressedDisplay
        
    def test(self):
        if self.pressedDisplay == 1:
            return 1
        else: 
            return 0
