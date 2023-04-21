from .Led import Led
from .Button import Button
from .Display import Display

class Model:
    
    def __init__(self, name: str, n_leds: int, n_buttons: int, display: Display, version):
        self._name = name
        self._n_leds = n_leds
        self._n_buttons = n_buttons
        self._display = display
        self._version = version
        self._leds: list[Led] = []
        self._buttons: list[Button] = []
    
    def get_name(self):
        return self._name
    
    def set_name(self, name: int):
        self._name = name

    def get_n_leds(self):
        return self._n_leds
    
    def get_n_buttons(self):
        return self._n_buttons
    
    def get_leds(self):
        return self._leds
    
    def get_buttons(self):
        return self._buttons
    
    def get_display(self):
        return self._display
    
    def get_version(self):
        return self._version
    
    #vetor dos leds 
    def set_led(self, led: Led):
        if(len(self._leds) < self._n_leds):
            self._leds.append(led)
            return 0
        else:
            return -1
    
    def delete_leds(self):
        self._leds = []

    #vetor dos botoes
    def set_button(self, button: Button):
        if(len(self._buttons) < self._n_buttons):
            self._buttons.append(button)
            return 0
        else:
            return -1
    
    def delete_buttons(self):
        self._buttons = []
        
    def set_all_leds_buttons(self, list_leds: list[Led], list_buttons: list[Button]):
        if len(list_leds) < self._n_leds and len(list_buttons) < self._n_buttons:
            self._leds.extend(list_leds)
            self._buttons.extend(list_buttons)
            return 0
        else:
            return -1
    
    def set_n_leds_buttons(self, n_leds: int, n_buttons: int):
        if len(self._leds) < n_leds and len(self._buttons) < n_buttons:
            self._n_leds = n_leds
            self._n_buttons = n_buttons
            return 0
        else:
            return -1
