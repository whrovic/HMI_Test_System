class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def set_pos(self, new_x: int, new_y: int):
        self.x = new_x
        self.y = new_y
    
    def get_pos(self):
        return {self.x, self.y}
        