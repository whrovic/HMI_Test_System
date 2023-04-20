from .Position import Position

class Display(Position):
    def __init__(self, name: str, pos_init_x: int, pos_init_y: int, dim_x: int, dim_y: int):
        super().__init__(pos_init_x, pos_init_y)
        self.name = name
        self.dim_x = dim_x
        self.dim_y = dim_y
    
    def set_name(self, name: str):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def new_pos(self, pos_init_x: int, pos_init_y: int, dim_x: int, dim_y: int):
        super().set_pos(pos_init_x, pos_init_y)
        self.dim_x = dim_x
        self.dim_y = dim_y