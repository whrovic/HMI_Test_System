from data.model.Display import Display
import copy

class DisplayTest:
    color_test: bool
    blacklight_test: bool
    characters_test: bool

    def __init__(self, display: Display):
        self.display = copy.deepcopy(display)
    
    # RGB screen detetado por CV
    def RGB_CV(self, RGB):
        self.RGB = RGB
       
    def test_RGB(self):
        return self.RGB

    def result_color(self):
        return self.color_test

    def test_color(self, result):
        if result:
            self.color_test = True

    def result_blacklight(self):
        return self.blacklight_test

    def test_blacklight(self, result):
        if result:
            self.blacklight_test_test = True

    def result_characters(self):
        return self.characters_test

    def test_characters(self, result):
        if result:
            self.characters_test = True
