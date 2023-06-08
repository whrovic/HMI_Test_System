from main.constant_main import *
from serial_port.serial_port import SerialPort
from video.camera import Camera


class SetupTest:
    
    __cam_leds = None
    __cam_display = None
    __sp_main = None
    __sp_usb = None

    @staticmethod
    def get_sp_main():
        return SetupTest.__sp_main
    
    @staticmethod
    def get_cam_leds():
        return SetupTest.__cam_leds

    @staticmethod
    def setup(cam_leds = False, cam_display = False, sp_main = False, sp_usb = False):
        # TODO: Ir buscar as definições das camaras e dos serial ports
        if cam_leds and (SetupTest.__cam_leds is None or SetupTest.__cam_leds.closed()):
            SetupTest.__cam_leds = Camera(0)
        if cam_display and (SetupTest.__cam_display is None or SetupTest.__cam_display.closed()):
            SetupTest.__cam_display = Camera(0)
        if sp_main and (SetupTest.__sp_main is None or SetupTest.__sp_main.closed()):
            SetupTest.__sp_main = SerialPort('COM5')
        if sp_usb and (SetupTest.__sp_usb is None or SetupTest.__sp_main.closed()):
            SetupTest.__sp_usb = SerialPort('COM4')
    
    @staticmethod
    def close(cam_leds = True, cam_display = True, sp_main = True, sp_usb = True):
        if cam_leds and SetupTest.__cam_leds is not None:
            SetupTest.__cam_leds.close()
            SetupTest.__cam_leds = None
        if cam_display and SetupTest.__cam_display is not None:
            SetupTest.__cam_display.close()
            SetupTest.__cam_display = None
        if sp_main and SetupTest.__sp_main is not None:
            SetupTest.__sp_main._serial.close()
            SetupTest.__sp_main = None
        if sp_usb and SetupTest.__sp_usb is not None:
            SetupTest.__sp_usb._serial.close()
            SetupTest.__sp_main = None