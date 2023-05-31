from .model.model import Model
from .model.display import Display
from .path import Path
from test.sequence_test import SequenceTest
from .hardware_settings.test_settings import TestSettings

class Settings:

    def __init__(self):
        self.model: list[Model] = []
        self.path = Path()
        self.test = TestSettings()
        #self.cam1 = CameraSettings()
        #self.cam2 = CameraSettings()


    #------------------------------------Model------------------------------------#
    def new_model(self, name: str, n_leds: int, n_buttons: int, display: Display, info):
        self.model.append(Model(name, n_leds, n_buttons, display, info))
   
    
    def call_model(self, name):
        for i in range(0, len(self.model)):
            model_name = self.model[int(i)].get_name()
            if(name == model_name):
                return self.model[i]
        
        # Model not found
        return None

    
    def index_model(self, name):
        for i in range(len(self.model)):
            model_name = self.model[int(i)].get_name()
            if(name == model_name):
                return i
        
        # Model not found
        return -1
    
    
    def delete_model(self, name):
        n_model = int(self.index_model(name))

        if(n_model == -1):
            return -1
        else:
            self.model.remove(n_model)
            return 0


    def index_led(self, name_model, led_name):
        index = self.index_model(name_model)

        for i in range(0, len(self.model[index]._leds)):
            if(self.model[index]._leds[i]._name == led_name):
                return i
        
        return None
    
    
    def index_button(self, name_model, button_name):
        index = self.index_model(name_model)

        for i in range(0, len(self.model[index]._buttons)):
            if(self.model[index]._buttons[i]._name == button_name):
                return i
        
        return None
        


