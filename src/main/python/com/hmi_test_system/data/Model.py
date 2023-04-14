from Led import Led
from Button import Button
from Display import Display

class Model:
    
    def __init__(self, name, n_leds_control, n_leds_alarm, n_leds_buttons, n_buttons_model, n_special_buttons, display: Display, version):
        self.name = name
        self.n_leds_control = n_leds_control
        self.n_leds_alarm = n_leds_alarm
        self.n_leds_buttons = n_leds_buttons
        self.n_buttons_model = n_buttons_model
        self.n_special_buttons = n_special_buttons
        self.display = display
        self.version = version
        self.leds_control = []
        self.leds_alarm = []
        self.leds_buttons = []
        self.buttons_model = []
        self.special_buttons = []
    
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name


    #vetor dos leds de controlo 
    def set_led_control(self, led: Led):
        if(len(self.leds_control) < self.n_leds_control):
            self.leds_control.append(led)
        else:
            print("ERROR")
    
    def delete_leds_control(self):
        self.leds_control = []


    #vetor dos leds de alarme 
    def set_led_alarm(self, led: Led):
        if(len(self.leds_alarm) < self.n_leds_alarm):
            self.leds_alarm.append(led)
        else:
            print("ERROR")
    
    def delete_leds_alarm(self):
        self.leds_alarm = []


    #vetor dos leds dos botoes       
    def set_led_buttons(self, led: Led):
        if(len(self.leds_buttons) < self.n_leds_buttons):
            self.leds_buttons.append(led)
        else:
            print("ERROR")
    
    def delete_leds_button(self):
        self.leds_buttons = []


    #vetor dos botoes
    def set_button_model(self, button: Button):
        if(len(self.buttons_model) < self.n_buttons_model):
            self.buttons_model.append(button)
        else:
            print("ERROR")
    
    def delete_buttons_model(self):
        self.buttons_model = []

    
    #vetor dos botoes especiais
    def set_special_button(self, button: Button):
        if(len(self.special_buttons) < self.n_special_buttons):
            self.special_buttons.append(button)
        else:
            print("ERROR")
    
    def delete_special_buttons(self):
        self.special_buttons = []
   
