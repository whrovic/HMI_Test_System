import Led
import Button
import Display

class Model:
    
    def __init__(self, name, version):
        self.name = name
        self.ledsControll = Led
        self.ledsAlarm = Led
        self.ledsButtons = Led
        self.buttonsModel = Button
        self.specialButtons = Button
        self.display = Display
        self.version = version
    
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name

    def setModel(self):
        pass
   
