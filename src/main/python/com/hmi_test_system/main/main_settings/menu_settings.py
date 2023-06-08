import os

from data.define_and_fill_model import DefineAndFillModel as df
from data.settings import Settings
from main.constant_main import *
from main.library import Library as L

from .library_edit_model import LibraryEditModel as LEM
from .library_settings import LibrarySettings as LS
from .menu_prints import MenuPrints as MP


class MenuSettings:

    @staticmethod
    def settings_menu():
        count = 0
        while True:
            MP.settings()        
            menu_choice = input()
            
            
            match (menu_choice):
                #new model
                case '1':
                    count = 0
                    if ( MenuSettings.new_model() == -1 ):
                        return -1
                
                # color
                case '2':                    
                    count = 0
                    print("In construction")
                    menu_choice = input('Press Enter')
            
                # edit model 
                case '3':
                    count = 0
                    if ( LEM.edit_model() == -1 ):
                        return -1

                # test setting
                case '4':
                    count = 0
                    print("In construction")
                    menu_choice = input('Press Enter')
            
                # directory
                case '5':
                    count = 0
                    if ( MenuSettings.directory_menu() == -1 ):
                        return -1

                # exit 
                case '6':
                    os.system('cls')
                    return 0
            
                case _:
                    count = count + 1
                    if (count > NTIMEOUT_MENUS):
                        return -1
                    continue
    
    @staticmethod
    def new_model():
        count = 0
        while True:
            MP.new_model()
            menu_choice = input()
            
            match (menu_choice):
                # create
                case '1':
                    count = 0
                    LS.add_models_mannually()

                # Import XML  
                case '2':
                    count = 0
                    LS.add_models_xml()
            
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
    def directory_menu():
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
                               
    
    @staticmethod
    def edit_model_menu(M: Settings, index: int, image):
        count = 0
        while True:
            MP.edit_menu()                
            menu_choice = input()

            match (menu_choice):
                # edit name model
                case '1':
                    LEM.edit_model_info(M, index)
                    name_model = M.model[index].get_name()
                        
                # edit led
                case '2':
                    LEM.edit_led(M, name_model, index, image)
                
                # edit button
                case '3':
                    LEM.edit_button(M, name_model, index, image)
                
                # edit LCD
                case '4':
                    LEM.edit_display(M, index, image)
                
                # save
                case '5':
                    df.create_xml(M, name_model)
                    L.exit_input("Changes saved!")
                    '''print("Changes saved!")
                    input("Press Enter to continue...")
                    continue'''
                
                #back
                case '6':
                    LEM.save_changes(M, name_model)
                    return 0
                
                #exit
                case '7':
                    LEM.save_changes(M, name_model)
                    return -1
                
                case _:
                    count = count + 1
                    if (count > NTIMEOUT_MENUS):
                        return -1
                    
                    
                    
                

    