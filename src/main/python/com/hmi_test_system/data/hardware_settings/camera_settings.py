class CameraSettings:

    def __init__(self, name: str):
        self._name = name

    def set_name(self, name: str):
        self._name = name
        
    def get_name(self):
        return self._name