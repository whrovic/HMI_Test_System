import os
import xml.etree.ElementTree as ET

from data import *
from data.hardware_settings.parameter import Parameter
from data.model.model import Model
from main.constant_main import *
from main.library import Library as L
from opencv.define_model_cv import DefineModelCV


class LibraryNewModel:
    
    @staticmethod
    def new_model_mannually():
        #------------------------------------ADD NEW MODEL------------------------------------#
        while True:
            os.system('cls') 
                
            name_model = L.get_input("Insert the name of the new model:")
            if (name_model is None):
                # back to menu
                break
            
            # model doesn't exist -> new configuration
            elif (df.open_model_xml(name_model) is None):
                os.system('cls') 
                print("\n\n----------------------NEW MODEL CONFIGURATION----------------------\n")

                if (LibraryNewModel.create_model_manually(name_model) == 0):
                    df.create_xml(name_model)
                    os.system('cls')
                    L.exit_input(f"{name_model} IS ADDED \n\n")
                    break
                else:
                    os.system('cls')
                    L.exit_input(f"{name_model} IS NOT ADDED \n\n")
                    break
            # model already exists
            else:
                os.system('cls')
                L.exit_input(f"{name_model} ALREADY EXISTS\n\n")
                break
    
    @staticmethod
    def new_model_import_xml():
        
        #------------------------------------ADD NEW MODEL------------------------------------#
        while True:
            os.system('cls') 
                
            name_model = L.get_input("Insert the name of the new model:")
            if (name_model is None):
                # back to menu
                break
            
            # model doesn't exist -> new configuration
            elif (df.open_model_xml(name_model) is None):
                os.system('cls') 
                print("Insert the path of the XML file")
                directory = str(input())

                if (LibraryNewModel.create_model_import_xml(directory, name_model) == 0):
                    df.create_xml(name_model)
                    os.system('cls')
                    L.exit_input(f"{name_model} IS ADDED \n\n")
                    break
                else:
                    os.system('cls')
                    L.exit_input(f"{name_model} IS NOT ADDED \n\n")
                    break
            # model already exists
            else:
                os.system('cls')
                L.exit_input(f"{name_model} ALREADY EXISTS\n\n")
                break
    
    @staticmethod
    def create_model_manually(name_model):

        # Board Info Configuration
        print("BOARD INFO CONFIGURATION\n")       

        board = L.until_find_str("Board: ")
        if board is None: return -1
        option = L.until_find_str("Option: ")
        if option is None: return -1
        revision = L.until_find_str("Revision: ")
        if revision is None: return -1
        edition = L.until_find_str("Edition: ")
        if edition is None: return -1
        lcd_type = L.until_find_str("LCD Type: ")
        if lcd_type is None: return -1

        info = Info(board, option, revision, edition, lcd_type)

        # Bootloader Info Configuration
        print("\n\nBOOTLOADER INFO CONFIGURATION\n")

        boot_version = L.until_find_str("Boot loader version: ")
        if boot_version is None: return -1
        boot_date = L.until_find_str("Boot loader date: ")
        if boot_date is None: return -1
        
        boot_info = BootLoaderInfo(boot_version, boot_date)     

        # LCD configuration
        print("\n\nLCD CONFIGURATION\n")

        print("Before continuing, please make sure that the display camera is ready")
        input("Press Enter to continue...")

        # Gets the image of the display
        display_img = DefineModelCV.get_display_board_image()

        print("Select the LCD initial position and press Enter to continue...")
        pos_vector_init = DefineModelCV.click_pos(display_img)
        
        print("Select the LCD final position and press Enter to continue...")
        pos_vector_final= DefineModelCV.click_pos(display_img)
        
        dim_x = int(pos_vector_final[0]) - int(pos_vector_init[0])
        dim_y = int(pos_vector_final[1]) - int(pos_vector_init[1])
        display = Display('display', int(pos_vector_init[0]) , int(pos_vector_init[1]) , dim_x, dim_y)


        n_buttons = L.until_find_int("Number of buttons: ")
        if (n_buttons) == -1: return -1
        n_leds = L.until_find_int("Number of leds: ")
        if (n_leds) == -1: return -1

        # add model
        new_model = Model(name_model, n_leds, n_buttons, display, info, boot_info)
        
        # buttons configuration
        print("\n\nBUTTONS CONFIGURATION\n")

        # Get the image for the buttons
        buttons_img = DefineModelCV.get_leds_board_image()

        if(n_buttons > 0):
            for i in range(0, n_buttons):
                print(f"\nButton {i+1} name: ")
                button_name = input()
                print(f"Select the button {i+1} central position and press ENTER")
                pos_vector= DefineModelCV.click_pos(buttons_img)

                new_model.set_button(Button(button_name, int(pos_vector[0]), int(pos_vector[1])))
        else:
            print("\nModel doesn't have buttons\n")

        # leds configuration
        print("\n\nLEDS CONFIGURATION\n")

        parameters_leds = Parameter(1080, 720, 0.0, 30, 0.0, -11, 0, 0.0, 3760, 80, 128, 255, 128)
        leds_img = DefineModelCV.get_leds_board_image(parameters_leds)

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
                pos_vector= DefineModelCV.click_pos(leds_img)
                    

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
                    
                new_model.set_led(led)
        else:
            print("\nModel doesn't have leds\n")

        # Add model to settings        
        Settings.add_model(new_model)

        return 0

    @staticmethod
    def create_model_import_xml(directory: str, name_model: str):
        
        try:
            tree = ET.parse(directory)
        except:
            return -1

        model = tree.getroot()
        name = model.find('name')
        name = str(name.text.strip())
        if(len(name) <= 0):
            return -1
        
        if(name == name_model):
            n_leds = model.find('n_leds')
            n_leds = str(n_leds.text.strip())
            if not n_leds.isdigit():
                return -1
            
            n_buttons = model.find('n_buttons')
            n_buttons = str(n_buttons.text.strip())
            if not n_buttons.isdigit():
                return -1
            
            display = model.find('display')
            display_name = display.find('display_name')
            display_name = str(display_name.text.strip())
            if(len(display_name) <= 0):
                return -1
            
            display_x = display.find('display_x')
            display_x = str(display_x.text.strip())
            if not display_x.isdigit():
                return -1
            
            display_y = display.find('display_y')
            display_y = str(display_y.text.strip())
            if not display_y.isdigit():
                return -1
            
            display_dimx = display.find('display_dimx')
            display_dimx = str(display_dimx.text.strip())
            if not display_dimx.isdigit():
                return -1
            
            display_dimy = display.find('display_dimy')
            display_dimy = str(display_dimy.text.strip())
            if not display_dimy.isdigit():
                return -1
            
            LCD = Display(display_name, int(display_x), int(display_y), int(display_dimx), int(display_dimy))

            info = model.find('info')
            info_board = info.find('board')
            info_board = str(info_board.text.strip())
            if(len(info_board) <= 0):
                return -1
            
            info_option = info.find('option')
            info_option = str(info_option.text.strip())
            if(len(info_option) <= 0):
                return -1
            
            info_revision = info.find('revision')
            info_revision = str(info_revision.text.strip())
            if(len(info_revision) <= 0):
                return -1
            
            info_edition = info.find('edition')
            info_edition = str(info_edition.text.strip())
            if(len(info_edition) <= 0):
                return -1
            
            info_lcd_type = info.find('lcd_type')
            info_lcd_type = str(info_lcd_type.text.strip())
            if(len(info_lcd_type) <= 0):
                return -1
            
            INFO = Info(info_board, info_option, info_revision, info_edition, info_lcd_type)

            boot_info = model.find('boot_loader_info')
            boot_version = boot_info.find('version')
            boot_version = str(boot_version.text.strip())
            if(len(boot_version) <= 0):
                return -1
            
            boot_date = boot_info.find('date')
            boot_date = str(boot_date.text.strip())
            if(len(boot_date) <= 0):
                return -1
            
            BOOT_INFO = BootLoaderInfo(boot_version, boot_date)
            
            Settings.new_model(name, int(n_leds), int(n_buttons), LCD, INFO, BOOT_INFO)
            index = Settings.index_model(name)

            leds = model.find('leds')
            for i in range(0, int(n_leds)):
                led_name = leds.find(f'led{i+1}_name')
                led_name = str(led_name.text.strip())
                if(len(led_name) <= 0):
                    return -1
                
                led_nColour = leds.find(f'led{i+1}_nColour')
                led_nColour = str(led_nColour.text.strip())
                if not led_nColour.isdigit():
                    return -1

                led_x = leds.find(f'led{i+1}_x')
                led_x = str(led_x.text.strip())
                if not led_x.isdigit():
                    return -1
                
                led_y = leds.find(f'led{i+1}_y')
                led_y = str(led_y.text.strip())
                if not led_y.isdigit():
                    return -1
                 
                led = Led(led_name, int(led_nColour), int(led_x), int(led_y))
                
                leds_colours = leds.find(f'led{i+1}_colours')
                for j in range(0, int(led_nColour)):   
                    led_colour = leds_colours.find(f'led{i+1}_colour{j+1}')
                    led_colour = str(led_colour.text.strip())
                    if(len(led_colour) <= 0):
                        return -1
                    
                    led.new_colour(ListOfColors.get_color(led_colour))
                
                Settings.model[index].set_led(led) 


            buttons = model.find('buttons')
            for i in range(0, int(n_buttons)):
                button_name = buttons.find(f'button{i+1}_name')
                button_name = str(button_name.text.strip())
                if(len(button_name) <= 0):
                    return -1
                
                button_x = buttons.find(f'button{i+1}_x')
                button_x = str(button_x.text.strip())
                if not button_x.isdigit():
                    return -1
                
                button_y = buttons.find(f'button{i+1}_y')
                button_y = str(button_y.text.strip())
                if not button_y.isdigit():
                    return -1
                
                button = Button(button_name, int(button_x), int(button_y))
                Settings.model[index].set_button(button)

            return 0
        
        else:
            return -1
    