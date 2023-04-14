
class PosCenter:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def set_pos(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    
    def get_pos(self):
        return {self.x, self.y}
        