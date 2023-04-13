from Model import Model
from hmi_test_system.test.SequenceTest import SequenceTest
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
        self.sequence_test = SequenceTest


    def newModel(self, name, nledsControll, nledsAlarm, nledsButtons, nbuttonsModel, nspecialButtons, display: Display, version):
        self.model.append(Model(name, nledsControll, nledsAlarm, nledsButtons, nbuttonsModel, nspecialButtons, display, version))

    
    def callModel(self, name):
        for i in len(self.model):
            if(name == self.model[int(i)].name):
                return self.model[i]
        
        #nao encontra o modelo
        return None

    
    def indexModel(self, name):
        for i in len(self.model):
            if(name == self.model[int(i)].name):
                return i
        
        #nao encontra o modelo
        return -1
    
    def deleteModel(self, name):
        N_model = int(self.indexModel(name))

        if(N_model == -1):
            print("ERROR - Modelo a eliminar não existe")
        else:
            self.model.remove(N_model)


    def setModelTest(self, name):
        n_model = int(self.indexModel(name))

        if(n_model == -1):
            print("ERROR - Modelo a testar não existe")
            return
        else:
            for i in self.model[n_model].nledsControll:
                self.mT.ledsControll_test.append(LedTest(self.model[n_model].ledsControll[i]))

            for i in self.model[n_model].nledsAlarm:
                self.mT.ledsAlarm_test.append(LedTest(self.model[n_model].ledsAlarm[i]))

            for i in self.model[n_model].nledsButtons:
                self.mT.ledsButtons_test.append(LedTest(self.model[n_model].ledsButtons[i]))

            for i in self.model[n_model].nbuttonsModel:
                self.mT.buttonsModel_test.append(ButtonTest(self.model[n_model].buttonsModel[i]))

            for i in self.model[n_model].nspecialButtons:
                self.mT.specialButtons_test.append(ButtonTest(self.model[n_model].specialButtons[i]))   

            self.mT.display_test= DisplayTest(self.model[n_model].display) 