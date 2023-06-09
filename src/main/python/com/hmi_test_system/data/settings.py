from .hardware_settings.test_settings import TestSettings
from .model.boot_loader_info import BootLoaderInfo
from .model.display import Display
from .model.info import Info
from .model.model import Model
from .path import Path


class Settings:

    model: list[Model] = []
    path = Path
    test_settings = TestSettings()
    
    @staticmethod
    def new_model(name: str, n_leds: int, n_buttons: int, display: Display, info: Info, boot_loader_info: BootLoaderInfo):
        Settings.model.append(Model(name, n_leds, n_buttons, display, info, boot_loader_info))
    
    @staticmethod
    def add_model(model: Model):
        if model not in Settings.model:
            Settings.model.append(model)

    @staticmethod
    def get_model(name):
        for model in Settings.model:
            if model.get_name() == name:
                return model
        # Model not found
        return None
    
    @staticmethod
    def index_model(name):
        for i in range(len(Settings.model)):
            model_name = Settings.model[int(i)].get_name()
            if(name == model_name):
                return i
        # Model not found
        return -1
    
    @staticmethod
    def delete_model(name):
        n_model = int(Settings.index_model(name))

        if(n_model == -1):
            return -1
        else:
            Settings.model.remove(n_model)
            return 0

    @staticmethod
    def index_led(name_model, led_name):
        index = Settings.index_model(name_model)

        for i in range(0, len(Settings.model[index]._leds)):
            if(Settings.model[index]._leds[i]._name == led_name):
                return i
        return None
    
    @staticmethod
    def index_button(name_model, button_name):
        index = Settings.index_model(name_model)

        for i in range(0, len(Settings.model[index]._buttons)):
            if(Settings.model[index]._buttons[i]._name == button_name):
                return i
        return None
    