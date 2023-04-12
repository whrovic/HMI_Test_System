from LedTest import LedTest
from ButtonTest import ButtonTest
from DisplayTest import DisplayTest
from Model import Model
from Led import Led
from Button import Button
from Display import Display

class ModelTest:
    
    def __init__(self, model: Model):
        self.model = model
        self.ledsControll_test = [LedTest]

    def setModelTest(self):
        for i in self.model.nledsControll:
             self.ledsControll_test.append(LedTest(self.model.ledsControll[i]))

        
