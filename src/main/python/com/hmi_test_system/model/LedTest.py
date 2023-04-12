import Led


class LedTest:
    def __init__(self, led):
        self.led = led
        self.coloursCV = []
    
    def setLed(self, led):
        self.led = led

    #vetor de cores detetas por cv
    def colourTest(self, colour):
        self.coloursCV.append(colour)

    def getColourResult(self):
        return self.coloursCV
    
    def test(self):
        if(self.coloursCV == self.led.colours):
            return 1
        else:
            return 0


