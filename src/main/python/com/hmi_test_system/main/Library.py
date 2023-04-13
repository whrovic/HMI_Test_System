from hmi_test_system.data.Led import Led
from hmi_test_system.data.Button import Button
from hmi_test_system.data.Display import Display
from hmi_test_system.data.Settings import Settings

def createModel(settings: Settings, name_model):
    
    print("Numero de botoes especiais: ")
    n_specialbuttons = int(input())

    print("Numero de botoes de função: ")
    n_buttonsmodel = int(input())

    print("Numero de leds de alarme: ")
    n_alarm = int(input())

    print("Numero de leds de controlo: ")
    n_controll = int(input())


    #leds dos alarmes
    print("Pos x dos leds de alarme: ")
    x_alarm = int(input())
    y_alarm = []
    for i in n_alarm:
        print("Pos y do led %d de alarme: ", i)
        y_alarm.append(int(input()))
    print("Cor 1 do led de alarme: ")
    colour_alarm1 = input()
    print("Cor 2 do led de alarme: ")
    colour_alarm2 = input()


    #leds dos botões
    x_buttons = []
    y_buttons = []
    for i in n_buttonsmodel:
        print("Pos x do led de botão %d: ", i)
        x_buttons.append(int(input()))
        print("Pos y do led de botão %d: ", i)
        y_buttons.append(int(input()))
    print("Cor 1 do led de botão: ")
    colour_button1 = input()
    print("Cor 2 do led de botão: ")
    colour_button2 = input()


    #leds de controlo
    x_controll = []
    for i in n_controll:
        print("Pos x do led de controlo %d: ", i)
        x_controll.append(int(input))
    print("Pos y dos leds de controlo: ")
    y_controll = int(input())
    print("Cor 1 do led de controlo: ")
    colour_controll1 = input()
    print("Cor 2 do led de controlo: ")
    colour_controll2  = input()


    #LCD
    print("Pos x do LCD: ")
    x_display = int(input())
    print("Pos y do LCD: ")
    y_display = int(input())
    print("Dim_x do LCD: ")
    dim_x = int(input())
    print("Dim_y do LCD: ")
    dim_y = int(input())
    display = Display('display', x_display , y_display , dim_x, dim_y)


    #version
    print("Versao do modelo: ")
    version = int(input())
    

    #Adciona o modelo
    settings.newModel(name_model, n_controll, n_alarm, n_buttonsmodel*2, n_buttonsmodel, n_specialbuttons, display, version)

    index = settings.indexModel(name_model)
    
    if(index != -1):
        for i in n_alarm:
            led = Led('LA'+str(i), 2, x_alarm, y_alarm[i])
            led.newColour(colour_alarm1)
            led.newColour(colour_alarm2)
            settings.model[int(index)].setLedsAlarm(led)

        for i in n_controll:
            led = Led('LC'+str(i), 2, x_controll[i], y_controll)
            led.newColour(colour_controll1)
            led.newColour(colour_controll2)
            settings.model[int(index)].setLedsControll(led)

        for i in n_buttonsmodel*2:
            led = Led('LB'+str(i), 1, x_buttons[i], y_buttons[i])
            if(i%2):
                led.newColour(colour_button1)
            else:
                led.newColour(colour_button2)
            settings.model[int(index)].setLedsButtons(led)

        for i in n_buttonsmodel:
            settings.model[int(index)].setButtonsModel(Button('BM'+str(i), 0, 0))

        for i in n_specialbuttons:
            settings.model[int(index)].setSpecialButtons(Button('SB'+str(i), 0, 0))
    else:
        print("ERROR - Modelo mal criado")
        settings.deleteModel(name_model)

