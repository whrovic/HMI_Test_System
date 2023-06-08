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
            
            
            match (menu_choice):
                #new model
                case '1':
                    count = 0
                    if ( MenuSettings.new_model(M) == -1 ):
                        return -1
                
                # color
                case 2:                    
                    count = 0
                    print("In construction")
                    menu_choice = input('Press Enter')
            
                # edit model 
                case 3:
                    count = 0
                    if ( LEM.edit_model(M) == -1 ):
                        return -1

                # test setting
                case 4:
                    count = 0
                    print("In construction")
                    menu_choice = input('Press Enter')
            
                # directory
                case 5:
                    count = 0
                    if ( MenuSettings.directory_menu(M) == -1 ):
                        return -1

                # exit 
                case 6:
                    os.system('cls')
                    return 0
            
                case _:
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
            
            match (menu_choice):
                # create
                case '1':
                    count = 0
                    LS.add_models_mannually(M)

                # Import XML  
                case '2':
                    count = 0
                    LS.add_models_xml(M)
            
                # back  
                case '3':
                    os.system('cls')
                    return 0

                # exit  
                case '4':
                    os.system('cls')
                    return -1
                
                case _:
                    count = count + 1
                    if (count > NTIMEOUT_MENUS):
                        return -1
                    continue

    @staticmethod
    def directory_menu(M: Settings):
        count = 0
        while True:
            MP.directory()        
            menu_choice = input()
            
            match (menu_choice):
                #camera
                case '1':
                    count = 0
                    print("In construction")
                    menu_choice = input('Press Enter')
                    continue
                
                #serial port
                case '2':
                    count = 0
                    print("In construction")
                    menu_choice = input('Press Enter')
                    continue
                
                #back
                case '3':
                    return 0
                
                #exit
                case '4':
                    return -1
                
                case _:
                    count = count + 1
                    if (count > NTIMEOUT_MENUS):
                        return -1
                

