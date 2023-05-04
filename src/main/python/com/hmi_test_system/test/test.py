import dis
from tkinter import Image

from data.model.model import Model
from model_test.model_test import ModelTest
from model_test.led_test import LedTest
from model_test.button_test import ButtonTest
from model_test.display_test import DisplayTest
#from opencv.hmicv import HMIcv
from video.camera import Camera

cam_value: Camera

class Test:

    @staticmethod
    def start_test():
        cam_value.start_capture()

    @staticmethod
    def end_test():
        cam_value.stop_capture()

    def test_button_display(self, buttons_test: list[ButtonTest]):
        # for i in range(0, len(buttons_test)):
        #     result =
        pass

    def test_button_serial_port(self, buttons_test: list[ButtonTest]):
        # for i in range(0, len(buttons_test)):
        pass

    def test_button(self, buttons_test: list[ButtonTest]):
        self.test_button_display()
        self.test_button_serial_port()

    def test_led(self, leds_test: list[LedTest]):
        for i in range(0, len(leds_test)):
            result = HMIcv.led_test(cam_value.get_image(), leds_test[i].get_led())
            if result is not None:
                leds_test[i].test_colour(result)

    def test_display(self, display: DisplayTest, test):
        if test == 1:
            result_blacklight = HMIcv.display_backlight_test(cam_value.get_image(), display.display)
            if result_blacklight:
                display.test_blacklight(result_blacklight)
                return 0
            else:
                return -1

        elif test == 2:
            result_color = HMIcv.display_color_pattern_test(cam_value.get_image(), display.display)
            if result_color:
                display.test_color(result_color)
                return 0
            else:
                return -1

        elif test == 3:
            result_character = HMIcv.display_characters_test(cam_value.get_image(), display.display)
            if result_character:
                display.test_characters(result_character)
                return 0
            else:
                return -1

        elif test == 4:
            result_blacklight = HMIcv.display_backlight_test(cam_value.get_image(), display.display)
            result_color = HMIcv.display_color_pattern_test(cam_value.get_image(), display.display)
            result_character = HMIcv.display_characters_test(cam_value.get_image(), display.display)
            if result_blacklight:
                display.test_blacklight(result_blacklight)
            else:
                return -1
            if result_color:
                display.test_color(result_color)
            else:
                return -1
            if result_character:
                display.test_characters(result_character)
                return 0
            else:
                return -1
