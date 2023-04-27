from data.Settings import Settings
from data.DefineAndFillModel import DefineAndFillModel as df
from data.model.Button import Button
from data.model.Display import Display
from data.model.Led import Led
from data.DefineModelCV import DefineModelCV
from video.image_files import ImageFiles
import os


def create_model_manual(M: Settings, name_model):

    img_path = "test_images/HMI.png"

    cap = ImageFiles([img_path])

    cap.start_capture()

    image = cap.get_image()

    cap.stop_capture()
    cap.clear_queue()

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

    while True:
        print("Model version:")
        version = str(input())       # version of model
        version = version.strip()
        if (len(version) > 0):
            break
        else:
            continue
 

    # LCD configuration
    print("\n\nLCD CONFIGURATION\n")
    
    print("Select the LCD initial position")
    pos_vector_init = DefineModelCV.click_pos_led(image)
    print('Check the position and press ENTER')
    DefineModelCV.print_pos_led(image, pos_vector_init)
    while True:
        print("Is that the correct position? [y/n]")
        c = input()
        if(c == 'y'):
            break
        elif(c == 'n'):
            print("Select the LCD initial position")
            pos_vector = DefineModelCV.click_pos_led(image)
            print('Check the position and press ENTER')
            DefineModelCV.print_pos_led(image, pos_vector_init)
        else:
            continue

    print("Select the LCD final position")
    pos_vector_final = DefineModelCV.click_pos_led(image)
    print('Check the position and press ENTER')
    DefineModelCV.print_pos_led(image, pos_vector_final)
    while True:
        print("Is that the correct position? [y/n]")
        c = input()
        if(c == 'y'):
            break
        elif(c == 'n'):
            print("Select the LCD final position")
            pos_vector = DefineModelCV.click_pos_led(image)
            print('Check the position and press ENTER')
            DefineModelCV.print_pos_led(image, pos_vector_final)
        else:
            continue
    
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
            pos_vector = DefineModelCV.click_pos_led(image)
            print('Check the position and press ENTER')
            DefineModelCV.print_pos_led(image, pos_vector)
            while True:
                print("Is that the correct position? [y/n]")
                c = input()
                if(c == 'y'):
                    break
                elif(c == 'n'):
                    print(f"Select the led {i+1} central position")
                    pos_vector = DefineModelCV.click_pos_led(image)
                    print('Check the position and press ENTER')
                    DefineModelCV.print_pos_led(image, pos_vector)
                else:
                    continue
                

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
            pos_vector = DefineModelCV.click_pos_led(image)
            print('Check the position and press ENTER')
            DefineModelCV.print_pos_led(image, pos_vector_init)
            while True:
                print("Is that the correct position? [y/n]")
                c = input()
                if(c == 'y'):
                    break
                elif(c == 'n'):
                    print(f"Select the button {i+1} central position")
                    pos_vector = DefineModelCV.click_pos_led(image)
                    print('Check the position and press ENTER')
                    DefineModelCV.print_pos_led(image, pos_vector)
                else:
                    continue

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
            
            
            # back to menu
            if(name_model == 'q'):
                break
            
            # model doesn't exist -> new configuration
            elif(df.open_model_xml(M, name_model, M.path.get_xml_directory()) is None):
                os.system('cls') 
                print(f"{name_model} DOESN'T EXIST\n")
                print("\n\n----------------------NEW MODEL CONFIGURATION----------------------\n")

                if ( create_model_manual(M, name_model) == 0):
                    df.create_xml(M, name_model, M.path.get_xml_directory())

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

    img_path = "test_images/HMI.png"

    cap = ImageFiles([img_path])

    cap.start_capture()

    image = cap.get_image()

    cap.stop_capture()
    cap.clear_queue()

    #------------------------------------EDIT MENU------------------------------------#
    while True:
        
            os.system('cls') 
            print("What model do you want to edit?" )
            print("(to go to the menu insert q)\n" )
            name_model = input()
            
            
            # back to menu
            if(name_model == 'q'):
                return 0

            # model doesn't exist
            elif(df.open_model_xml(M, name_model, M.path.get_xml_directory()) is None):
                os.system('cls') 
                print(f"{name_model} DOESN'T EXIST\n")
                print("To go to the menu insert anything\n" )
                c = input()
            
            # model  exists
            else:
                #df.delete_xml(name_model, directory) # Delete the xml file
                index = M.index_model(name_model)

                if(index == -1):
                    return -1

                name_model = M.model[index].get_name()

                while True:
                    os.system('cls') 
                    print("-------------Edit Menu-------------\n\n")
                    print("1- Edit name model   2- Edit led\n")
                    print("3- Edit button       4- Edit LCD\n")
                    print("             5- Save")
                    print("6- Back              7- Exit\n")
                    print("\n\n----------------------------------\n")
                
                    c= input()

                    # edit name model
                    if c == '1':
                        edit_name_model(M, index)
                        name_model = M.model[index].get_name()
                            
                    # edit led
                    elif c == '2':
                        edit_led(M, name_model, index, image)
                    
                    # edit button
                    elif c == '3':
                        edit_button(M, name_model, index, image)
                    
                    # edit LCD
                    elif c == '4':
                        edit_display(M, index, image)
                    
                    # save
                    elif c == '5':
                        while True:
                            print("What version is this?\n")
                            version = input() 
                            if version.isdigit():
                                version = int(version)
                                break
                            else: 
                                continue
                        M.model[index].set_version(version)
                        df.create_xml(M, name_model, M.path.get_xml_directory())
                        n = 0
                        break
                    
                    #back
                    elif c == '6':
                        while True:
                            resp = input("Do you want to save the changes before leaving? [y/n]")
                            if (resp == 'y'):
                                df.create_xml(M, name_model, M.path.get_xml_directory())
                                break
                            elif (resp == 'n'):
                                break
                            else: 
                                continue
                        
                        return 0
                    
                    #exit
                    elif c == '7':
                        while True:
                            resp = input("Do you want to save the changes before leaving? [y/n]")
                            if (resp == "y"):
                                df.create_xml(M, name_model, M.path.get_xml_directory())
                                break
                            elif (resp == 'n'):
                                break
                            else:
                                continue

                        return -1
                    
                    

#------------------------------------EDIT NAME MODEL------------------------------------#
def edit_name_model(M: Settings, index: int):

    os.system('cls')
    print("What is the new name model?\n")
    name_model = input()
    M.model[index].set_name(name_model)
    
    os.system('cls')
    print("NAME CHANGED\n")
    print("To go to the edit menu insert anything\n")
    c = input()

#------------------------------------EDIT LED------------------------------------#
def edit_led(M: Settings, name_model, index: int, image):
    
    while True:

        os.system('cls')
        print("What led do you want to edit?")
        print("(to go to the menu insert q)\n" )
        led_name = input()

        # back to menu
        if(led_name == 'q'):
            break
        
        index_led = M.index_led_model(name_model, led_name)
        
        if (index_led is None):
            os.system('cls')
            print(f"{led_name} DOESN'T EXIST")
            print("To edit another one or go to the edit menu insert anything\n")
            c = input()
            continue

        else:
            edit_led_settings(M, index, index_led, image)

def edit_led_settings(M: Settings, index: int, index_led: int, image):
    
    while True:
        os.system('cls') 
        print("-------------Edit Led-------------\n\n")
        print("1- Name          2- Colours\n")
        print("3- Position      4- Edit menu")
        print("\n\n----------------------------------\n")
        c = input()

        # edit name
        if c=='1':
            os.system('cls') 
            print("What is the new led name?\n")
            led_name = input().strip()
            M.model[index]._leds[index_led].set_name(led_name)

            os.system('cls')
            print("LED NAME CHANGED")
            print("To continue insert anything\n")
            c= input()                   
        
        # edit colours
        elif c=='2':
            M.model[index]._leds[index_led].delete_colour()
            os.system('cls')

            while True:
                print("How many colours have the led?\n")
                n_colours = input()
                if n_colours.isdigit():
                    n_colours = int(n_colours)
                    break
            
            for i in range(0, n_colours):
                print(f"Colour {i+1} of led:")
                new_colour = input()
                M.model[index]._leds[index_led].new_colour(new_colour)
            
            os.system('cls')
            print("LED COLOURS CHANGED")
            print("To continue insert anything\n")
            c= input()

        # edit position 
        elif c=='3':
            os.system('cls') 
            print("Select the led central position")
            pos_vector = DefineModelCV.click_pos_led(image)
            print('Check the position and press ENTER')
            DefineModelCV.print_pos_led(image, pos_vector)
            while True:
                print("Is that the correct position? [y/n]")
                c = input()
                if(c == 'y'):
                    break
                elif(c == 'n'):
                    print("Select the led central position")
                    pos_vector = DefineModelCV.click_pos_led(image)
                    print('Check the position and press ENTER')
                    DefineModelCV.print_pos_led(image, pos_vector)
                else:
                    continue

            M.model[index]._leds[index_led].set_pos(pos_vector[0], pos_vector[1])

            os.system('cls')
            print("LED POSITION CHANGED")
            print("To continue insert anything\n")
            c= input()
                    
        # back to menu
        elif c == '4':
            break

#------------------------------------EDIT BUTTON------------------------------------#
def edit_button(M: Settings, name_model, index: int, image):

    while True:

        os.system('cls')
        print("What button do you want to edit?")
        print("(to go to the menu insert q)\n" )
        button_name = input()

        # back to menu
        if(button_name == 'q'):
            break
        
        index_button = M.index_button_model(name_model, button_name) 
        
        if (index_button is None):
            os.system('cls')
            print(f"{button_name} DOESN'T EXIST")
            print("To edit another one or go to the edit menu insert anything\n")
            c = input()
            continue

        else:
            while True:
                os.system('cls') 
                print("-------------Edit button-------------\n\n")
                print("1- Name          2- Position\n")
                print("      3- Edit menu")
                print("\n\n----------------------------------\n")
                c = input()

                # edit name
                if c=='1':
                    os.system('cls') 
                    print("What is the new button name?\n")
                    button_name = input()
                    M.model[index]._buttons[index_button].set_name(button_name)

                    os.system('cls')
                    print("BUTTON NAME CHANGED")
                    print("To continue insert anything\n")
                    c= input()
                    continue

                # edit position 
                elif c=='2':
                    os.system('cls') 
                    print(f"Select the button central position")
                    pos_vector = DefineModelCV.click_pos_led(image)
                    print('Check the position and press ENTER')
                    DefineModelCV.print_pos_led(image, pos_vector)
                    while True:
                        print("Is that the correct position? [y/n]")
                        c = input()
                        if(c == 'y'):
                            break
                        elif(c == 'n'):
                            print("Select the button central position")
                            pos_vector = DefineModelCV.click_pos_led(image)
                            print('Check the position and press ENTER')
                            DefineModelCV.print_pos_led(image, pos_vector)
                        else:
                            continue

                    M.model[index]._buttons[index_button].set_pos(pos_vector[0], pos_vector[1])

                    os.system('cls')
                    print("BUTTON POSTION CHANGED")
                    print("To continue insert anything\n")
                    c= input()
                
                # back to menu
                elif c == '3':
                    break

#------------------------------------EDIT LCD------------------------------------#
def edit_display(M: Settings, index: int, image):

    os.system('cls')
    print("Select the LCD initial position")
    pos_vector_init = DefineModelCV.click_pos_led(image)
    print('Check the position and press ENTER')
    DefineModelCV.print_pos_led(image, pos_vector_init)
    while True:
        print("Is that the correct position? [y/n]")
        c = input()
        if(c == 'y'):
            break
        elif(c == 'n'):
            print("Select the LCD initial position")
            pos_vector_init = DefineModelCV.click_pos_led(image)
            print('Check the position and press ENTER')
            DefineModelCV.print_pos_led(image, pos_vector_init)
        else:
            continue
    print("Select the LCD final position")
    pos_vector_final = DefineModelCV.click_pos_led(image)
    print('Check the position and press ENTER')
    DefineModelCV.print_pos_led(image, pos_vector_final)
    while True:
        print("Is that the correct position? [y/n]")
        c = input()
        if(c == 'y'):
            break
        elif(c == 'n'):
            print("Select the LCD final position")
            pos_vector = DefineModelCV.click_pos_led(image)
            print('Check the position and press ENTER')
            DefineModelCV.print_pos_led(image, pos_vector_final)
        else:
            continue
    
    dim_x = int(pos_vector_final[0]) - int(pos_vector_init[0])
    dim_y = int(pos_vector_final[1]) - int(pos_vector_init[1])
    
    M.model[index]._display.new_pos(int(pos_vector_init[0]), int(pos_vector_init[1]), dim_x, dim_y)

    os.system('cls')
    print("LCD POSITION CHANGED\n")
    print("To go to the edit menu insert anything\n")
    c = input()