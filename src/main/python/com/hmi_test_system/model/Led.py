import PosCenter

class Led(PosCenter):
    def __init__(self, name, colourTest, x, y):
        super().__init__(x, y)
        self.name = name
        self.colourTest = colourTest
    
    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name
    
    def setColour(self, colour):
        self.colourTest = colour

    def getColour(self):
        return self.colourTest
    
