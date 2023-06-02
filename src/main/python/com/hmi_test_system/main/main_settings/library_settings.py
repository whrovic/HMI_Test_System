'''from data.color.list_of_colors import ListOfColors
from data.define_and_fill_model import DefineAndFillModel as df
from data.model.boot_loader_info import BootLoaderInfo
from data.model.button import Button
from data.model.display import Display
from data.model.info import Info
from data.model.led import Led
from data.settings import Settings
'''
import os

from data import *
from .menu_prints import MenuPrints as MP
from opencv.define_model_cv import DefineModelCV
from video.image_files import ImageFiles
from main.constant_main import *

class LibrarySettings:
    def edit_camara_settings(M: Settings):
        pass

    def edit_SP_settings(M: Settings):
        pass


    def add_models(M: Settings):
        #------------------------------------ADD NEW MODEL------------------------------------#
        while True:
            os.system('cls') 
            print("Insert the name of the new model:" )
            #print("(to go to the menu insert q)\n" )
            name_model = input('Write \'q\' to back to menu  ')
            
            # back to menu
            if(name_model == 'q'):
                break
            
            # model doesn't exist -> new configuration
            elif(df.open_model_xml(M, name_model) is None):
                os.system('cls') 
                print(f"{name_model} DOESN'T EXIST\n")
                print("\n\n----------------------NEW MODEL CONFIGURATION----------------------\n")

                if ( LibrarySettings.create_model_manual(M, name_model) == 0):
                    df.create_xml(M, name_model)
                    os.system('cls') 
                    print(f"{name_model} IS ADDED \n\n")
                    #print("To go to the menu insert anything\n")
                    #c = input()
                    c = input('Press Enter')
                    break
                else:
                    os.system('cls') 
                    print(f"{name_model} IS NOT ADDED \n\n")
                    c = input('Press Enter')
                    break
            # model already exists
            else:
                os.system('cls') 
                print(f"{name_model} ALREADY EXISTS\n\n")
                c = input('Press Enter')
                break

    def create_model_manual(M: Settings, name_model):

        img_path = "test_images/HMI.png"

        cap = ImageFiles([img_path])

        cap.start_capture()

        image = cap.get_image()

        cap.stop_capture()
        cap.clear_queue()

        n_buttons = LibrarySettings._until_find_int("Number of buttons: ")
        if (n_buttons) == -1:
            return -1
        
        n_leds = LibrarySettings._until_find_int("Number of leds: ")
        if (n_leds) == -1:
            return -1

        # Info configuration
        print("\n\nINFO CONFIGURATION\n")       

        board = LibrarySettings._until_find_str("Board:")
        option = LibrarySettings._until_find_str("Option:")
        revision = LibrarySettings._until_find_str("Revision:")
        edition = LibrarySettings._until_find_str("Edition:")
        boot_version = LibrarySettings._until_find_str("Boot loader version:")
        boot_date = LibrarySettings._until_find_str("Boot loader date:")

        info = Info(board, option, revision, edition)
        boot_info = BootLoaderInfo(boot_version, boot_date)
    

        # LCD configuration
        print("\n\nLCD CONFIGURATION\n")
        
        print("Select the LCD initial position and press ENTER")
        pos_vector_init = DefineModelCV.click_pos(image)
        

        print("Select the LCD final position and press ENTER")
        pos_vector_final= DefineModelCV.click_pos(image)
        
        dim_x = int(pos_vector_final[0]) - int(pos_vector_init[0])
        dim_y = int(pos_vector_final[1]) - int(pos_vector_init[1])
        display = Display('display', int(pos_vector_init[0]) , int(pos_vector_init[1]) , dim_x, dim_y)

        # add model 
        M.new_model(name_model, n_leds, n_buttons, display, info, boot_info)

        index = M.index_model(name_model)


        # model exists 
        if(index != -1):
            
            # leds configuration
            print("\n\nLEDS CONFIGURATION\n")
            if(n_leds > 0):
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

                    print(f"Select the led {i+1} central position and press ENTER")
                    pos_vector= DefineModelCV.click_pos(image)
                        

                    led = Led(led_name, n_colours, int(pos_vector[0]), int(pos_vector[1]))
                    for j in range(0, n_colours):
                        print(f"Colour {j+1} of led {i+1}:")
                        for i , color in enumerate(ListOfColors.get_list_of_colors()):
                            print(f'{i+1} - {color.get_name()}')
                        while True:
                            print('Type which number you want')
                            new_colour = input()
                            if new_colour.isdigit():
                                new_colour = int(new_colour)
                                led.new_colour(ListOfColors.get_color_index(new_colour-1))
                                break
                            else:
                                continue
                        
                    
                    M.model[int(index)].set_led(led)
            else:
                print("\nModel doesn't have leds\n")


            # buttons configuration
            print("\n\nBUTTONS CONFIGURATION\n")
            if(n_buttons > 0):
                for i in range(0, n_buttons):
                    print(f"\nButton {i+1} name: ")
                    button_name = input()
                    print(f"Select the button {i+1} central position and press ENTER")
                    pos_vector= DefineModelCV.click_pos(image)

                    M.model[int(index)].set_button(Button(button_name, int(pos_vector[0]), int(pos_vector[1])))
            else:
                print("\nModel doesn't have buttons\n")

            
            return 0
        

        # model doesn't exist
        else:
            print("ERROR - Model creation failed")
            M.delete_model(name_model)
            return -1

    def _until_find_str(print_str: str):
        while True:
            print(print_str)
            board = str(input()) 
            board = board.strip()
            if (len(board) > MIN_LEN_STRING):
                break
            else:
                continue
        return board

    def _until_find_int(print_str: str):
        while True:
            count = 0
            print(print_str)
            value_input = input()    
            if value_input.isdigit():
                value_input = int(value_input)
                break
            elif (count > NTIMEOUT_LIBRARY_SETTINGS):
                return -1
            else: 
                count +=1
                continue
        return value_input


    def edit_model(M: Settings):

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
                #print("(to go to the menu insert q)\n" )
                #name_model = input()
                name_model = input('Write \'q\' to back to menu  ')
                
                # back to menu
                if(name_model == 'q'):
                    return 0

                # model doesn't exist
                elif(df.open_model_xml(M, name_model) is None):
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

                    #TODO: not good pratic while inside while
                    while True:
                        MP.edit_menu()                
                        menu_choice = input()

                        # edit name model
                        if menu_choice == '1':
                            LibrarySettings.edit_model_info(M, index)
                            name_model = M.model[index].get_name()
                                
                        # edit led
                        elif menu_choice == '2':
                            LibrarySettings.edit_led(M, name_model, index, image)
                        
                        # edit button
                        elif menu_choice == '3':
                            LibrarySettings.edit_button(M, name_model, index, image)
                        
                        # edit LCD
                        elif menu_choice == '4':
                            LibrarySettings.edit_display(M, index, image)
                        
                        # save
                        elif menu_choice == '5':
                            while True:
                                print("What version is this?\n")
                                version = input() 
                                if version.isdigit():
                                    version = int(version)
                                    break
                                else: 
                                    continue
                            M.model[index].set_version(version)
                            df.create_xml(M, name_model)
                            n = 0
                            break
                        
                        #back
                        elif menu_choice == '6':
                            while True:
                                resp = input("Do you want to save the changes before leaving? [y/n]")
                                if (resp == 'y'):
                                    df.create_xml(M, name_model)
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
                                    df.create_xml(M, name_model)
                                    break
                                elif (resp == 'n'):
                                    break
                                else:
                                    continue

                            return -1
                        
                        
    #------------------------------------EDIT MODEL INFO------------------------------------#
    def edit_model_info(M: Settings, index: int):

        while True:
            os.system('cls')
            print("What is the new name model?\n")
            name_model = str(input())
            name_model = name_model.strip()
            if(len(name_model)>0):
                M.model[index].set_name(name_model)
                break
            else:
                continue
        

        while True:
            os.system('cls')
            print("What is the new board:")
            board = str(input())       # Board of model
            board = board.strip()
            if (len(board) > 0):
                break
            else:
                continue


        while True:
            os.system('cls')
            print("What is the new option:")
            option = str(input())       # Option of model
            option = option.strip()
            if (len(option) > 0):
                break
            else:
                continue

        while True:
            os.system('cls')
            print("What is the new revision:")
            revision = str(input())       # Revision of model
            revision = revision.strip()
            if (len(revision) > 0):
                break
            else:
                continue

        while True:
            os.system('cls')
            print("What is the new edition:")
            edition = str(input())       # Edition of model
            edition = edition.strip()
            if (len(edition) > 0):
                break
            else:
                continue

        while True:
            print("What is the new boot loader version:")
            boot_version = str(input())       # boot loader boot_version of model
            boot_version = boot_version.strip()
            if (len(boot_version) > 0):
                break
            else:
                continue

        while True:
            print("What is the new boot loader date:")
            boot_date = str(input())       # boot loader boot_date of model
            boot_date = boot_date.strip()
            if (len(boot_date) > 0):
                break
            else:
                continue

        info = Info(board, option, revision, edition)
        M.model[index].set_info(info)

        boot_info = BootLoaderInfo(boot_version, boot_date)
        M.model[index].set_boot_loader_info(boot_info)

        
        os.system('cls')
        print("INFO CHANGED\n")
        print("To go to the edit menu insert anything\n")
        c = input()


    #------------------------------------EDIT LED------------------------------------#
    def edit_led_settings(M: Settings, index: int, index_led: int, image):
        while True:
            MP.edit_led()
            menu_choice = input()

            # edit name
            if menu_choice == '1':
                os.system('cls') 
                print("What is the new led name?\n")
                led_name = input().strip()
                M.model[index]._leds[index_led].set_name(led_name)

                os.system('cls')
                print("LED NAME CHANGED")
                print("To continue insert anything\n")
                menu_choice = input()                   
            
            # edit colours
            elif menu_choice == '2':
                M.model[index]._leds[index_led].delete_colours()
                os.system('cls')

                while True:
                    print("How many colours have the led?\n")
                    n_colours = input()
                    if n_colours.isdigit():
                        n_colours = int(n_colours)
                        break
                
                for i in range(0, n_colours):
                    print(f"Colour {i+1} of led:")
                    for i , color in enumerate(ListOfColors.get_list_of_colors()):
                        print(f'{i+1} - {color.get_name()}')
                    while True:
                        print('Type which number you want')
                        new_colour = input()
                        if new_colour.isdigit():
                            new_colour = int(new_colour)
                            M.model[index]._leds[index_led].new_colour(ListOfColors.get_color(new_colour-1))
                            break
                        else:
                            continue

                
                os.system('cls')
                print("LED COLOURS CHANGED")
                print("To continue insert anything\n")
                menu_choice = input()

            # edit position 
            elif menu_choice =='3':
                os.system('cls') 
                print("Select the led central position and press ENTER")
                pos_vector= DefineModelCV.click_pos(image)

                M.model[index]._leds[index_led].set_pos(pos_vector[0], pos_vector[1])

                os.system('cls')
                print("LED POSITION CHANGED")
                print("To continue insert anything\n")
                menu_choice = input()
                        
            # back to menu
            elif menu_choice == '4':
                break

    def edit_led(M: Settings, name_model, index: int, image):
        
        while True:

            os.system('cls')
            print("What led do you want to edit?")
            print("(to go to the menu insert q)\n" )
            led_name = input()

            # back to menu
            if(led_name == 'q'):
                break
            
            index_led = M.index_led(name_model, led_name)
            
            if (index_led is None):
                os.system('cls')
                print(f"{led_name} DOESN'T EXIST")
                print("To edit another one or go to the edit menu insert anything\n")
                c = input()
                continue

            else:
                LibrarySettings.edit_led_settings(M, index, index_led, image)


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
            
            index_button = M.index_button(name_model, button_name) 
            
            if (index_button is None):
                os.system('cls')
                print(f"{button_name} DOESN'T EXIST")
                print("To edit another one or go to the edit menu insert anything\n")
                c = input()
                continue

            else:
                while True:
                    MP.edit_button()
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
                        print(f"Select the button central position and press ENTER")
                        pos_vector= DefineModelCV.click_pos(image)

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
        print("Select the LCD initial position and press ENTER")
        pos_vector_init= DefineModelCV.click_pos(image)
        
        print("Select the LCD final position")
        pos_vector_final= DefineModelCV.click_pos(image)
        
        dim_x = int(pos_vector_final[0]) - int(pos_vector_init[0])
        dim_y = int(pos_vector_final[1]) - int(pos_vector_init[1])
        
        M.model[index]._display.new_pos(int(pos_vector_init[0]), int(pos_vector_init[1]), dim_x, dim_y)

        os.system('cls')
        print("LCD POSITION CHANGED\n")
        print("To go to the edit menu insert anything\n")
        c = input()