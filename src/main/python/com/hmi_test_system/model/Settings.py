from Model import Model
from hmi_test_system.test import SequenceTest
from ModelTest import ModelTest
from LedTest import LedTest
from ButtonTest import ButtonTest
from DisplayTest import DisplayTest

class Settings:
    model = Model('M', 2, 3,4,5,6,1,2)
    sequenceTest = SequenceTest
    mT = ModelTest()

    def setModelTest(self):
        for i in self.model.nledsControll:
             self.mT.ledsControll_test.append(LedTest(self.model.ledsControll[i]))

        for i in self.model.nledsAlarm:
            self.mT.ledsAlarm_test.append(LedTest(self.model.ledsAlarm[i]))

        for i in self.model.nledsButtons:
            self.mT.ledsButtons_test.append(LedTest(self.model.ledsButtons[i]))

        for i in self.model.nbuttonsModel:
            self.mT.buttonsModel_test.append(ButtonTest(self.model.buttonsModel[i]))

        for i in self.model.nspecialButtons:
            self.mT.specialButtons_test.append(ButtonTest(self.model.specialButtons[i]))   

        self.mT.display_test= DisplayTest(self.model.display)


