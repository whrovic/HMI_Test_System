
from model_test.ModelTest import ModelTest
from model_test.ButtonTest import ButtonTest
from model_test.LedTest import LedTest
from model_test.DisplayTest import DisplayTest

from data.Led import Led
from data.Button import Button
from data.Display import Display


class ReportTerminal:

    def __init__(self, model_test : ModelTest):
        self.model_test = model_test
        
    def ButtonTerminal(self, codebutton : int):
        if(codebutton == 1):
            print("All button tests passed.\n")

        else :
            self.model_test.buttons_test    

    def LedTerminal(self):
        
     Led.result_press_display()
        

    def DisplayTerminal(self):    
        

#####################################################################

leds = [Led('L1','red',1,2), Led('L2','red',3,5), Led('L3','ok',5,7)]
#buttons = [Button((2, 3)), Button((4,5)), Button((7,9))]
display = Display('d1',5,7,10,20)

mt = ModelTest(leds, display)

report = ReportTerminal(mt)


report.LedTerminal()

