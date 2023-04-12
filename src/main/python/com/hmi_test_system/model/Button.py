from PosCenter import PosCenter

class Button(PosCenter):
    def __init__(self, name, x, y):
        super().__init__(x, y)
        self.name = name
    
    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name

    
  