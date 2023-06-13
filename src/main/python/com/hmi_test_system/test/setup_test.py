from main.constant_main import *
from serial_port.serial_port import SerialPort
from video.camera import Camera
from data.hardware_settings.test_settings import TestSettings


class SetupTest:
    
    _cam_leds = None
    _cam_display = None
    _sp_main = None
    _sp_usb = None

    @staticmethod
    def setup(cam_leds = False, cam_display = False, sp_main = False, sp_usb = False):
        # TODO: Ir buscar as definições das camaras e dos serial ports
        if cam_leds and (SetupTest._cam_leds is None or SetupTest._cam_leds.closed()):
            cam_leds_settings = TestSettings.get_cam_leds()
            if cam_leds_settings is not None:
                camera_id = cam_leds_settings.get_device_id()
                SetupTest._cam_leds = Camera(camera_id)
        if cam_display and (SetupTest._cam_display is None or SetupTest._cam_display.closed()):
            cam_dsp_settings = TestSettings.get_cam_display()
            if cam_dsp_settings is not None:
                camera_id = cam_dsp_settings.get_device_id()
                SetupTest._cam_display = Camera(camera_id)
        if sp_main and (SetupTest._sp_main is None or SetupTest._sp_main.closed()):
            try:
                sp_main_settings = TestSettings.get_sp_main()
                if sp_main_settings is not None:
                    sp_port = sp_main_settings.get_port()
                    SetupTest._sp_main = SerialPort(sp_port)
            except:
                print("Couldn't open sp")
                pass
        if sp_usb and (SetupTest._sp_usb is None or SetupTest._sp_main.closed()):
            pass
    
    @staticmethod
    def close(cam_leds = True, cam_display = True, sp_main = True, sp_usb = True):
        if cam_leds and SetupTest._cam_leds is not None:
            SetupTest._cam_leds.close()
            SetupTest._cam_leds = None
        if cam_display and SetupTest._cam_display is not None:
            SetupTest._cam_display.close()
            SetupTest._cam_display = None
        if sp_main and SetupTest._sp_main is not None:
            SetupTest._sp_main._serial.close()
            SetupTest._sp_main = None
        if sp_usb and SetupTest._sp_usb is not None:
            SetupTest._sp_usb._serial.close()
            SetupTest._sp_main = None
    
    @staticmethod
    def get_cam_leds():
        return SetupTest._cam_leds
    
    @staticmethod
    def get_cam_display():
        return SetupTest._cam_display
    
    @staticmethod
    def get_sp_main():
        return SetupTest._sp_main
    
    @staticmethod
    def get_sp_usb():
        return SetupTest._sp_usb
    