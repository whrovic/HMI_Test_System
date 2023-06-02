
import os

from data import *
from main.constant_main import *
from main.library import Library as L
from opencv.define_model_cv import DefineModelCV
from video.image_files import ImageFiles

from .menu_prints import MenuPrints as MP


class LibraryNewModel:
    def create_model_manual(M: Settings, name_model):

        img_path = "test_images/HMI.png"

        cap = ImageFiles([img_path])

        cap.start_capture()

        image = cap.get_image()

        cap.stop_capture()
        cap.clear_queue()

        n_buttons = L.until_find_int("Number of buttons: ")
        if (n_buttons) == -1: return -1
        n_leds = L.until_find_int("Number of leds: ")
        if (n_leds) == -1: return -1

        # Info configuration
        print("\n\nINFO CONFIGURATION\n")       

        board = L.until_find_str("Board:")
        if (board) == None: return -1
        option = L.until_find_str("Option:")
        if (option) == None: return -1
        revision = L.until_find_str("Revision:")
        if (revision) == None: return -1
        edition = L.until_find_str("Edition:")
        if (edition) == None: return -1
        boot_version = L.until_find_str("Boot loader version:")
        if (boot_version) == None: return -1
        boot_date = L.until_find_str("Boot loader date:")
        if (boot_date) == None: return -1
        
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


