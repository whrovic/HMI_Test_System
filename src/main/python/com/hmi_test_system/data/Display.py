class Display:
    def __init__(self, name, pos_init_x, pos_init_y, dim_x, dim_y):
        self.name = name
        self.pos_init_x = pos_init_x
        self.pos_init_y = pos_init_y
        self.dim_x = dim_x
        self.dim_y = dim_y
    
    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def new_pos(self, pos_init_x, pos_init_y, dim_x, dim_y):
        self.posInc_x = pos_init_x
        self.posInc_y = pos_init_y
        self.dim_x = dim_x
        self.dim_y = dim_y