from .position import Position


class Display(Position):
    
    def __init__(self, name: str, pos_init_x: int, pos_init_y: int, dim_x: int, dim_y: int, chr_reference_path: str = None, pal_reference_path: str = None):
        super().__init__(pos_init_x, pos_init_y)
        self._name = name
        self._dim_x = dim_x
        self._dim_y = dim_y
        self._chr_reference_path = chr_reference_path
        self._pal_reference_path = pal_reference_path

    def get_name(self):
        return self._name
    
    def set_name(self, name: str):
        self._name = name
    
    def get_dim_x(self):
        return self._dim_x
    
    def get_dim_y(self):
        return self._dim_y
    
    def set_new_pos(self, pos_init_x: int, pos_init_y: int, dim_x: int, dim_y: int):
        super().set_pos(pos_init_x, pos_init_y)
        self._dim_x = dim_x
        self._dim_y = dim_y

    def get_chr_reference_path(self):
        return self._chr_reference_path
    
    def set_chr_reference_path(self, chr_reference_path):
        self._chr_reference_path = chr_reference_path

    def get_pal_reference_path(self):
        return self._pal_reference_path
    
    def set_pal_reference_path(self, pal_reference_path):
        self._pal_reference_path = pal_reference_path
    