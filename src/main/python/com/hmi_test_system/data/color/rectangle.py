from data.model.position import Position

class Rectangle:
    def __init__(self, x, y, w, h):
        self.coordinates = Position(x, y)
        self.dimentions = [w, h]

    def get_coordinates(self):
        return [self.coordinates.get_pos_x(), self.coordinates.get_pos_y()]
    
    def get_dimentions(self):
        return self.dimentions
    
    def set_coordinates(self, x, y):
        self.coordinates.set_pos(x, y)

    def set_dimentions(self, w, h):
        self.dimentions = [w, h]