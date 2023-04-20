from data.Settings import Settings
from LibrarySettings import add_models
from LibraryTest import model_menu
import os
from data.Led import Led
from data.Button import Button
from data.Display import Display
import xml.etree.ElementTree as ET
from main.MenuPrints import MenuPrints as MP

NTIMEOUT = 5
count = 0
M = Settings()

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
            if (count > NTIMEOUT):
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
            print("In construction")
            print("  Come later")
            menu_choice = input()

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
            if (count > NTIMEOUT):
                return -1
            continue

#------------------------------------CODE BEGIN------------------------------------#
while(1):
    MP.main_menu_print()        
    menu_choice = input()

    # add model
    if (menu_choice == '1'):
        count = 0
        if ( settings_menu(M) == -1 ):
            break

    # test model    
    elif (menu_choice == '2'):
        count = 0
        model_menu(M) == -1 

    # turn off the program    
    elif(menu_choice =='3'):
        os.system('cls')
        break

    else:
        count = count + 1
        if (count > NTIMEOUT):
            break
        continue