from data.Settings import Settings
from data.DefineAndFillModel import DefineAndFillModel as df
from data.model.Button import Button
from data.model.Display import Display
from data.model.Led import Led
from data.Settings import Settings
import os

def create_model_manual(M: Settings, name_model):
    
    print("Number of buttons: ")
    n_buttons = int(input())   # number of buttons of model
    
    print("Number of leds: ")
    n_leds= int(input())        # number of leds of model
    
    print("Model version: ")
    version = input()      # version of model

    # LCD configuration
    print("\n\nLCD CONFIGURATION\n")
    print("Select the LCD initial position")
    pos_vector_init = [0, 0]
    print("Select the LCD final position")
    pos_vector_final = [0, 0]
    
    dim_x = int(pos_vector_final[0]) - int(pos_vector_init[0])
    dim_y = int(pos_vector_final[1]) - int(pos_vector_init[1])
    display = Display('display', int(pos_vector_init[0]) , int(pos_vector_init[1]) , dim_x, dim_y)

    # add model 
    M.new_model(name_model, n_leds, n_buttons, display, version)

    index = M.index_model(name_model)

    print(f"index= {index}")

    # model exists 
    if(index != -1):

        # leds configuration
        print("\n\nLEDS CONFIGURATION\n")
        for i in range(0, n_leds):
            print(f"\nLed {i+1} name: ")
            led_name = input()
            print(f"How many colours have the led {i+1}?")
            n_colours = int(input())
            print(f"Select the led {i+1} central position")
            pos_vector = [0, 0]
            led = Led(led_name, n_colours, int(pos_vector[0]), int(pos_vector[1]))
            for j in range(0, n_colours):
                print(f"Colour {j+1} of led {i+1}:")
                new_colour = input()
                led.new_colour(new_colour)
             
            M.model[int(index)].set_led(led) 


        # buttons configuration
        print("\n\nBUTTONS CONFIGURATION\n")
        for i in range(0, n_buttons):
            print(f"\nButton {i+1} name: ")
            button_name = input()
            print(f"Select the button {i+1} central position")
            pos_vector = [0, 0]
            M.model[int(index)].set_button(Button(button_name, int(pos_vector[0]), int(pos_vector[1])))
        
        return 0
    
    # model doesn't exist
    else:
        print("ERROR - Model creation failed")
        M.delete_model(name_model)
        return -1


def add_models(M: Settings):
    #------------------------------------ADD NEW MODEL------------------------------------#
    #try:
        while True:
            os.system('cls') 
            print("Insert the name of the new model:" )
            print("(to go to the menu insert q)\n" )
            name_model = input()
            
            
            #directory = r"C:/Users/filip/Desktop/ES/Models"
            
            # back to menu
            if(name_model == 'q'):
                break
            
            # model doesn't exist -> new configuration
            #elif(df.open_model_xml(M, name_model, directory) is None):
            elif(M.call_model(name_model) is None):
                os.system('cls') 
                print(f"{name_model} DOESN'T EXIST\n")
                print("\n\n----------------------NEW MODEL CONFIGURATION----------------------\n")

                if ( create_model_manual(M, name_model) == 0):
                    #df.create_xml(M, name_model)

                    os.system('cls') 
                    print(f"{name_model} IS ADDED \n\n")
                    print("To go to the menu insert anything\n")
                    c = input()
                    break
                else:
                    os.system('cls') 
                    print(f"{name_model} IS NOT ADDED \n\n")
                    print("To go to the menu insert anything\n")
                    c = input()
                    break
            # model already exists
            else:
                os.system('cls') 
                print("MODEL ALREADY EXISTS\n\n")
                print("To go to the menu insert anything\n")
                c = input()
                break

    #except:
'''    print("error")
        print("Do you want to repeat [y|n]")
        answer = input()
        if(answer == 'y'):
            add_models(M)'''
        