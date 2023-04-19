from .Model import Model
from .SequenceTest import SequenceTest
from model_test.ModelTest import ModelTest
from model_test.LedTest import LedTest
from model_test.ButtonTest import ButtonTest
from model_test.DisplayTest import DisplayTest
from .Display import Display
from typing import List

class Settings:
        
    def __init__(self):
        self.model:List[Model] = []
        self.model_test = ModelTest()
        self.sequence_test = SequenceTest


    #------------------------------------Model------------------------------------#
    def new_model(self, name, n_leds, n_buttons, display: Display, version):
        self.model.append(Model(name, n_leds, n_buttons, display, version))

    
    def call_model(self, name):
        for i in range(0, len(self.model)):
            if(name == self.model[int(i)].name):
                return self.model[i]
        
        #nao encontra o modelo
        return None

    
    def index_model(self, name):
        for i in range(len(self.model)):
            if(name == self.model[int(i)].name):
                return i
        
        #nao encontra o modelo
        return -1
    
    
    def delete_model(self, name):
        n_model = int(self.index_model(name))

        if(n_model == -1):
            print("ERROR - Modelo a eliminar não existe")
        else:
            self.model.remove(n_model)



    #------------------------------------Model test------------------------------------#
    def set_model_test(self, name):
        n_model = int(self.index_model(name))

        if(n_model == -1):
            print("ERROR - Modelo a testar não existe")
            return
        else:
            for i in range(0, self.model[n_model].n_leds):
                self.model_test.leds_test.append(LedTest(self.model[n_model].leds[i]))

            for i in range(0, self.model[n_model].n_buttons):
                self.model_test.buttons_test.append(ButtonTest(self.model[n_model].buttons[i]))  

            self.model_test.display_test = DisplayTest(self.model[n_model].display) 

    def reset_model_test(self):
        self.model_test = ModelTest()


    def index_led(self, led_name):
        for i in range(0, len(self.model_test.leds_test)):
            if(self.model_test.leds_test[i] == led_name):
                return i
        
        return None


    def index_button(self, button_name):
        for i in range(0, len(self.model_test.buttons_test)):
            if(self.model_test.buttons_test[i] == button_name):
                return i
        
        return None
