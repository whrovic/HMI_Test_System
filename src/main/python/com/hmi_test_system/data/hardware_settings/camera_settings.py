from hardware_settings.dimension import Dimension
from hardware_settings.parameter import Parameter

class CameraSettings:

    def __init__(self, name: str, structure: Dimension, parameters: Parameter):
        self._name = name
        self._structure = structure
        self._parameters = parameters

    def set_name(self, name: str):
        self._name = name
        
    def get_name(self):
        return self._name
    
    def get_structure(self):
        return self._structure.get_length() , self._structure.get_width()