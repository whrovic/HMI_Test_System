import PosCenter

class Led(PosCenter):
    #name = "test"
    def __init__(self, name, colourTest):
        self.name = name
        self.colourTest = colourTest
    
    def setName(newName):
        Led.name = newName
    
    def getName():
        return Led.name
    
    def setColour(newColour):
        Led.colourTest = newColour
    
