from data.settings import Settings
from main.library_settings import add_models
from main.library_settings import edit_model
from main.library_test import model_menu
import os
from main.menu_prints import MenuPrints as MP

from data.color.list_of_colors import ListOfColors

'''from tkinter import Tk
from tkinter.filedialog import askdirectory

Tk().withdraw() # Isto torna oculto a janela principal
filename = askdirectory() # Isto te permite selecionar um arquivo
print(filename) # printa o arquivo selecionado      
menu_choice = input()'''

NTIMEOUT = 5
count = 0
M = Settings()

ListOfColors.read_from_file(M.path.get_settings_directory() + "/colors.json")

#ListOfColors.add_color("Red", [0, 50, 50], [10, 255, 255], [170, 50, 50], [180, 255, 255])
#ListOfColors.add_color("Yellow", [20, 50, 50], [45, 255, 255])
#ListOfColors.add_color("Green", [60, 50, 50], [90, 255, 255])



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
            if (count > NTIMEOUT):
                return -1
            continue


#------------------------------------CODE BEGIN------------------------------------#
while(1):
    MP.main_menu_print()        
    menu_choice = input()
    
    # Menu Settings
    if (menu_choice == '1'):
        count = 0
        if (settings_menu(M) == -1 ):
            break

    # Test model    
    elif (menu_choice == '2'):
        count = 0
        model_menu(M) == -1 

    # Turn off the program    
    elif(menu_choice == '3'):
        os.system('cls')
        break

    else:
        count = count + 1
        if (count > NTIMEOUT):
            break
        continue