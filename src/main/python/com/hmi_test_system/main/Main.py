from hmi_test_system.model.Settings import Settings
from hmi_test_system.model.Led import Led
from hmi_test_system.model.Button import Button
from hmi_test_system.model.Display import Display
from hmi_test_system.model.Model import Model


M = Settings()
Leds_alarm = []
Leds_controll = []
Leds_buttons = []
Buttons_model = []
Special_buttons = []

name = 'm1'

n_specialbuttons = 9
n_buttons = 9
n_alarm = 16
n_controll = 3

x_alarm = 10
y_alarm = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]

x_buttons = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180]
y_buttons = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180]

x_controll = [10, 20, 30]
y_controll = 20

x_display = 0
y_display = 0
dim_x = 10
dim_y = 10


if(M.callModel(name) is None):

    display = Display('display', x_display , y_display , dim_x, dim_y)

    M.newModel(name, n_controll, n_alarm, n_buttons*2, n_buttons, n_specialbuttons, display, 2)

    index = M.indexModel(name)
    
    if(index != -1):
        for i in n_alarm:
            M.model[int(index)].setLedsAlarm(Led('LA'+str(i), 2, x_alarm, y_alarm[i]))

        for i in n_controll:
            M.model[int(index)].setLedsControll(Led('LC'+str(i), 2, x_controll[i], y_controll))

        for i in n_buttons*2:
            M.model[int(index)].setLedsButtons(Led('LB'+str(i), 2, x_buttons[i], y_buttons[i] ))

        for i in n_buttons:
            M.model[int(index)].setButtonsModel(Button('BM'+str(i), 0, 0))

        for i in n_specialbuttons:
            M.model[int(index)].setSpecialButtons(Button('SB'+str(i), 0, 0))
    else:
        print("ERROR")


M.setModelTest(name)







