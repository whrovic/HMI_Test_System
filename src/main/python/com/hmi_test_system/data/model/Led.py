from .Position import Position
from data.color.color import Color


class Led(Position):
    def __init__(self, name: str, n_Colour, x: int, y: int):
        super().__init__(x, y)
        self._name = name
        self._n_Colour = n_Colour
        self._colours: list[Color] = []
    
    def set_name(self, name: str):
        self._name = name
    
    def get_name(self):
        return self._name
    
    def get_n_Colour(self):
        return self._n_Colour
    
    #vetor das cores associadas ao led
    def new_colour(self, colour: Color):
        if(len(self._colours) < self._n_Colour):
            self._colours.append(colour)
            return 0
        else: 
            return -1

    def delete_colour(self):
        self._colours = []

    def get_colour(self):
        return self._colours
    
    