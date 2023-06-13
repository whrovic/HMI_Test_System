from .parameter import Parameter

class CameraSettings:

    def __init__(self, name: str, device_id = 0):
        self._name = name
        self._device_id = device_id
        self._parameters: dict[str, Parameter] = {}

    def get_name(self):
        return self._name

    def set_name(self, name: str):
        self._name = name
    
    def get_device_id(self):
        return self._device_id
    
    def set_device_id(self, device_id):
        self._device_id = device_id

    def get_parameters(self, position: str):
        parameters = self._parameters.get(position, None)
        if parameters is None:
            return None
        else:
            return parameters.get_parameters()
    
    def set_parameters(self, position: str, parameters: Parameter = Parameter()):
        self._parameters[position] = parameters
    