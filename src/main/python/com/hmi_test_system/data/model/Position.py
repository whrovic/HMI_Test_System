class Position:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y
    
    def set_pos(self, new_x: int, new_y: int):
        self._x = new_x
        self._y = new_y
    
    def get_pos(self):
        return {self._x, self._y}
    
    def get_pos_x(self):
        return self._x
    
    def get_pos_y(self):
        return self._y
        