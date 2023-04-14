from .PosCenter import PosCenter

class Button(PosCenter):
    def __init__(self, name, x, y):
        super().__init__(x, y)
        self.name = name
    
    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

    
  