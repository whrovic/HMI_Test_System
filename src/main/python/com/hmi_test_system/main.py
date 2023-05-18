from data.settings import Settings
#from main.library_test import model_menu
from main.menus import settings_menu
import os
import sys
from main.menu_prints import MenuPrints as MP
from data.color.list_of_colors import ListOfColors
from main.library_test import *

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

#------------------------------------CODE BEGIN------------------------------------#
if len(sys.argv) < 2:
    print("Usage: main.py test [name_model] [type_test] [timeOut]")
    sys.exit()

value = sys.argv[1]
settings = False

if value == "test":
    print("The value is 'test'") 
    menu_choice = input('Press Enter')
    test_menu(M)    
elif value == "set":
    print("The value is 'set'")
    settings = True
else:
    print(f"The value '{value}' is not 'test' or 'set'")
    menu_choice = input('Press Enter')
        
while(settings):
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
        print("Not working anymore :(")
        menu_choice = input('Press Enter')
        #model_menu(M) == -1 

    # Turn off the program    
    elif(menu_choice == '3'):
        os.system('cls')
        break

    else:
        count = count + 1
        if (count > NTIMEOUT):
            break
        continue