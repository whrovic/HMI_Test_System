import os
import sys

from data.color.list_of_colors import ListOfColors
from data.settings import Settings
from main.constant_main import *
from main.main_settings import *
from main.main_test.library_test import test_menu
#from main.main_settings.menu_settings import MenuSettings as MS
#from main.main_test.library_test import *
from report import ExitCode

'''from tkinter import Tk
from tkinter.filedialog import askdirectory

Tk().withdraw() # Isto torna oculto a janela principal
filename = askdirectory() # Isto te permite selecionar um arquivo
print(filename) # printa o arquivo selecionado      
menu_choice = input()'''

count = 0
M = Settings()

# Read all the colors from the local file
ListOfColors.read_from_file(M.path.get_settings_directory() + "/colors.json")

def arguments_help():
    print("HELP")
    print("main.py [type: set or test]")
    print("   set - Initialize the user friendly menu of settings")
    print("   test [name_model] [(optional)type_test] [optionals]")
    print("   test [model_name] [serial_number] [manufacture_date] - Tests everything sequentially as defined in the model and the actual firmware")
    print("TYPE_TEST:")
    print("        KEYS		: -key \n 	BOOTLOADER INFO	: -bootloader \n	BOARD INFO	: -board")
    print("        ALIGHT	        : -alight \n	LEDS		: -led\n 	DISPLAY		: -display")

#------------------------------------CODE BEGIN------------------------------------#

if len(sys.argv) < 2:
    print("Miss arguments: main.py [type: set or test]")
    print("Ex: main.py set")
    print("Ex: main.py test [name_model] [(optional)type_test] [optionals]")
    ExitCode.failure_in_excetution()
    sys.exit(ExitCode.get_current_value())

value = sys.argv[1]
if value == TYPE_TEST:
    '''
    print("The value is 'test'") 
    menu_choice = input('Press Enter')'''
    exit_code = test_menu(M)
    print("Test Exit Code =", exit_code)
    
elif value == TYPE_SET:
    # Menu Settings
    MS.settings_menu(M)
elif value == TYPE_HELP:
    # Menu Settings
    arguments_help()
else:
    print("Wrong arguments, write main.py -help for help")
    menu_choice = input('Press Enter to exit ')


sys.exit(ExitCode.get_current_value())

'''while(settings):
    MP.main_menu_print()        
    menu_choice = input()
    
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
        if (count > NTIMEOUT_MENUS):
            break
        continue'''
