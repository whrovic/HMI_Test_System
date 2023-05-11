from opencv.hmicv import HMIcv
from video.camera import Camera
from serial.serial_port import SerialPort

from data.model.display import Display
from data.model.button import Button
from data.model.led import Led

class Test:

    @staticmethod
    def test_button_display(button_sequence: list[Button]):
        return -1

    # return 0 - Test passed, -1 not passed
    @staticmethod
    def test_button_serial_port(serial: SerialPort, button_sequence: list[Button]):
        for button in button_sequence:
            data, time = serial.get_serial()
            if data.endswith(button.get_name):
                serial.get_serial()
                continue
            return -1
        
        data, time = serial.get_serial()
        if data != "TestKeys - Test OK":
            return -1
        
        return 0

    @staticmethod
    def test_button(cam: Camera, serial: SerialPort, button_sequence: list[Button], SP = True, DP = False):
        return Test.test_button_serial_port(serial, button_sequence)

    # return 0 - Test passed, -1 not passed
    @staticmethod
    def test_display(cam: Camera, serial: SerialPort, display: Display):
        return -1

    @staticmethod
    def start_test():
        pass

    @staticmethod
    def end_test():
        pass

    @staticmethod
    def test_led(cam: Camera, led_sequence: list[Led]):
        return -1