from .serial_port_settings import SerialPortSettings
from .camera_settings import CameraSettings
from .dimension import Dimension
from .parameter import Parameter


class TestSettings:

    _cam: list[CameraSettings] = []
    _sp: list[SerialPortSettings] = []
    _cam_display = None
    _cam_leds = None
    _sp_main = None
    _sp_usb = None


    def get_cam_display():
        return TestSettings._cam_display

    def set_cam_display(name: str):
        cam_index = TestSettings.get_index_cam(name)
        if cam_index == -1:
            # TODO: Error Code
            return -1
        else:
            TestSettings._cam_display = TestSettings._cam[cam_index]

    def get_cam_leds():
        return TestSettings._cam_leds

    def set_cam_leds(name: str):
        cam_index = TestSettings.get_index_cam(name)
        if cam_index == -1:
            # TODO: Error Code
            return -1
        else:
            TestSettings._cam_leds = TestSettings._cam[cam_index]

    def get_sp_main():
        return TestSettings._sp_main
    
    def set_sp_main(name: str):
        sp_index = TestSettings.get_index_sp(name)
        if sp_index == -1:
            # TODO: Error code
            return -1
        TestSettings._sp_main = TestSettings._sp[sp_index]

    def add_new_sp_settings(name: str, baudrate: int, port: str):
        TestSettings._sp.append(SerialPortSettings(name, baudrate, port))

    def get_index_sp(name: str):
        for i in range(len(TestSettings._sp)):
            sp_name = TestSettings._sp[i].get_name()
            if(sp_name == name):
                return TestSettings._sp[i]
        return -1
    
    def delete_sp_settings(name: str):
        sp_index = TestSettings.get_index_sp(name)
        TestSettings._sp.pop(sp_index)

    def add_new_cam_settings(name: str, structure: Dimension, parameters: Parameter):
        TestSettings._cam.append(CameraSettings(name, structure, parameters))

    def get_index_cam(name: str):
        for i in range(len(TestSettings._cam)):
            cam_name = TestSettings._cam[i].get_name()
            if(cam_name == name):
                return TestSettings._cam[i]
        return -1
    
    def delete_cam_settings(name: str):
        cam_index = TestSettings.get_index_cam(name)
        TestSettings._cam.pop(cam_index)