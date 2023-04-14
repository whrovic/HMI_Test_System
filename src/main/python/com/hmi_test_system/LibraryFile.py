from data.Led import Led
from data.Button import Button
from data.Display import Display
from data.Settings import Settings


def create_model_file(M: Settings, name_model, name_file):
    with open(name_file, 'r') as file:
        # Read lines from the file
        name_model = file.readlines()
        lines = file.readlines()

        # Extract values from lines
        n_special_buttons = int(lines[0])
        n_buttons_model = int(lines[1])
        n_alarm = int(lines[2])
        n_control = int(lines[3])
        x_alarm = int(lines[4])
        y_alarm = [int(line) for line in lines[5:5+n_alarm]]
        colour_alarm1 = lines[5+n_alarm].strip()
        colour_alarm2 = lines[5+n_alarm+1].strip()
        x_buttons = []
        y_buttons = []
        for i in range(0, n_buttons_model*2):
            x_buttons.append(int(lines[5+n_alarm+2+i*2]))
            y_buttons.append(int(lines[5+n_alarm+3+i*2]))
        colour_button1 = lines[5+n_alarm+2+n_buttons_model*2].strip()
        colour_button2 = lines[5+n_alarm+3+n_buttons_model*2].strip()
        x_control = [int(line) for line in lines[5+n_alarm+4+n_buttons_model*2:5+n_alarm+4+n_buttons_model*2+n_control]]
        y_controll = int(lines[5+n_alarm+4+n_buttons_model*2+n_control].strip())
        colour_control1 = lines[5+n_alarm+5+n_buttons_model*2+n_control].strip()
        colour_control2 = lines[5+n_alarm+6+n_buttons_model*2+n_control].strip()
        x_display = int(lines[5+n_alarm+7+n_buttons_model*2+n_control].strip())
        y_display = int(lines[5+n_alarm+8+n_buttons_model*2+n_control].strip())
        dim_x = int(lines[5+n_alarm+9+n_buttons_model*2+n_control].strip())
        dim_y = int(lines[5+n_alarm+10+n_buttons_model*2+n_control].strip())
        version = int(lines[5+n_alarm+11+n_buttons_model*2+n_control].strip())

    
    display = Display('display', x_display , y_display , dim_x, dim_y)
    
    #Adciona o modelo
    M.new_model(name_model, n_control, n_alarm, n_buttons_model*2, n_buttons_model, n_special_buttons, display, version)

    index = M.index_model(name_model)
    
    if(index != -1):
        for i in range(0, n_alarm):
            led = Led('LA'+str(i+1), 2, x_alarm, y_alarm[i])
            led.new_colour(colour_alarm1)
            led.new_colour(colour_alarm2)
            M.model[int(index)].set_led_alarm(led)

        for i in range(0, n_control):
            led = Led('LC'+str(i+1), 2, x_control[i], y_controll)
            led.new_colour(colour_control1)
            led.new_colour(colour_control2)
            M.model[int(index)].set_led_control(led)

        for i in range(0, n_buttons_model*2):
            led = Led('LB'+str(i+1), 1, x_buttons[i], y_buttons[i])
            if(i%2):
                led.new_colour(colour_button1)
            else:
                led.new_colour(colour_button2)
            M.model[int(index)].set_led_buttons(led)

        for i in range(0, n_buttons_model):
            M.model[int(index)].set_button_model(Button('BM'+str(i+1), 0, 0))

        for i in range(0, n_special_buttons):
            M.model[int(index)].set_special_button(Button('SB'+str(i), 0, 0))
    else:
        print("ERROR - Modelo mal criado")
        M.delete_model(name_model)
