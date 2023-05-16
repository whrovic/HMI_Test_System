from .position import Position

'''
'!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGH\n' \
'IJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnop\n' \
'qrstuvwxyz{|}~!"#$%&\'()*+,-./0123456789:\n' \
';<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`ab\n' \
'cdefghijklmnopqrstuvwxyz{]}~!"#$%&\'()*+,\n' \
'-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRST\n' \
'UVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|\n' \
'}~!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEF\n' \
'GHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmn\n' \
'opqrstuvwxyz{|}~!"#$%&\'()*+,-./012345678\n' \
'9:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^-`\n' \
'abcdefghijklmnopqrstuvwxyz{|}~!"#$%&\'()*\n' \
'+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQR\n' \
'STUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz\n' \
'{|}~!"#S%&\'()*+,-./0123456789:;<=>?@ABCD\n' \
'EFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijkl\n'
'''

class Display(Position):
    def __init__(self, name: str, pos_init_x: int, pos_init_y: int, dim_x: int, dim_y: int, str = None):
        super().__init__(pos_init_x, pos_init_y)
        self._name = name
        self._dim_x = dim_x
        self._dim_y = dim_y
        self._color_vector = []
        self.blacklight_test: bool
        self.characters_test: bool

    
    def set_name(self, name: str):
        self._name = name
    
    def get_name(self):
        return self._name
    
    def get_dim_x(self):
        return self._dim_x
    
    def get_dim_y(self):
        return self._dim_y
    
    def new_pos(self, pos_init_x: int, pos_init_y: int, dim_x: int, dim_y: int):
        super().set_pos(pos_init_x, pos_init_y)
        self._dim_x = dim_x
        self._dim_y = dim_y

    def set_color_vector(self, vector):
        self._color_vector = vector

    def get_color_vector(self):
        return self._color_vector
    
    def set_char(self, str):
        self._characters_str = str

    def get_char(self):
        return self._characters_str
    

    