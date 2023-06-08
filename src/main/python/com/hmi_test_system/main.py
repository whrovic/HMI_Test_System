import sys

from data.color.list_of_colors import ListOfColors
from data.settings import Settings
from main.constant_main import *
from main.main_settings import *
from main.main_test.library_test import test_menu
from report import ExitCode

'''from tkinter import Tk
from tkinter.filedialog import askdirectory

Tk().withdraw() # Isto torna oculto a janela principal
filename = askdirectory() # Isto te permite selecionar um arquivo
print(filename) # printa o arquivo selecionado      
menu_choice = input()'''

# Read all the colors from the local file
ListOfColors.read_from_file(Settings.path.get_settings_directory() + "/colors.json")

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
    
    exit_code = test_menu(Settings)
    print("Test Exit Code =", exit_code)
    
elif value == TYPE_SET:
    # Menu Settings
    MS.settings_menu(Settings)
elif value == TYPE_HELP:
    # Menu Settings
    arguments_help()
else:
    print("Wrong arguments, write main.py -help for help")
    menu_choice = input('Press Enter to exit ')


sys.exit(ExitCode.get_current_value())