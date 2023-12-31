import os
import xml.etree.ElementTree as ET

from data import *
from data.model.model import Model
from main.constant_main import *
from main.library import Library as L
from main.library import Library as Lib
from opencv.define_model_cv import DefineModelCV


class LibraryNewModel(Lib):
    
    @staticmethod
    def new_model_create():
        while True:
            os.system('cls') 
                
            name_model = Lib.get_input_str("Insert the name of the new model:")
            if (name_model is None):
                # back to menu
                break
            
            # model doesn't exist -> new configuration
            elif (df.open_model_xml(name_model) is None):
                if (LibraryNewModel._create_model_manually(name_model) == 0):
                    model = Settings.get_model(name_model)
                    if model is None: return -1
                    
                    df.create_xml(model)
                    os.system('cls')
                    Lib.exit_input(f"The model {name_model} added successfully")
                    break
                else:
                    os.system('cls')
                    Lib.exit_input(f"The model {name_model} wasn't created")
                    break
            # model already exists
            else:
                os.system('cls')
                Lib.exit_input(f"The name {name_model} is already in use")
                break
    
    @staticmethod
    def new_model_import_xml():
        while True:
            os.system('cls') 
                
            name_model = Lib.get_input_str("Insert the name of the new model:")
            if (name_model is None):
                # back to menu
                return -1
            
            # model doesn't exist -> new configuration
            elif (df.open_model_xml(name_model) is None):
                os.system('cls') 
                #print("Insert the path of the XML file")
                #directory = str(input())
                directory = Lib.ask_directory()
                if directory is None:
                    Lib.exit_input("Path doesn't exits")
                    return -1

                if (LibraryNewModel._create_model_import_xml(directory, name_model) == 0):
                    model = Settings.get_model(name_model)
                    if model is None: return -1
                    df.create_xml(model)
                    os.system('cls')
                    Lib.exit_input(f"{name_model} IS ADDED \n\n")
                    return 0
                else:
                    os.system('cls')
                    Lib.exit_input(f"{name_model} IS NOT ADDED \n\n")
                    return -1
            # model already exists
            else:
                os.system('cls')
                Lib.exit_input(f"{name_model} ALREADY EXISTS\n\n")
                return -1
    
    @staticmethod
    def _create_model_manually(name_model):
        
        os.system('cls') 
        print("----------------------NEW MODEL CONFIGURATION----------------------\n")
        
        # Board Info Configuration
        print("BOARD INFO CONFIGURATION\n")

        board = Lib.until_find_str("Board: ")
        if board is None: return -1
        option = Lib.until_find_str("Option: ")
        if option is None: return -1
        revision = Lib.until_find_str("Revision: ")
        if revision is None: return -1
        edition = Lib.until_find_str("Edition: ")
        if edition is None: return -1
        lcd_type = Lib.until_find_str("LCD Type: ")
        if lcd_type is None: return -1

        info = Info(board, option, revision, edition, lcd_type)

        # Bootloader Info Configuration
        print("\n\nBOOTLOADER INFO CONFIGURATION\n")

        boot_version = Lib.until_find_str("Boot loader version: ")
        if boot_version is None: return -1
        boot_date = Lib.until_find_str("Boot loader date: ")
        if boot_date is None: return -1
        
        boot_info = BootLoaderInfo(boot_version, boot_date)

        # LCD configuration   
        print("\n\nLCD CONFIGURATION\n")

        # Inform user about the need of the camera
        Lib.exit_input("Before continuing, please make sure that the display camera is ready and the display tests are ready to start")

        # Gets the image of the display
        display_img = DefineModelCV.get_display_image()
        if display_img is None: return -1
        
        # Get reference images
        chr_ref_img, pal_ref_img = DefineModelCV.get_reference_display_images()
        if chr_ref_img is None or pal_ref_img is None: return -1

        display = Display('display')

        n_buttons = Lib.until_find_int("Number of buttons: ")
        if (n_buttons) == -1: return -1
        n_leds = Lib.until_find_int("Number of leds: ")
        if (n_leds) == -1: return -1

        # Add model
        new_model = Model(name_model, n_leds, n_buttons, display, info, boot_info)
    
        # buttons configuration
        print("\n\nBUTTONS CONFIGURATION\n")
        input("Please make sure that the camera is positioned in the leds board...")

        if(n_buttons > 0):
            
            b_posit = input("Do you want to also configure the buttons position [y|n]?")
            b_posit = bool(b_posit.lower() == 'y')
            if b_posit:
                # Get the image for the buttons
                buttons_img = DefineModelCV.get_buttons_image()
                if buttons_img is None: return -1

            for i in range(0, n_buttons):
                print(f"\nButton {i+1} name: ")
                button_name = input()
                
                if b_posit:
                    print(f"Select the button {button_name}'s central position and press ENTER")
                    pos_vector= DefineModelCV.click_pos(buttons_img)
                    if pos_vector is None: return -1
                else:
                    pos_vector = [0, 0]

                new_model.set_button(Button(button_name, int(pos_vector[0]), int(pos_vector[1])))
        else:
            print("\nModel doesn't have buttons\n")

        # leds configuration
        print("\n\nLEDS CONFIGURATION\n")

        if(n_leds > 0):
            
            count = 0
            while True:

                if count >= 5: return -1

                # Get the image for the leds
                leds_img = DefineModelCV.get_leds_image()
                if leds_img is None: return -1

                leds_img_detect = DefineModelCV.get_leds_image(True)
                if leds_img_detect is None: return -1
                leds_coordinates = DefineModelCV.detect_pos_leds(leds_img, leds_img_detect)
                
                print(f"The system detected {len(leds_coordinates)} Leds instead of {n_leds} Leds")

                if len(leds_coordinates) < n_leds:
                    c = input("Do you want to add the remaining ones manually [y|n]? ")
                    
                    if c.lower() == 'y':
                        print("First, the system will show you the leds already positioned")
                        c = input("Press ENTER to continue and press in the position of the remaining leds, or 'q' to cancel")
                        if c == 'q': return -1
                        for i in range(len(leds_coordinates), n_leds):
                            DefineModelCV.show_coordinates(leds_img, leds_coordinates)
                            coord = DefineModelCV.click_pos(leds_img)
                            if coord is None: return -1
                            leds_coordinates.append(coord)
                        break
                elif len(leds_coordinates) > n_leds:
                    L.exit_input(f"The system detected {len(leds_coordinates)} instead of {n_leds} LEDs\nPlease, check the environment luminosity and retry later")
                else:
                    break

                c = input("Do you want to try again [y|n]?")
                if c.lower() != 'y': return -1

            leds_coordinates = DefineModelCV.ask_leds_order(leds_img, leds_coordinates)

            input("For the next step, check which LED is currently being configured and press ENTER...")

            for i in range(len(leds_coordinates)):

                DefineModelCV.show_coordinates(leds_img, [leds_coordinates[i],])

                led_name = 'L' + str(i+1)
                n_colours=Lib.until_find_int(f"How many colours have the led {i+1}?")
                if (n_colours) == -1: return -1

                led = Led(led_name, n_colours, int(leds_coordinates[i][0]), int(leds_coordinates[i][1]))

                for j in range(0, n_colours):
                    print(f"Colour {j+1} of led {i+1}:")
                    for i , color in enumerate(ListOfColors.get_list_of_colors()):
                        print(f'{i+1} - {color.get_name()}')
                    new_colour = Lib.get_name_or_index("Insert the index or the name of the color", [c.get_name() for c in ListOfColors.get_list_of_colors()])
                    if new_colour is None: return -1
                    led.new_colour(ListOfColors.get_color(new_colour))
                               
                new_model.set_led(led)
        else:
            print("\nModel doesn't have leds\n")
        
        # Save reference images
        if not DefineModelCV.write_reference_image_to_file(chr_ref_img, name_model+'_chr'):
            input("Couldn't write chr img")
            return -1
        if not DefineModelCV.write_reference_image_to_file(pal_ref_img, name_model+'_pal'): 
            input("Couldn't write pal img")
            return -1
        

        # Add model to settings
        Settings.add_model(new_model)

        return 0

    @staticmethod
    def _create_model_import_xml(directory: str, name_model: str):
        
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
            
            new_model = Settings.new_model(name, int(n_leds), int(n_buttons), LCD, INFO, BOOT_INFO)

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
                
                new_model.set_led(led)


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
                new_model.set_button(button)

            return 0
        
        else:
            return -1
