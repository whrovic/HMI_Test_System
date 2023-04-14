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


    def new_model(self, name, n_leds_control, n_leds_alarm, n_leds_buttons, n_buttons_model, n_special_buttons, display: Display, version):
        self.model.append(Model(name, n_leds_control, n_leds_alarm, n_leds_buttons, n_buttons_model, n_special_buttons, display, version))

    
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


    def set_model_test(self, name):
        n_model = int(self.index_model(name))

        if(n_model == -1):
            print("ERROR - Modelo a testar não existe")
            return
        else:
            for i in range(0, self.model[n_model].n_leds_control):
                self.model_test.leds_control_test.append(LedTest(self.model[n_model].leds_control[i]))

            for i in range(0, self.model[n_model].n_leds_alarm):
                self.model_test.leds_alarm_test.append(LedTest(self.model[n_model].leds_alarm[i]))

            for i in range(0, self.model[n_model].n_leds_buttons):
                self.model_test.leds_buttons_test.append(LedTest(self.model[n_model].leds_buttons[i]))

            for i in range(0, self.model[n_model].n_buttons_model):
                self.model_test.buttons_model_test.append(ButtonTest(self.model[n_model].buttons_model[i]))

            for i in range(0, self.model[n_model].n_special_buttons):
                self.model_test.special_buttons_test.append(ButtonTest(self.model[n_model].special_buttons[i]))   

            self.model_test.display_test= DisplayTest(self.model[n_model].display) 