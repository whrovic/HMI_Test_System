import os

from data.settings import Settings
from main.constant_main import *
from .library_settings import LibrarySettings as LS
from .menu_prints import MenuPrints as MP
from .library_edit_model import LibraryEditModel as LEM

#count = 0
class MenuSettings:

    @staticmethod
    def settings_menu(M: Settings):
        count = 0
        while True:
            MP.settings()        
            menu_choice = input()
            
            # match (menu_choice):
            #     case '1':
            #         break

            # new model
            if (menu_choice == '1'):
                count = 0
                if ( MenuSettings.new_model(M) == -1 ):
                    return -1

            # color
            elif (menu_choice == '2'):
                count = 0
                print("In construction")
                menu_choice = input('Press Enter')
        
            # edit model    
            elif (menu_choice == '3'):
                count = 0
                if ( LEM.edit_model(M) == -1 ):
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
                LS.add_models(M)

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