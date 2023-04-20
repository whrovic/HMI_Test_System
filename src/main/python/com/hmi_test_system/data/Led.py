from .Position import Position


class Led(Position):
    def __init__(self, name: str, n_Colour, x: int, y: int):
        super().__init__(x, y)
        self.name = name
        self.n_Colour = n_Colour
        self.colours = []
    
    def set_name(self, name: str):
        self.name = name
    
    def get_name(self):
        return self.name
    
    #vetor das cores associadas ao led
    def new_colour(self, colour):
        if(len(self.colours) < self.n_Colour):
            self.colours.append(colour)
            return 0
        else: 
            return -1

    def delete_colour(self):
        self.colours = []

    def get_colour(self):
        return self.colours
    
    