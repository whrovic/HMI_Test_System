from .dimension import Dimension
from .parameter import Parameter

class CameraSettings:

    def __init__(self, name: str, structure: Dimension, parameters: Parameter):
        self._name = name
        self._structure = structure
        self._parameters: dict[str, Parameter] = {}

    def get_name(self):
        return self._name

    def set_name(self, name: str):
        self._name = name
    
    def get_parameters(self, position: str):
        return self._parameters.get(position, None)
    
    def set_parameters(self, position: str, parameters: Parameter):
        self._parameters[position] = parameters

    def get_structure(self):
        return self._structure.get_length() , self._structure.get_width()