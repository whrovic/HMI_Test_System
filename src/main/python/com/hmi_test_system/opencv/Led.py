import Position

class Led(Position):
    def __init__(self, x, y, number):
        super().__init__(x, y)
        self.number = number