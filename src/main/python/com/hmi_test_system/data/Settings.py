from .model.Model import Model
from .SequenceTest import SequenceTest
from ..model_test.ModelTest import ModelTest
from ..model_test.LedTest import LedTest
from ..model_test.ButtonTest import ButtonTest
from ..model_test.DisplayTest import DisplayTest
from .model.Display import Display
from typing import List
from .path import path

class Settings:
        
    def __init__(self):
        self.model: List[Model] = []
        self.model_test = ModelTest()
        self.sequence_test = SequenceTest
        self.path = path()

    #------------------------------------Model------------------------------------#
    def new_model(self, name: str, n_leds: int, n_buttons: int, display: Display, version):
        self.model.append(Model(name, n_leds, n_buttons, display, version))
    
    '''if not isinstance(name, str):
        #    raise TypeError("name must be a string.")
        if not isinstance(n_leds, int):
            raise TypeError("n_leds must be an integer.")
        if not isinstance(n_buttons, int):
            raise TypeError("n_buttons must be an integer.")
        if not isinstance(display, Display):
            raise TypeError("display must be an Display.")'''

    
    def call_model(self, name):
        for i in range(0, len(self.model)):
            model_name = self.model[int(i)].get_name()
            if(name == model_name):
                return self.model[i]
        
        #nao encontra o modelo
        return None

    
    def index_model(self, name):
        for i in range(len(self.model)):
            model_name = self.model[int(i)].get_name()
            if(name == model_name):
                return i
        
        #nao encontra o modelo
        return -1
    

    def index_led_model(self, name_model, led_name):
        index = self.index_model(name_model)

        for i in range(0, len(self.model[index]._leds)):
            if(self.model[index]._leds[i]._name == led_name):
                return i
        
        return None
    
    
    def index_button_model(self, name_model, button_name):
        index = self.index_model(name_model)

        for i in range(0, len(self.model[index]._buttons)):
            if(self.model[index]._buttons[i]._name == button_name):
                return i
        
        return None
    
    
    def delete_model(self, name):
        n_model = int(self.index_model(name))

        if(n_model == -1):
            return -1
        else:
            self.model.remove(n_model)
            return 0



    #------------------------------------Model test------------------------------------#
    def set_model_test(self, name):
        n_model = int(self.index_model(name))

        if(n_model == -1):
            print("ERROR - Modelo a testar não existe")
            return
        else:
            for i in range(0, self.model[n_model]._n_leds):
                self.model_test.leds_test.append(LedTest(self.model[n_model]._leds[i]))

            for i in range(0, self.model[n_model]._n_buttons):
                self.model_test.buttons_test.append(ButtonTest(self.model[n_model]._buttons[i]))  

            self.model_test.display_test = DisplayTest(self.model[n_model]._display) 

    def reset_model_test(self):
        self.model_test = ModelTest()

    def index_led(self, led_name):
        for i in range(0, len(self.model_test.leds_test)):
            name = self.model_test.leds_test[i].led.get_name()
            if(name == led_name):
                return i
        
        return None

    def index_button(self, button_name):

        for i in range(0, len(self.model_test.buttons_test)):
            name = self.model_test.buttons_test[i].button.get_name()
            if(name == button_name):
                return i
        
        return None
