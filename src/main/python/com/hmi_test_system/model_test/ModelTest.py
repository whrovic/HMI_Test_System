from .DisplayTest import DisplayTest
from .ButtonTest import ButtonTest
from .LedTest import LedTest


class ModelTest:
    def __init__(self):
        self.leds_test: list[LedTest] = []
        self.buttons_test: list[ButtonTest] = []
        self.display_test: DisplayTest

    def clear_model_test(self):
        for i in range(0, len(self.buttons_test)):
            self.buttons_test[i].test_press_serial_port(False)
            self.buttons_test[i].test_press_display(False)

        for i in range(0, len(self.leds_test)):
            self.leds_test[i].clear_colour()

