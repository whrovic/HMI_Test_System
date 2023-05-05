from .position import Position

class Button(Position):
    def __init__(self, name: str, x: int, y: int):
        super().__init__(x, y)
        self._name = name
        self.pressed_display = False
        self.pressed_serial_port = False
    
    def set_name(self, name: str):
        self._name = name
    
    def get_name(self):
        return self._name

 
    #---------------------test---------------------#
    
    #valor detetado pelo CV ao premir o botão
    def test_press_display(self, result):
        self.pressed_display = result
        
    def resul_press_display(self):
        return self.pressed_display
    
    #valor detetado pelo Serial Port ao premir o botão
    def test_press_serial_port(self, result):
        self.pressed_serial_port = result
        
    def result_press_serial_port(self):
        return self.pressed_serial_port