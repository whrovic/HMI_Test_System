import PosCenter

class Display:
    def __init__(self, name, posInc_x, posInc_y, dim_x, dim_y):
        self.name = name
        self.posInc_x = posInc_x
        self.posInc_y = posInc_y
        self.dim_x = dim_x
        self.dim_y = dim_y
    
    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name
    
    def newPos(self, posInc_x, posInc_y, dim_x, dim_y):
        self.posInc_x = posInc_x
        self.posInc_y = posInc_y
        self.dim_x = dim_x
        self.dim_y = dim_y