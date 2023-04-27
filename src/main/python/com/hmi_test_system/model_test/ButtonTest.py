from data.model.Button import Button
import copy

class ButtonTest:
    def __init__(self, button: Button):
        self.button = copy.deepcopy(button)
        self.pressed_display = False
        self.pressed_serial_port = False
        
    def set_button(self, button):
        self.button = button

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
