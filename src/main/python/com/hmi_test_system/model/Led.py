import PosCenter


class Led(PosCenter):
    def __init__(self, name, nColour, x, y):
        super().__init__(x, y)
        self.name = name
        self.nColour = nColour
        self.colours = []
    
    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name
    
    #vetor das cores associadas ao led
    def newColour(self, colour):
        if(len(self.colours) < self.nColour):
            self.colours.append[colour]
        else: 
            print("ERROR")

    def deleteColour(self):
        self.colours = []

    def getColour(self):
        return self.colours
    
    