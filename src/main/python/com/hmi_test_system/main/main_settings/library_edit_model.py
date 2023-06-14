import os

from data import *
from data.model.model import Model
from data.path import Path
from main.constant_main import *
from main.library import Library as Lib
from opencv.define_model_cv import DefineModelCV
from video.image_files import ImageFiles

from .library_color import LibraryColor as LC
from .menu_prints import MenuPrints as MP


class LibraryEditModel(Lib):

    @staticmethod
    def sett_editmenu_first():
        os.system('cls')
        # Get list of available models
        name_models = df.get_all_xml_file_names()
        if name_models is None:
            Lib.exit_input("Error path don't exist")
            return None
        elif len(name_models) == 0:
            Lib.exit_input("No available models to edit")
            return None
        
        # Choose which model to edit
        os.system('cls') 

        # Print all available models
        print("Available models:")
        for i, name in enumerate(name_models):
            print(str(i+1) + ' - ' + name)
        
        name_model=Lib.get_name_or_index("\nWhat model do you want to edit?", name_models)
        if (name_model is None):
            # back to menu
            return None
                    
        if (df.open_model_xml(name_model) is None):
            os.system('cls')
            Lib.exit_input(f"{name_model} doesn't exist\n")
            return None
        else:
            return Settings.get_model(name_model)
    

    # Info
    @staticmethod
    def edit_model_info(model: Model):
        os.system('cls')
        
        while True:
            os.system('cls')
            print("What is the new name model?\n")
            name_model = str(input())
            name_model = name_model.strip()
            if(len(name_model)>0):
                os.rename(Path.get_model_images_directory()+'/'+model.get_name()+'_chr.png', Path.get_model_images_directory()+'/'+name_model+'_chr.png')
                os.rename(Path.get_model_images_directory()+'/'+model.get_name()+'_pal.png', Path.get_model_images_directory()+'/'+name_model+'_pal.png')
                model.set_name(name_model)
                break
            else:
                continue
        

        #TODO: possibilitate to change just some parameters 
        board = Lib.until_find_str("What is the new board:")
        if board is None: return -1
        option = Lib.until_find_str("What is the new option:")
        if option is None: return -1
        revision = Lib.until_find_str("What is the new revision:")
        if revision is None: return -1
        edition = Lib.until_find_str("What is the new edition:")
        if edition is None: return -1
        dsp_type = Lib.until_find_str("What is the new display type:")
        if dsp_type is None: return -1
        boot_version = Lib.until_find_str("What is the new boot loader version:")
        if boot_version is None: return -1
        boot_date = Lib.until_find_str("What is the new boot loader date:")
        if boot_date is None: return -1

        info = Info(board, option, revision, edition, dsp_type)
        model.set_info(info)

        boot_info = BootLoaderInfo(boot_version, boot_date)
        model.set_boot_loader_info(boot_info)
        
        os.system('cls')
        Lib.exit_input("INFO CHANGED")
        return 0


    # LED
    @staticmethod
    def sett_editmenu_editled_first(model: Model):
        
        os.system('cls')
        image = DefineModelCV.get_leds_image()

        led_name=Lib.get_input_str("What led do you want to edit?")
        if (led_name is None):
            # back to menu
            return None, None
        
        led = model.get_led(led_name)
        if led is None:
            Lib.exit_input(f"{led_name} doesn't exist")
            return None, None
        else:
            return led, image

    @staticmethod
    def edit_menu_edit_led_name(led: Led):
        os.system('cls') 
        led_name = Lib.get_input_str("What is the new led name?\n").strip()
                    
        if (led_name is not None):
            led.set_name(led_name)
            Lib.exit_input("LED NAME CHANGED")
            return 0
        else:
            Lib.exit_input("Error to change name")
            return -1

    @staticmethod
    def edit_menu_edit_led_colours(led: Led):
        os.system('cls')
        
        n_colours = Lib.until_find_int("How many colours have the led?")
        if n_colours is None: 
            return -1

        led.set_n_Colour(n_colours)
        if (led.get_n_Colour() != n_colours):
            Lib.exit_input("Error: not possible to change")
            return -1
           
        for i in range(n_colours):
            print(f"Colour {i+1} of led:")
            for i, color in enumerate(ListOfColors.get_list_of_colors()):
                print(f'{i+1} - {color.get_name()}')
            
            new_color = LC.sett_color_editcolor_first()
            if new_color is None: return 0
            
            led.new_colour(new_color)
                    
        Lib.exit_input("LED COLOURS CHANGED")

    @staticmethod
    def edit_menu_edit_led_position(led: Led, image):
        os.system('cls') 
        print("Select the led central position and press ENTER")
        pos_vector = DefineModelCV.click_pos(image)

        led.set_pos(pos_vector[0], pos_vector[1])

        Lib.exit_input("LED POSITION CHANGED")



    # Button
    @staticmethod
    def sett_editmenu_editbutton_first(model: Model):
        
        os.system('cls')
        image = DefineModelCV.get_buttons_image()

        
        button_name = Lib.get_input_str("What button do you want to edit?")

        if (button_name is None):
            # back to menu
            return None, None
        
        button = model.get_button(button_name)
        if button is None:
            Lib.exit_input(f"{button_name} doesn't exist")
            return None, None
        else:
            return button, image  

    @staticmethod
    def edit_model_edit_button_name(button: Button):
        os.system('cls') 
        print("What is the new button name?")
        button_name = Lib.get_input_str("What is the new button name?\n").strip()
                    
        if (button_name is not None):
            button.set_name(button_name)
            Lib.exit_input("BUTTON NAME CHANGED")
            return 0
        else:
            Lib.exit_input("Error to change name")
            return -1

    @staticmethod
    def edit_model_edit_button_position(image, button: Button):
        os.system('cls') 
        print("Select the button central position and press ENTER")
        pos_vector = DefineModelCV.click_pos(image)

        button.set_pos(pos_vector[0], pos_vector[1])

        Lib.exit_input("BUTTON POSITION CHANGED")


    # Display
    @staticmethod
    def edit_model_display(model: Model):
        
        os.system('cls')
        name_model = model.get_name()

        # Gets the image of the display
        display_img = DefineModelCV.get_display_image()
        if display_img is None: return -1
        
        # Get reference images
        chr_ref_img, pal_ref_img = DefineModelCV.get_reference_display_images()
        if chr_ref_img is None or pal_ref_img is None: return -1
        
        # Save reference images
        if not DefineModelCV.write_reference_image_to_file(chr_ref_img, name_model+'_chr'):
            input("Couldn't write chr img")
            return -1
        if not DefineModelCV.write_reference_image_to_file(pal_ref_img, name_model+'_pal'):
            input("Couldn't write pal img")
            return -1

        os.system('cls')
        input("Press Enter to continue...")
    


    # Save
    @staticmethod
    def save_changes(model: Model):
        while True:
            resp = input("Do you want to save the changes before leaving? [y/n] ")
            if (resp.lower() == 'y'):
                df.create_xml(model)
                break
            elif (resp.lower() == 'n'):
                break
            else: 
                continue
    