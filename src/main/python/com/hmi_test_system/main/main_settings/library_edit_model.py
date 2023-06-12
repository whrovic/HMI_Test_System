import os

from data import *
from data.model.model import Model
from data.path import Path
from main.constant_main import *
from main.library import Library as Lib
from opencv.define_model_cv import DefineModelCV
from video.image_files import ImageFiles

from .menu_prints import MenuPrints as MP


class LibraryEditModel(Lib):

    
    @staticmethod
    def sett_editmenu_first():
        
        os.system('cls')

        # Get list of available models
        name_models = df.get_all_xml_file_names()
        if name_models is None:
            # TODO: Error code
            Lib.exit_input("Error path don't exist")
            return None
        elif len(name_models) == 0:
            Lib.exit_input("No available models to edit")
            return None
        
        # Choose which model to edit
        while True:

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
                continue
            else:
                return Settings.get_model(name_model)
    
    
    #------------------------------------EDIT MODEL INFO------------------------------------#
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

    #------------------------------------EDIT LED------------------------------------#
    @staticmethod
    def edit_model_led(model: Model):
        
        os.system('cls')
        # TODO: Change this
        img_path = "test_images/HMI.png"

        cap = ImageFiles([img_path])

        cap.start_capture()

        image = cap.get_image()

        cap.stop_capture()
        cap.clear_queue()

        led_name=Lib.get_input_str("What led do you want to edit?")
        if (led_name is None):
            # back to menu
            return -1
        
        led = model.get_led(led_name)
        if led is None:
            Lib.exit_input(f"{led_name} doesn't exist")
            return -1
        else:
            LibraryEditModel.edit_model_led_settings(led, image)

    @staticmethod
    def edit_model_led_settings(led: Led, image):
        #TODO: Menu choise is not here
        while True:

            MP.sett_editmenu_editled()
            menu_choice = input()

            match(menu_choice):
                # edit name
                case '1':
                    os.system('cls') 
                    led_name = Lib.get_input_str("What is the new led name?\n").strip()
                    #print("What is the new led name?\n")
                    #led_name = input().strip()
                    
                    if (led_name is not None):
                        led.set_name(led_name)
                        Lib.exit_input("LED NAME CHANGED")
                        #print("LED NAME CHANGED")
                        #print("To continue insert anything\n")
                        #menu_choice = input()           
                        # back to menu
                    else:
                        Lib.exit_input("Error to change name")
                
                # edit colours
                case '2':
                    led.delete_colours()
                    os.system('cls')

                    while True:
                        print("How many colours have the led?\n")
                        n_colours = input()
                        if n_colours.isdigit():
                            n_colours = int(n_colours)
                            break

                    led._n_colour = n_colours
                    
                    for i in range(n_colours):
                        print(f"Colour {i+1} of led:")
                        for i, color in enumerate(ListOfColors.get_list_of_colors()):
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

                    
                    os.system('cls')
                    print("LED COLOURS CHANGED")
                    print("To continue insert anything\n")
                    menu_choice = input()

                # edit position 
                case '3':
                    os.system('cls') 
                    print("Select the led central position and press ENTER")
                    pos_vector = DefineModelCV.click_pos(image)

                    led.set_pos(pos_vector[0], pos_vector[1])

                    os.system('cls')
                    print("LED POSITION CHANGED")
                    print("To continue insert anything\n")
                    menu_choice = input()
                            
                # back to menu
                case '4':
                    break

    #------------------------------------EDIT BUTTON------------------------------------#
    @staticmethod
    def edit_model_button(model: Model):

        # TODO: Change this
        img_path = "test_images/HMI.png"

        cap = ImageFiles([img_path])

        cap.start_capture()

        image = cap.get_image()

        cap.stop_capture()
        cap.clear_queue()

        while True:
            os.system('cls')
            print("What button do you want to edit?")
            print("(to go to the menu insert q)\n" )
            button_name = input()

            # back to menu
            if(button_name == 'q'):
                break
            
            button = model.get_button(button_name)            
            if (button is None):
                os.system('cls')
                print(f"{button_name} doesn't exist")
                input("Press Enter to continue...")
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
                        button.set_name(button_name)

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

                        button.set_pos(pos_vector[0], pos_vector[1])

                        os.system('cls')
                        print("BUTTON POSTION CHANGED")
                        print("To continue insert anything\n")
                        c= input()
                    
                    # back to menu
                    elif c == '3':
                        break

    #------------------------------------EDIT LCD------------------------------------#
    @staticmethod
    def edit_model_display(model: Model):
        
        # TODO: Change this
        img_path = "test_images/HMI.png"

        cap = ImageFiles([img_path])

        cap.start_capture()

        image = cap.get_image()

        cap.stop_capture()
        cap.clear_queue()

        display = model.get_display()

        os.system('cls')
        print("Select the LCD initial position and press ENTER")
        pos_vector_init= DefineModelCV.click_pos(image)
        
        print("Select the LCD final position")
        pos_vector_final= DefineModelCV.click_pos(image)
        
        dim_x = int(pos_vector_final[0]) - int(pos_vector_init[0])
        dim_y = int(pos_vector_final[1]) - int(pos_vector_init[1])
        
        display.set_new_pos(int(pos_vector_init[0]), int(pos_vector_init[1]), dim_x, dim_y)

        os.system('cls')
        print("LCD POSITION CHANGED\n")
        input("Press Enter to continue...")
    
    #---------------------------------AUXILIAR FUNCTIONS ---------------------------------#
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
    