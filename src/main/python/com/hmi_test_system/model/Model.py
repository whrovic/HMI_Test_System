from Led import Led
from Button import Button
from Display import Display

class Model:
    
    def __init__(self, name, nledsControll, nledsAlarm, nledsButtons, nbuttonsModel, nspecialButtons, display: Display, version):
        self.name = name
        self.nledsControll = nledsControll
        self.nledsAlarm = nledsAlarm
        self.nledsButtons = nledsButtons
        self.nbuttonsModel = nbuttonsModel
        self.nspecialButtons = nspecialButtons
        self.display = display
        self.version = version
        self.ledsControll = []
        self.ledsAlarm = []
        self.ledsButtons = []
        self.buttonsModel = []
        self.specialButtons = []
    
    
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name


    #vetor dos leds de controlo 
    def setLedsControll(self, led: Led):
        if(len(self.ledsControll) < self.nledsControll):
            self.ledsControll.append(led)
        else:
            print("ERROR")
    
    def deleteLedsControll(self):
        self.ledsControll = []


    #vetor dos leds de alarme 
    def setLedsAlarm(self, led: Led):
        if(len(self.ledsAlarm) < self.nledsAlarm):
            self.ledsAlarm.append(led)
        else:
            print("ERROR")
    
    def deleteLedsAlarm(self):
        self.ledsAlarm = []


    #vetor dos leds dos botoes       
    def setLedsButtons(self, led: Led):
        if(len(self.ledsButtons) < self.nledsButtons):
            self.ledsButtons.append(led)
        else:
            print("ERROR")
    
    def deleteLedsButton(self):
        self.ledsButtons = []


    #vetor dos botoes
    def setButtonsModel(self, button: Button):
        if(len(self.buttonsModel) < self.nbuttonsModel):
            self.buttonsModel.append(button)
        else:
            print("ERROR")
    
    def deleteButtonsModel(self):
        self.buttonsModel = []

    
    #vetor dos botoes especiais
    def setSpecialButtons(self, button: Button):
        if(len(self.specialButtons) < self.nspecialButtons):
            self.specialButtons.append(button)
        else:
            print("ERROR")
    
    def deleteSpecialButtons(self):
        self.specialButtons = []
   
