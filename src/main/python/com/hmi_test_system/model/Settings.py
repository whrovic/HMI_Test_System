from Model import Model
from hmi_test_system.test import SequenceTest
from ModelTest import ModelTest
from LedTest import LedTest
from ButtonTest import ButtonTest
from DisplayTest import DisplayTest
from Display import Display
from typing import List


class Settings:
        
    def __init__(self):
        self.model:List[Model] = []
        self.mT = ModelTest()
        self.sequenceTest = SequenceTest


    def newModel(self, name, nledsControll, nledsAlarm, nledsButtons, nbuttonsModel, nspecialButtons, display: Display, version):
        self.model.append(Model(name, nledsControll, nledsAlarm, nledsButtons, nbuttonsModel, nspecialButtons, display, version))


    def setModelTest(self, name):
        N_model = -1

        for i in len(self.model):
            if(name == self.model[i].name):
                N_model = i
                break

        if(N_model == -1):
            print("ERROR")
            return

        for i in self.model[N_model].nledsControll:
             self.mT.ledsControll_test.append(LedTest(self.model[N_model].ledsControll[i]))

        for i in self.model[N_model].nledsAlarm:
            self.mT.ledsAlarm_test.append(LedTest(self.model[N_model].ledsAlarm[i]))

        for i in self.model[N_model].nledsButtons:
            self.mT.ledsButtons_test.append(LedTest(self.model[N_model].ledsButtons[i]))

        for i in self.model[N_model].nbuttonsModel:
            self.mT.buttonsModel_test.append(ButtonTest(self.model[N_model].buttonsModel[i]))

        for i in self.model[N_model].nspecialButtons:
            self.mT.specialButtons_test.append(ButtonTest(self.model[N_model].specialButtons[i]))   

        self.mT.display_test= DisplayTest(self.model[N_model].display)   


    def callModel(self, name):
        for i in len(self.model):
            if(name == self.model[i].name):
                return self.model[i]
        
        #nao encontra o modelo
        return None 