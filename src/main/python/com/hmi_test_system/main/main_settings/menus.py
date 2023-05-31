import os
from data.settings import Settings
from main.main_settings.library_settings import add_models
from main.main_settings.library_settings import edit_model
from main.main_settings.menu_prints import MenuPrints as MP
from main.constant_main import *

count = 0

def new_model(M: Settings):
    count = 0
    while True:
        MP.new_model_print()
        menu_choice = input()
        
        # manually
        if (menu_choice == '1'):
            count = 0
            add_models(M)

        # automatic
        elif (menu_choice == '2'):
            count = 0
            print("In construction")
            print("  Come later")
            menu_choice = input()
    
        # textfile   
        elif (menu_choice == '3'):
            count = 0
            print("In construction")
            print("  Come later")
            menu_choice = input()

        # XML  
        elif (menu_choice == '4'):
            count = 0
            print("In construction")
            print("  Come later")
            menu_choice = input()
        
        # back  
        elif(menu_choice == '5'):
            os.system('cls')
            return 0

        # turn off the program    
        elif(menu_choice == '6'):
            os.system('cls')
            return -1
        
        else:
            count = count + 1
            if (count > NTIMEOUT_MENUS):
                return -1
            continue


def settings_menu(M: Settings):
    count = 0
    while True:
        MP.settings_menu_print()        
        menu_choice = input()
        
        # add model
        if (menu_choice == '1'):
            count = 0
            if ( new_model(M) == -1 ):
                return -1

        # new sequence
        elif (menu_choice == '2'):
            count = 0
            print("In construction")
            print("  Come later")
            menu_choice = input()
    
        # edit model    
        elif (menu_choice == '3'):
            count = 0
            if ( edit_model(M) == -1 ):
                return -1


        # edit video    
        elif (menu_choice == '4'):
            count = 0
            print("In construction")
            print("  Come later")
            menu_choice = input()
        
        # back  
        elif(menu_choice == '5'):
            os.system('cls')
            return 0

        # turn off the program    
        elif(menu_choice == '6'):
            os.system('cls')
            return -1
        
        else:
            count = count + 1
            if (count > NTIMEOUT_MENUS):
                return -1
            continue
