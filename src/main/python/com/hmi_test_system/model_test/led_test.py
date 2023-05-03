from data.model.Led import Led
from data.color.color import Color
import copy

class LedTest:
    def __init__(self, led: Led):
        self.led = copy.deepcopy(led)
        self.colours_cv: list[Color] = []

    def set_led(self, led):
        self.led = led

    def get_led(self):
        return self.led


    # vetor de cores detetas por cv
    def test_colour(self, colour):
        self.colours_cv.append(colour)

    def get_colour_result(self):
        return self.colours_cv

    def result_test_Led(self):
        if self.colours_cv == self.led._colours:
            return 1
        else:
            return 0

    def clear_colour(self):
        self.colours_cv.clear()