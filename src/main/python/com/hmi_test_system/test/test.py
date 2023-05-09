import dis
from tkinter import Image

from ..data.model.model import Model
from ..model_test.model_test import ModelTest
from ..model_test.led_test import LedTest
from ..model_test.button_test import ButtonTest
from ..model_test.display_test import DisplayTest
from ..opencv.hmicv import HMIcv
from ..video.camera import Camera
from ..data.color.color import Color

cam_value: Camera
vet_cor: list [37]
vet_cor_bef: list [37]


#TODO: complet the start_test and end_test 
# whith the right functions

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

    def test_led(self, leds_test: list[LedTest]):
        state = 0
        aux = 0
        while 1:
            cam = cam_value.get_image()
            for i in range(0, len(leds_test)):
                vet_cor[i] = HMIcv.led_test(cam, leds_test[i].get_led())
            if state == 0:
                aux = 0
                for i in range(0, len(leds_test)):
                    if vet_cor[i] is not None:
                        aux = aux + 1
                if aux == len(leds_test):
                    state = 1
                else:
                    # fazer funçao de escrever no terminal
                    return -1
            if state == 1:
                aux = 0
                for i in range(0, len(leds_test)):
                    if vet_cor[i] is None:
                        aux = aux + 1
                if aux == len(leds_test):
                    state = 2
                else:
                    # fazer funçao de escrever no terminal
                    return -1
            if state == 2:
                aux = 0
                for i in range(0, len(leds_test)):
                    if vet_cor[i] is not None:
                        aux = aux + 1
                if aux == len(leds_test):
                    state = 3
                else:
                    # fazer funçao de escrever no terminal
                    return -1
            if state == 3:
                aux = 0
                #for i in range(0, len(leds_test)):
                if vet_cor[0].get_name() == 'green' and vet_cor[0].get_name() != vet_cor_bef[0].get_name():

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
