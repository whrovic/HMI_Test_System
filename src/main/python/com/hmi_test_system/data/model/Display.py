from .Position import Position

class Display(Position):
    def __init__(self, name: str, pos_init_x: int, pos_init_y: int, dim_x: int, dim_y: int):
        super().__init__(pos_init_x, pos_init_y)
        self._name = name
        self._dim_x = dim_x
        self._dim_y = dim_y
        self._vector_test: list = []
    
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

    def get_char(self):
        test =  '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGH\n' \
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
        return test
    
    def get_n_test_vector(self):
        return len(self._vector_test)
    
    def get_test_pos(self, pos):
        if len(self._vector_test) > pos:
            return self._vector_test[pos]
        return None
    
    def get_test(self):
        return self._vector_test