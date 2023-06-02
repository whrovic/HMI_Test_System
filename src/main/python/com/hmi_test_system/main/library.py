
import os

from data import *
from .constant_main import *

class Library:

    def get_input(print_str: str):
        print(print_str)
        name_model = input('Write \'q\' to back to menu  ')
        # back to menu
        if(name_model == 'q'):
            return None
        
        return name_model
        
        
    def until_find_str(print_str: str):
        count = 0
        while True:
            print(print_str)
            board = str(input()) 
            board = board.strip()
            if (len(board) > MIN_LEN_STRING):
                break
            elif (count > NTIMEOUT_LIBRARY_SETTINGS):
                return None
            else:
                count +=1
                continue
        return board

    def until_find_int(print_str: str):
        count = 0
        while True:
            print(print_str)
            value_input = input()    
            if value_input.isdigit():
                value_input = int(value_input)
                break
            elif (count > NTIMEOUT_LIBRARY_SETTINGS):
                return -1
            else: 
                count +=1
                continue
        return value_input

