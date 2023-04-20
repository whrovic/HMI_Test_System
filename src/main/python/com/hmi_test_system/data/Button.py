from .Position import Position

class Button(Position):
    def __init__(self, name: str, x: int, y: int):
        super().__init__(x, y)
        self.name = name
    
    def set_name(self, name: str):
        self.name = name
    
    def get_name(self):
        return self.name

    
  