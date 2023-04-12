class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getPos(self):
        return {self.x, self.y}
    
    def setPos(self, x, y):
        self.x = x
        self.y = y

    