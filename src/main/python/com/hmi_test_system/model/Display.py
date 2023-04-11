import PosCenter

class Display(PosCenter):
    def __init__(self, name, x, y, dim_x, dim_y):
        super().__init__(x, y)
        self.name = name
        self.dim_x = dim_x
        self.dim_y = dim_y
    
    def setName(self, newName):
        self.name = newName
    
    def getName(self):
        return self.name