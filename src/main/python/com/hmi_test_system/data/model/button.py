from .position import Position


class Button(Position):
    
    def __init__(self, name: str, x: int, y: int):
        super().__init__(x, y)
        self._name = name
    
    def get_name(self):
        return self._name
    
    def set_name(self, name: str):
        self._name = name
    