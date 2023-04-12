from hmi_test_system.model.Settings import Settings
from hmi_test_system.model.Led import Led
from hmi_test_system.model.Button import Button
from hmi_test_system.model.Display import Display

M = Settings()
Leds_alarm = []
Leds_controll = []
Leds_buttons = []
Buttons_model = []
Special_buttons = []

name_model = 'm1'

n_specialbuttons = 9
n_buttons = 9
n_alarm = 16
n_controll = 3

x_alarm = 10
y_alarm = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]
colour_alarm1 = 'Yellow'
colour_alarm2 = 'Green'

x_buttons = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180]
y_buttons = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180]
colour_button1 = 'Red'
colour_button2 = 'Green'

x_controll = [10, 20, 30]
y_controll = 20
colour_controll1 = 'Red'
colour_controll2 = 'Green'

x_display = 0
y_display = 0
dim_x = 10
dim_y = 10


if(M.callModel(name_model) is None):

    display = Display('display', x_display , y_display , dim_x, dim_y)

    M.newModel(name_model, n_controll, n_alarm, n_buttons*2, n_buttons, n_specialbuttons, display, 2)

    index = M.indexModel(name_model)
    
    if(index != -1):
        
        for i in n_alarm:
            led = Led('LA'+str(i), 2, x_alarm, y_alarm[i])
            led.newColour(colour_alarm1)
            led.newColour(colour_alarm2)
            M.model[int(index)].setLedsAlarm(led)

        for i in n_controll:
            led = Led('LC'+str(i), 2, x_controll[i], y_controll)
            led.newColour(colour_controll1)
            led.newColour(colour_controll2)
            M.model[int(index)].setLedsControll(led)

        for i in n_buttons*2:
            led = Led('LB'+str(i), 1, x_buttons[i], y_buttons[i])
            if(i%2):
                led.newColour(colour_button1)
            else:
                led.newColour(colour_button2)
            M.model[int(index)].setLedsButtons(led)

        for i in n_buttons:
            M.model[int(index)].setButtonsModel(Button('BM'+str(i), 0, 0))

        for i in n_specialbuttons:
            M.model[int(index)].setSpecialButtons(Button('SB'+str(i), 0, 0))
    else:
        print("ERROR")


M.setModelTest(name_model)







