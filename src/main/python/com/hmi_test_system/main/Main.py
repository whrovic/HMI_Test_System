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


print("Nome do modelo: ")
name_model = input()


if(M.callModel(name_model) is None):
    
    print("MODELO NOVO")

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
    print("Pos y do leds de controlo: ")
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

    #Cria o modelo
    M.newModel(name_model, n_controll, n_alarm, n_buttonsmodel*2, n_buttonsmodel, n_specialbuttons, display, 2)

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

        for i in n_buttonsmodel*2:
            led = Led('LB'+str(i), 1, x_buttons[i], y_buttons[i])
            if(i%2):
                led.newColour(colour_button1)
            else:
                led.newColour(colour_button2)
            M.model[int(index)].setLedsButtons(led)

        for i in n_buttonsmodel:
            M.model[int(index)].setButtonsModel(Button('BM'+str(i), 0, 0))

        for i in n_specialbuttons:
            M.model[int(index)].setSpecialButtons(Button('SB'+str(i), 0, 0))
    else:
        print("ERROR - Modelo mal criado")
        M.deleteModel(name_model)


else:
    print("MODELO EXISTENTE")


M.setModelTest(name_model)







