
class PosCenter:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def setPos(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    
    def getPos(self):
        return {self.x, self.y}
        