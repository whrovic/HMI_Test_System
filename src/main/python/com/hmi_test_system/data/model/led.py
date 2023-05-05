from .position import Position
from data.color.color import Color

class Led(Position):
    def __init__(self, name: str, n_colour, x: int, y: int):
        super().__init__(x, y)
        self._name = name
        self._n_colour = n_colour
        self._colours: list[Color] = []
        self.colours_cv: list[Color] = []
    
    def set_name(self, name: str):
        self._name = name
    
    def get_name(self):
        return self._name
    
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

    def get_colours(self):
        return self._colours
    

    #---------------------test---------------------#
        
    # vetor de cores detetas por cv
    def test_colour(self, colour):
        self.colours_cv.append(colour)

    def get_colour_result(self):
        return self.colours_cv

    def result_test_Led(self):
        if self.colours_cv == self._colours:
            return 1
        else:
            return 0

    def clear_colour(self):
        self.colours_cv.clear()
    
    
