from .Led import Led
from .Button import Button
from .Display import Display

class Model:
    
    def __init__(self, name, n_leds, n_buttons, display: Display, version):
        self.name = name
        self.n_leds = n_leds
        self.n_buttons = n_buttons
        self.display = display
        self.version = version
        self.leds = []
        self.buttons = []
    
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name


    #vetor dos leds 
    def set_led(self, led: Led):
        if(len(self.leds) < self.n_leds):
            self.leds.append(led)
        else:
            print("ERROR")
    
    def delete_leds(self):
        self.leds = []


    #vetor dos botoes
    def set_button(self, button: Button):
        if(len(self.buttons) < self.n_buttons):
            self.buttons.append(button)
        else:
            print("ERROR")
    
    def delete_buttons(self):
        self.buttons = []
   
