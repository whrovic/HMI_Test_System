
from model_test.ModelTest import ModelTest
from model_test.ButtonTest import ButtonTest
from model_test.LedTest import LedTest
from model_test.DisplayTest import DisplayTest

class ReportTerminal:

    def __init__(self, model_test : ModelTest):
        self.model_test = model_test
        
    def ButtonTerminal(self, codebutton : int):
        if(codebutton == 1):
            print("All button tests passed.\n")

        else :
            self.model_test.buttons_test    

    def LedTerminal(self):
        

    def DisplayTerminal(self):    


mt = ModelTest()

report = ReportTerminal(mt)

tt = LedTest()
report.LedTerminal()

