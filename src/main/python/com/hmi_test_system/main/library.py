from tkinter import Tk
from tkinter.filedialog import askdirectory

from .constant_main import *


class Library:
    @staticmethod
    def arguments_help():
        print("HELP")
        print("main.py [type: set or test]")
        print("   set - Initialize the user friendly menu of settings")
        print("   test [name_model] [(optional)type_test] [optionals]")
        print("   test [model_name] [serial_number] [manufacture_date] - Tests everything sequentially as defined in the model and the actual firmware")
        print("TYPE_TEST:")
        print("        KEYS		: -key \n 	BOOTLOADER INFO	: -bootloader \n	BOARD INFO	: -board")
        print("        ALIGHT	        : -alight \n	LEDS		: -led\n 	DISPLAY		: -display\n")
        print("        -sp             : The performed tests will only use serial port")
        print("                          Available in key, bootload, board and alight tests")
    
    @staticmethod
    def get_input_str(print_str: str):
        count = 0
        while True:
            if (count >= NTIMEOUT_LIBRARY_SETTINGS):
                Library.exit_input("Reach the limit of trys")
                return None
            
            # Ask for model name
            print(print_str)
            print("(Write \'q\' to cancel and return to menu)")
            name_model = str(input()).strip()
            
            # back to menu
            if (name_model == 'q'):
                return None
            elif name_model.isdigit() or (len(name_model) > 0 and name_model[0].isdigit()):
                print("Name cannot start with integer")
                count += 1
                continue
            elif len(name_model) == 0:
                print("Name cannot be empty")
                count += 1
                continue
            else:
                break
        return name_model
    
    @staticmethod
    def get_name_or_index(print_str: str, list_name: list[str]):
        count = 0
        while True:
            if (count >= NTIMEOUT_LIBRARY_SETTINGS):
                Library.exit_input("Reach the limit of trys")
                return None
            
            # Ask for model name
            print(print_str)
            print("(Write \'q\' to cancel and return to menu)")
            name_model = str(input()).strip()
            
            if (name_model == 'q'):
                # back to menu
                return None
            elif name_model.isdigit():
                model_index = int(name_model)
                if model_index > 0 and model_index <= len(list_name):
                    name_model = list_name[model_index - 1]
                    return name_model
                else:
                    Library.exit_input("Invalid input")
                    continue
            elif (len(name_model) > 0 and name_model[0].isdigit()):
                print("Name cannot start with integer")
                count += 1
                continue
            elif len(name_model) == 0:
                print("Name cannot be empty")
                count += 1
                continue
            else:
                break
        return name_model
    
    @staticmethod
    def get_yes_no_confirmation(print_str: str):
        count = 0
        while True:
            if (count >= NTIMEOUT_LIBRARY_SETTINGS):
                return False
            input_value = input(print_str).strip()

            if input_value.lower() == 'y':
                return True
            elif input_value.lower() == 'n':
                return False
            else:
                print("Invalid input! Please insert y or n")
                count += 1
                continue

    @staticmethod
    def exit_input(print_str: str):
        print(print_str)
        input('Press Enter to continue... ')
        return
    
    @staticmethod
    def until_find_str(print_str: str):
        count = 0
        while True:
            if (count >= NTIMEOUT_LIBRARY_SETTINGS):
                return None
            
            # Ask for data
            data = str(input(print_str)).strip()
            
            if (len(data) <= 0):
                count +=1
                continue
            else:
                break
        return data

    @staticmethod
    def until_find_int(print_str: str):
        count = 0
        while True:
            if (count >= NTIMEOUT_LIBRARY_SETTINGS):
                Library.exit_input("Maximum number of invalid inputs exceeded!")
                return -1
            
            # Ask for int
            value_input = str(input(print_str)).strip()
            
            # Check if it's integer
            if not value_input.isdigit():
                print("Invalid input! Please insert an integer value")
                count += 1
                continue
            else:
                value_input = int(value_input)
                break
        return value_input

    @staticmethod
    def get_hsv_values(print_str: str):
        count = 0
        while True:
            if (count >= NTIMEOUT_LIBRARY_SETTINGS): return (-1,)

            # Ask for three ints
            print(print_str)
            print("(Write \'q\' to cancel and return to menu)")
            value_input = input().strip()

            if value_input == 'q':
                return (-1,)

            # Check if it's three integer
            int_values = value_input.split()
            
            if len(int_values) != 3:
                print("Invalid input! Please insert three integer values, separated by a whitespace")
                count += 1
                continue
            elif not (int_values[0].isdigit() and int_values[1].isdigit() and int_values[2].isdigit()):
                print("Invalid input! Please insert three integer values, separated by a whitespace")
                count += 1
                continue
            else:
                h, s, v = int(int_values[0]), int(int_values[1]), int(int_values[2])
                
                if h < 0 or h > 180:
                    print("Invalid input! H value should be between 0 to 180")
                    count += 1
                    continue
                elif s < 0 or s > 255:
                    print("Invalid input! S value should be between 0 to 255")
                    count += 1
                    continue
                elif v < 0 or v > 255:
                    print("Invalid input! V value should be between 0 to 255")
                    count += 1
                    continue
                else:
                    return h, s, v
    
    
    @staticmethod
    def ask_directory():        
        count = 0
        while True:
            filename = askdirectory()    
            print(f"Path choose: {filename} \n\n")
            if filename is None:
                count +=1
                print("Inalid path")
                continue
            
            if (count >= NTIMEOUT_LIBRARY_SETTINGS):
                Library.exit_input("Reach the limit of trys")
                return None
            
            print("Do you want save the path [y|n]?")
            input_value = input().strip()
            if input_value.lower() == 'y':
                return filename
            else:
                print("Path not save")
                count += 1
                continue
        