import dis
from tkinter import Image

from ..data.model.model import Model
from ..model_test.model_test import ModelTest
from ..model_test.led_test import LedTest
from ..data.model.led import Led
from ..model_test.button_test import ButtonTest
from ..model_test.display_test import DisplayTest
from ..opencv.hmicv import HMIcv
from ..video.camera import Camera
from ..data.color.color import Color

cam_value: Camera
vet_cor: list[37]
vet_cor_bef: list[56][37]


# TODO: complet the start_test and end_test
# with the right functions

class Test:

    @staticmethod
    def start_test(cam_leds: bool, cam_display: bool, serial_port: bool):
        if cam_leds:
            pass
        elif cam_display:
            pass
        elif serial_port:
            pass
        cam_value.start_capture()

    @staticmethod
    def end_test(cam_leds: bool, cam_display: bool, serial_port: bool):
        if cam_leds:
            pass
        elif cam_display:
            pass
        elif serial_port:
            pass
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

    def test_led(self, leds_test: list[Led]):
        state = 0
        aux = 0
        while 1:
            cam = cam_value.get_image()

            for i in range(0, len(leds_test)):
                vet_cor[i] = HMIcv.led_test(cam, leds_test[i])
            if state == 0:
                aux = 0
                for i in range(0, len(leds_test)):
                    if vet_cor[i] is not None:
                        aux = aux + 1
                if aux == len(leds_test):
                    led_test_pass_terminal(state)
                    state = 1
                else:
                    led_test_error_terminal(state)
                    return -1

            if state == 1:
                aux = 0
                for i in range(0, len(leds_test)):
                    if vet_cor[i] is None:
                        aux = aux + 1
                if aux == len(leds_test):
                    led_test_pass_terminal(state)
                    state = 2
                else:
                    led_test_error_terminal(state)
                    return -1

            if state == 2:
                aux = 0
                for i in range(0, len(leds_test)):
                    if vet_cor[i] is not None:
                        aux = aux + 1
                if aux == len(leds_test):
                    led_test_pass_terminal(state)
                    state = 3
                else:
                    led_test_error_terminal(state)
                    return -1

            if state == 3:
                aux = 0
                cam_bef = None
                for i in range(0, 56):
                    for j in range(0, len(leds_test)):
                        if cam != cam_bef:
                            vet_cor_bef[i][j] = HMIcv.led_test(cam, leds_test[i])
                    cam_bef = cam
                    cam = cam_value.get_image()
                for i in range(0, 56):
                    for j in range(0, len(leds_test)):
                        for k in range(0, len(leds_test[j].get_colour())):
                            if vet_cor_bef[i][j] == leds_test[j].get_colour()[k]:
                                aux = aux + 1
                            elif vet_cor_bef[i][j] != leds_test[j].get_colour()[k]:


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


def led_test_error_terminal(code):
    if code == 0 or code == 2:
        print("Error on turned on LED's\n")
    elif code == 1:
        print("Error on turned off LED's\n")


def led_test_pass_terminal(code):
    if code == 0 or code == 2:
        print("All the leds Turn ON")
    elif code == 1:
        print("All the leds Turn OFF")
