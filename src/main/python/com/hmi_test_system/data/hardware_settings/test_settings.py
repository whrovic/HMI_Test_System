from .camera_settings import CameraSettings
from .parameter import Parameter
from .serial_port_settings import SerialPortSettings


class TestSettings:

    _cam: list[CameraSettings] = []
    _sp: list[SerialPortSettings] = []
    _cam_display = None
    _cam_leds = None
    _sp_main = None
    _sp_usb = None

    @staticmethod
    def get_cam_display():
        return TestSettings._cam_display

    @staticmethod
    def set_cam_display(name: str):
        cam_index = TestSettings.get_index_cam(name)
        if cam_index == -1:
            return -1
        else:
            TestSettings._cam_display = TestSettings._cam[cam_index]

    @staticmethod
    def get_cam_leds():
        return TestSettings._cam_leds

    @staticmethod
    def set_cam_leds(name: str):
        cam_index = TestSettings.get_index_cam(name)
        if cam_index == -1:
            # TODO: Error Code
            return -1
        else:
            TestSettings._cam_leds = TestSettings._cam[cam_index]

    @staticmethod
    def get_sp_main():
        return TestSettings._sp_main
    
    @staticmethod
    def set_sp_main(name: str):
        sp_index = TestSettings.get_index_sp(name)
        if sp_index == -1:
            # TODO: Error code
            return -1
        TestSettings._sp_main = TestSettings._sp[sp_index]

    @staticmethod
    def add_new_sp_settings(name: str, port: str, baudrate: int):
        TestSettings._sp.append(SerialPortSettings(name, port, baudrate))

    @staticmethod
    def get_index_sp(name: str):
        for i in range(len(TestSettings._sp)):
            sp_name = TestSettings._sp[i].get_name()
            if(sp_name == name):
                return i
        return -1
    
    @staticmethod
    def get_sp(name: str):
        index = TestSettings.get_index_sp(name)
        if index == -1:
            return None
        else:
            return TestSettings._sp[index]
    
    @staticmethod
    def delete_sp_settings(name: str):
        sp_index = TestSettings.get_index_sp(name)
        if sp_index != -1:
            TestSettings._sp.pop(sp_index)

    @staticmethod
    def add_new_cam_settings(settings: CameraSettings):
        TestSettings._cam.append(settings)

    @staticmethod
    def get_index_cam(name: str):
        for i in range(len(TestSettings._cam)):
            cam_name = TestSettings._cam[i].get_name()
            if(cam_name == name):
                return i
        return -1
    
    @staticmethod
    def get_cam(name: str):
        index = TestSettings.get_index_cam(name)
        if index == -1:
            return None
        else:
            return TestSettings._cam[index]

    @staticmethod
    def delete_cam_settings(name: str):
        cam_index = TestSettings.get_index_cam(name)
        if cam_index != -1:
            TestSettings._cam.pop(cam_index)
    