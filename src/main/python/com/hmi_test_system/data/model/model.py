from .led import Led
from .button import Button
from .display import Display
from .info import Info
from .boot_loader_info import BootLoaderInfo

class Model:
    
    def __init__(self, name: str, n_leds: int, n_buttons: int, display: Display, info: Info, boot_loader_info: BootLoaderInfo):
        self._name = name
        self._n_leds = n_leds
        self._leds: list[Led] = []
        self._n_buttons = n_buttons
        self._buttons: list[Button] = []
        self._display = display
        self._info = info
        self._boot_loader_info = boot_loader_info
    
    def set_name(self, name: str):
        self._name = name
        
    def get_name(self):
        return self._name
  
    #To change the parameters of the number of leds and buttons
    def set_n_leds_buttons(self, n_leds: int, n_buttons: int):
        if len(self._leds) < n_leds and len(self._buttons) < n_buttons:
            self._n_leds = n_leds
            self._n_buttons = n_buttons
            return 0
        else:
            return -1
 
    #Include a list of led's and button's
    #To include just one of them pass to the function a vector with zero elements
    def set_all_leds_buttons(self, list_leds: list[Led], list_buttons: list[Button]):
        if len(list_leds) < self._n_leds and len(list_buttons) < self._n_buttons:
            self._leds.extend(list_leds)
            self._buttons.extend(list_buttons)
            return 0
        else:
            return -1
     
    def get_n_leds(self):
        return self._n_leds
    
    #Include led to led
    def set_led(self, led: Led):
        if(len(self._leds) < self._n_leds):
            self._leds.append(led)
            return 0
        else:
            return -1
    
    def get_leds(self):
        return self._leds
    
    def get_led(self, name: str):
        for i in range(len(self._leds)):
            led_name = self._leds[i].get_name()
            if(led_name == name):
                return self._leds[i]
    
    #Delete all the list of leds
    def delete_leds(self):
        self._leds = []

    def get_n_buttons(self):
        return self._n_buttons
    
    #Include button to button
    def set_button(self, button: Button):
        if(len(self._buttons) < self._n_buttons):
            self._buttons.append(button)
            return 0
        else:
            return -1
        
    def get_buttons(self):
        return self._buttons
    
    def get_button(self, name):
        for i in range(len(self._buttons)):
            button_name = self._buttons[int(i)].get_name()
            if(button_name == name):
                return self._buttons[int(i)]
            
        return None
    
    def delete_buttons(self):
        self._buttons = []
    
    def set_display(self, display: Display):
        self._display=display
     
    def get_display(self):
        return self._display
       
    def set_info(self, info: Info):
        self._info = info
        
    def get_info(self):
        return self._info
    
    def set_boot_loader_info(self, boot_loader_info: BootLoaderInfo):
        self._boot_loader_info = boot_loader_info
        
    def get_boot_loader_info(self):
        return self._boot_loader_info