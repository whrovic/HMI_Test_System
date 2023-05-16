
from model_test.ModelTest import ModelTest
from model_test.ButtonTest import ButtonTest as B
from model_test.LedTest import LedTest as L
from model_test.DisplayTest import DisplayTest as Dp

from data.model.Led import Led
from data.model.Button import Button
from data.model.Display import Display


class ReportTerminal:

    def __init__(self, model_test : ModelTest):
        self.model_test = model_test
        
    def ButtonTerminal(self, codebutton : int):
        if(codebutton == 1):
            print("All button tests passed.\n")

        else :
            self.model_test.buttons_test    

    def LedTerminal(self, led:L):
        
        #Led.result_press_display()
        rgbvalue = led.get_led(self)
        aux = led.get_colour_result()
    

    def DisplayTerminal(self):   
        print(self.rgbvalue) 

        resultcolor = Dp.result_blacklight(self)
        dfg = Dp.result_color()
b = ModelTest()
a = ReportTerminal(b)
a.LedTerminal()





'''mt = ModelTest(leds, display)

report = ReportTerminal(mt)


report.LedTerminal()
'''
