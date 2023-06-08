from data import *

from .constant_main import *


class Library:

    def get_input(print_str: str):
        count = 0
        while True:
            if (count >= NTIMEOUT_LIBRARY_SETTINGS):
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
    
    def exit_input(print_str: str):
        print(print_str)
        input('Press Enter ')
        return
        
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

    def until_find_int(print_str: str):
        count = 0
        while True:
            if (count >= NTIMEOUT_LIBRARY_SETTINGS):
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