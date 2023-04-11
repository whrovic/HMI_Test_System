import LedTest
import ButtonTest
import Display

class Model:
    
    def __init__(self, name, version):
        self.name = name
        self.ledsControll = LedTest
        self.ledsAlarm = LedTest
        self.ledsButtons = LedTest
        self.buttonsModel = ButtonTest
        self.specialButtons = ButtonTest
        self.display = Display
        self.version = version
    
    def setModelTest(self):
        pass

    def clearModelTest(self):
        pass