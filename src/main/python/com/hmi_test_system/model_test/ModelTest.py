from model_test.DisplayTest import DisplayTest
from model_test.ButtonTest import ButtonTest
from model_test.LedTest import LedTest

class ModelTest:
    def __init__(self):
        self.leds_test: list[LedTest] = []
        self.buttons_test: list[ButtonTest] = []
        self.display_test: DisplayTest
