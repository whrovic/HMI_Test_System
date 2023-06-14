from .position import Position
from data.color.color import Color

class Led(Position):
    
    def __init__(self, name: str, n_colour, x: int, y: int):
        super().__init__(x, y)
        self._name = name
        self._n_colour = n_colour
        self._colours: list[Color] = []
    
    def set_name(self, name: str):
        self._name = name
    
    def get_name(self):
        return self._name
    
    def set_n_Colour(self, n_colour: int):
        
        self.delete_colours()
        self._n_colour = n_colour
        return 0
    
    def get_n_Colour(self):
        return self._n_colour
    
    #vetor of colors assossiate to the led
    def new_colour(self, colour: Color):
        if(len(self._colours) < self._n_colour):
            self._colours.append(colour)
            return 0
        else: 
            return -1

    def delete_colours(self):
        self._colours = []
        self._n_colour = 0
        

    def get_colours(self):
        return self._colours
    