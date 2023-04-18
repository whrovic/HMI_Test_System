from data.Led import Led
from data.Button import Button
from data.Display import Display
from data.Settings import Settings


def create_model(M: Settings, name_model):
    
    print("Number of buttons: ")
    n_buttons = int(input())

    print("Number of leds: ")
    n_leds= int(input())

    #version
    print("Model version: ")
    version = int(input())

    #LCD
    print("LCD initial position: ")
    pos_vector_init = 'FUNCAO'
    print("LCD final position: ")
    pos_vector_final = 'FUNCAO'
    dim_x = pos_vector_final[0] - pos_vector_init[0]
    dim_y = pos_vector_final[1] - pos_vector_init[1]
    display = Display('display', pos_vector_init[0] , pos_vector_init[1] , dim_x, dim_y)

    #Adciona o modelo
    M.new_model(name_model, n_leds, n_buttons, display, version)

    index = M.index_model(name_model)

    if(index != -1):
        for i in range(0, n_leds):
            print("Led name: ")
            led_name = input()
            print(f"How many colours have the led {i+1}?")
            n_colours = int(input())
            print(f"Led {i+1} central position:")
            pos_vector = 'FUNCAO'
            led = Led(led_name, n_colours, pos_vector[0], pos_vector[1])
            for j in range(0, n_colours):
                print(f"Colour {j+1} of led {i+1}:")
                led.new_colour(input())

            M.model[int(index)].set_led(led)

        for i in range(0, n_buttons):
            print("Button name: ")
            button_name = input()
            print(f"Button {i+1} central position:")
            pos_vector = 'FUNCAO'
            M.model[int(index)].set_button(Button(button_name, pos_vector[0], pos_vector[1]))

    else:
        print("ERROR - Model creation failed")
        M.delete_model(name_model)

    


    
    
    

