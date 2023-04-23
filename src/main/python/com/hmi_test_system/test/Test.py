from tkinter import Image

from ..data.model.Model import Model
from ..data.SequenceTest import SequenceTest
from ..model_test.ModelTest import ModelTest
from ..model_test.LedTest import LedTest
from ..model_test.ButtonTest import ButtonTest
from ..model_test.DisplayTest import DisplayTest
from ..opencv.

class Test:
        
    def test_button_serial_port(self, buttons_test: ButtonTest):

        pass
    def test_leds(self, leds_test: list[LedTest], img: Image):
        for i in range(0, len(leds_test)):
            result = led_test(img, led)
            if result != None
                leds_test[i] =
