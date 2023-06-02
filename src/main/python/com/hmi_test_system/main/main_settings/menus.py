import os

from data.settings import Settings
from main.constant_main import *
from .library_settings import (add_models, create_model_manual, edit_button,
                               edit_camara_settings, edit_display, edit_led,
                               edit_led_settings, edit_model, edit_model_info,
                               edit_SP_settings)
from .menu_prints import MenuPrints as MP

#count = 0
class Menu:

    @staticmethod
    def settings_menu(M: Settings):
        count = 0
        while True:
            MP.settings()        
            menu_choice = input()
            
            # new model
            if (menu_choice == '1'):
                count = 0
                if ( Menu.new_model(M) == -1 ):
                    return -1

            # color
            elif (menu_choice == '2'):
                count = 0
                print("In construction")
                menu_choice = input('Press Enter')
        
            # edit model    
            elif (menu_choice == '3'):
                count = 0
                if ( edit_model(M) == -1 ):
                    return -1

            # test settings   
            elif (menu_choice == '4'):
                count = 0
                print("In construction")
                menu_choice = input('Press Enter')
            
            # directory
            elif(menu_choice == '5'):
                print("In construction")
                menu_choice = input('Press Enter')

            # exit 
            elif(menu_choice == '6'):
                os.system('cls')
                return 0
            
            else:
                count = count + 1
                if (count > NTIMEOUT_MENUS):
                    return -1
                continue
    
    @staticmethod
    def new_model(M: Settings):
        count = 0
        while True:
            MP.new_model()
            menu_choice = input()
            
            # manually
            if (menu_choice == '1'):
                count = 0
                add_models(M)

            # automatic
            elif (menu_choice == '2'):
                count = 0
                print("In construction")
                menu_choice = input('Press Enter')

            # XML  
            elif (menu_choice == '3'):
                count = 0
                print("In construction")
                menu_choice = input('Press Enter')
            
            # back  
            elif(menu_choice == '4'):
                os.system('cls')
                return 0

            # exit  
            elif(menu_choice == '5'):
                os.system('cls')
                return -1
            
            else:
                count = count + 1
                if (count > NTIMEOUT_MENUS):
                    return -1
                continue
