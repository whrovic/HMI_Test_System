from Button import Button

class ButtonTest:
    def __init__(self, button: Button):
        self.button = button
        self.pressed_display = False
        self.pressed_serial_port = False
        
    def set_button(self, button):
        self.button = button

    #valor detetado pelo CV ao premir o botão
    def press_test_display(self, pressCV):
        self.pressed_display = pressCV
        
    def test_button_display(self):
        return self.pressed_display
    
    #valor detetado pelo Serial Port ao premir o botão
    def press_test_SP(self, pressSP):
        self.pressed_serial_port = pressSP
        
    def test_button_SP(self):
        return self.pressed_serial_port
