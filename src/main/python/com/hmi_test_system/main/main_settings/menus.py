import os

from data.settings import Settings
from main.constant_main import *
from main.main_settings import *

#count = 0

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


def settings_menu(M: Settings):
    count = 0
    while True:
        MP.settings()        
        menu_choice = input()
        
        # new model
        if (menu_choice == '1'):
            count = 0
            if ( new_model(M) == -1 ):
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
