class Dimension:

    def __init__(self, length: int, width: int):
        self._length = length
        self._width = width

    def set_length(self, length: int):
        self._length = length
        
    def get_length(self):
        return  self._length
    
    def set_width(self, width: int):
        self._width = width
        
    def get_width(self):
        return  self._width