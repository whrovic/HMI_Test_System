from data.Led import Led
from data.Button import Button
from data.Display import Display
from data.Settings import Settings

def create_model(M: Settings, name_model):
    
    print("Numero de botoes especiais: ")
    n_special_buttons = int(input())

    print("Numero de botoes de função: ")
    n_buttons_model = int(input())

    print("Numero de leds de alarme: ")
    n_alarm = int(input())

    print("Numero de leds de controlo: ")
    n_control = int(input())


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
    for i in n_buttons_model:
        print("Pos x do led de botão %d: ", i)
        x_buttons.append(int(input()))
        print("Pos y do led de botão %d: ", i)
        y_buttons.append(int(input()))
    print("Cor 1 do led de botão: ")
    colour_button1 = input()
    print("Cor 2 do led de botão: ")
    colour_button2 = input()


    #leds de controlo
    x_control = []
    for i in n_control:
        print("Pos x do led de controlo %d: ", i)
        x_control.append(int(input))
    print("Pos y dos leds de controlo: ")
    y_controll = int(input())
    print("Cor 1 do led de controlo: ")
    colour_control1 = input()
    print("Cor 2 do led de controlo: ")
    colour_control2  = input()


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
    M.new_model(name_model, n_control, n_alarm, n_buttons_model*2, n_buttons_model, n_special_buttons, display, version)

    index = M.index_model(name_model)
    
    if(index != -1):
        for i in n_alarm:
            led = Led('LA'+str(i), 2, x_alarm, y_alarm[i])
            led.new_colour(colour_alarm1)
            led.new_colour(colour_alarm2)
            M.model[int(index)].set_led_alarm(led)

        for i in n_control:
            led = Led('LC'+str(i), 2, x_control[i], y_controll)
            led.new_colour(colour_control1)
            led.new_colour(colour_control2)
            M.model[int(index)].set_led_control(led)

        for i in n_buttons_model*2:
            led = Led('LB'+str(i), 1, x_buttons[i], y_buttons[i])
            if(i%2):
                led.new_colour(colour_button1)
            else:
                led.new_colour(colour_button2)
            M.model[int(index)].set_led_buttons(led)

        for i in n_buttons_model:
            M.model[int(index)].set_button_model(Button('BM'+str(i), 0, 0))

        for i in n_special_buttons:
            M.model[int(index)].set_special_button(Button('SB'+str(i), 0, 0))
    else:
        print("ERROR - Modelo mal criado")
        M.delete_model(name_model)

