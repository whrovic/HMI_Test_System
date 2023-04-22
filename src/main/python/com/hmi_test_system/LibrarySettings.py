from data.Settings import Settings
from data.DefineAndFillModel import DefineAndFillModel as df
from data.model.Button import Button
from data.model.Display import Display
from data.model.Led import Led
from data.Settings import Settings
import os

def create_model_manual(M: Settings, name_model):
    
    
    while True:
        print("Number of buttons: ")
        n_buttons = input()    # number of buttons of model
        if n_buttons.isdigit():
            n_buttons = int(n_buttons)
            break
        else: 
            continue  
    
    while True:
        print("Number of leds: ")
        n_leds = input()        # number of leds of model
        if n_leds.isdigit():
            n_leds = int(n_leds)
            break
        else: 
            continue  


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

    # model exists 
    if(index != -1):

        # leds configuration
        print("\n\nLEDS CONFIGURATION\n")
        for i in range(0, n_leds):
            print(f"\nLed {i+1} name: ")
            led_name = input()
            while True:
                print(f"How many colours have the led {i+1}?")
                n_colours = input()
                if n_colours.isdigit():
                    n_colours = int(n_colours)
                    break
                else: 
                    continue
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


def add_models(M: Settings, directory):
    #------------------------------------ADD NEW MODEL------------------------------------#
    #try:
        while True:
            os.system('cls') 
            print("Insert the name of the new model:" )
            print("(to go to the menu insert q)\n" )
            name_model = input()
            
            
            # back to menu
            if(name_model == 'q'):
                break
            
            # model doesn't exist -> new configuration
            elif(df.open_model_xml(M, name_model, directory) is None):
                os.system('cls') 
                print(f"{name_model} DOESN'T EXIST\n")
                print("\n\n----------------------NEW MODEL CONFIGURATION----------------------\n")

                if ( create_model_manual(M, name_model) == 0):
                    df.create_xml(M, name_model, directory)

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
                print(f"{name_model} ALREADY EXISTS\n\n")
                print("To go to the menu insert anything\n")
                c = input()
                break

    #except:
'''    print("error")
        print("Do you want to repeat [y|n]")
        answer = input()
        if(answer == 'y'):
            add_models(M)'''
        
def edit_model(M: Settings, directory):

    n=1
    #------------------------------------EDIT MENU------------------------------------#
    while n:
            os.system('cls') 
            print("What model do you want to edit?" )
            print("(to go to the menu insert q)\n" )
            name_model = input()
            
            
            # back to menu
            if(name_model == 'q'):
                break

            # model doesn't exist -> new configuration
            elif(df.open_model_xml(M, name_model, directory) is None):
                os.system('cls') 
                print(f"{name_model} DOESN'T EXIST\n")
                print("To go to the menu insert anything\n" )
                c = input()
            
            # model  exists
            else:
                while True:
                    os.system('cls') 
                    print("-------------Edit Menu-------------\n\n")
                    print("1- Edit led          2- Edit button\n")
                    print("3- Edit LCD          4- Menu settings")
                    print("\n\n----------------------------------\n")
                
                    c= input()

                    # edit led
                    if c == '1':
                        n2 = 1
                    
                    # edit LCD
                    elif c == '2':
                        n2 = 2
                    
                    # edit button
                    elif c == '3':
                        n2 = 3
                    
                    # menu settings
                    elif c == '4':
                        n = 0
                        break
                    
                    else:
                        continue
                    
                    edit_led(M, n2, name_model)
                    edit_button(M, n2, name_model)
                    edit_display(n2, name_model)


def edit_led(M: Settings, n2, name_model):
    
    index = M.index_model(name_model)

    if(index == -1):
        return -1

    while n2==1:

        print("What led do you want to edit?")
        print("(to go to the menu insert q)\n" )
        led_name = input()

        # back to menu
        if(led_name == 'q'):
            n2 = 0
            break
        
        else:
            index_led = M.index_led(led_name) 
            
            if (index_led is None):
                print(f"{led_name} DOESN'T EXIST")
                print("To edit another one or go to the test menu insert anything\n")
                c = input()
                continue

            else:
                
        
         
         

def edit_button(M: Settings, n2, name_model):
    pass

def edit_display(M: Settings, n2, name_model):
    pass