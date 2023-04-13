from Led import Led


class LedTest:
    def __init__(self, led: Led):
        self.led = led
        self.colours_cv = []
    
    def set_led(self, led):
        self.led = led

    #vetor de cores detetas por cv
    def colour_test(self, colour):
        self.colours_cv.append(colour)

    def getColourResult(self):
        return self.colours_cv
    
    def testLed(self):
        if(self.colours_cv == self.led.colours):
            return 1
        else:
            return 0


