from .Led import Led
from .Button import Button
from .Display import Display

class Model:
    
    def __init__(self, name: str, n_leds: int, n_buttons: int, display: Display, version):
        self.name = name
        self.n_leds = n_leds
        self.n_buttons = n_buttons
        self.display = display
        self.version = version
        self.leds: list[Led] = []
        self.buttons: list[Button] = []
    
    def get_name(self):
        return self.name
    
    def set_name(self, name: int):
        self.name = name

    #vetor dos leds 
    def set_led(self, led: Led):
        if(len(self.leds) < self.n_leds):
            self.leds.append(led)
            return 0
        else:
            return -1
    
    def delete_leds(self):
        self.leds = []

    #vetor dos botoes
    def set_button(self, button: Button):
        if(len(self.buttons) < self.n_buttons):
            self.buttons.append(button)
            return 0
        else:
            return -1
    
    def delete_buttons(self):
        self.buttons = []
        
    def set_all_leds_buttons(self, list_leds: list[Led], list_buttons: list[Button]):
        if len(self.list_leds) < self.n_leds and len(self.list_buttons) < self.n_buttons:
            self.leds.extend(list_leds)
            self.buttons.extend(list_buttons)
            return 0
        else:
            return -1
    
    def set_n_leds_buttons(self, n_leds: int, n_buttons: int):
        if len(self.leds) < n_leds and len(self.buttons) < n_buttons:
            self.n_leds = n_leds
            self.n_buttons = n_buttons
            return 0
        else:
            return -1
