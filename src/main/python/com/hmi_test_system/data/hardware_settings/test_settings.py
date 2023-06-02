from .serial_port_settings import SerialPortSettings
from .camera_settings import CameraSettings
from .dimension import Dimension
from .parameter import Parameter


class TestSettings:

    def __init__(self):
        self._cam: list[CameraSettings] = []
        self._sp: list[SerialPortSettings] = []

    def set_new_sp(self, name: str, baudrate: int, port: str):
        self._sp.append(SerialPortSettings(name, baudrate, port))

    def get_index_sp(self, name: str):
        for i in range(len(self._sp)):
            sp_name = self._sp[i].get_name()
            if(sp_name == name):
                return self._sp[i]
    
    def delete_sp(self, name: str):
        sp_index = self.get_index_sp(name)
        self._sp.pop(sp_index)



    def set_new_cam(self, name: str, structure: Dimension, parameters: Parameter):
        self._cam.append(CameraSettings(name, structure, parameters))

    def get_index_cam(self, name: str):
        for i in range(len(self._cam)):
            cam_name = self._cam[i].get_name()
            if(cam_name == name):
                return self._cam[i]
    
    def delete_cam(self, name: str):
        cam_index = self.get_index_cam(name)
        self._cam.pop(cam_index)
    
    