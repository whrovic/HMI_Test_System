from PosCenter import PosCenter


class Led(PosCenter):
    def __init__(self, name, n_Colour, x, y):
        super().__init__(x, y)
        self.name = name
        self.n_Colour = n_Colour
        self.colours = []
    
    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    #vetor das cores associadas ao led
    def new_colour(self, colour):
        if(len(self.colours) < self.nColour):
            self.colours.append[colour]
        else: 
            print("ERROR")

    def delete_colour(self):
        self.colours = []

    def get_colour(self):
        return self.colours
    
    