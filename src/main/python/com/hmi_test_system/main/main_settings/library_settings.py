'''from data.color.list_of_colors import ListOfColors
from data.define_and_fill_model import DefineAndFillModel as df
from data.model.boot_loader_info import BootLoaderInfo
from data.model.button import Button
from data.model.display import Display
from data.model.info import Info
from data.model.led import Led
from data.settings import Settings
'''
import os

from data import *
from data.define_and_fill_model import DefineAndFillModel as df
from main.constant_main import *
from main.library import Library as L

from .library_edit_model import LibraryEditModel as LEM
from .library_new_model import LibraryNewModel as LNM
from .menu_prints import MenuPrints as MP


class LibrarySettings:
    
    @staticmethod
    def edit_camara_settings():
        pass

    @staticmethod
    def edit_SP_settings():
        pass

    @staticmethod
    def add_models_mannually():
        #------------------------------------ADD NEW MODEL------------------------------------#
        while True:
            os.system('cls') 
                
            name_model = L.get_input("Insert the name of the new model:")
            if (name_model is None):
                # back to menu
                break
            
            # model doesn't exist -> new configuration
            elif (df.open_model_xml(name_model) is None):
                os.system('cls') 
                print("\n\n----------------------NEW MODEL CONFIGURATION----------------------\n")

                if ( LNM.create_model_manual(name_model) == 0):
                    df.create_xml(name_model)
                    os.system('cls')
                    L.exit_input(f"{name_model} IS ADDED \n\n")
                    break
                else:
                    os.system('cls')
                    L.exit_input(f"{name_model} IS NOT ADDED \n\n")
                    break
            # model already exists
            else:
                os.system('cls')
                L.exit_input(f"{name_model} ALREADY EXISTS\n\n")
                break

    @staticmethod
    def add_models_xml():
        
        #------------------------------------ADD NEW MODEL------------------------------------#
        while True:
            os.system('cls') 
                
            name_model = L.get_input("Insert the name of the new model:")
            if (name_model is None):
                # back to menu
                break
            
            # model doesn't exist -> new configuration
            elif (df.open_model_xml(name_model) is None):
                os.system('cls') 
                print("Insert the path of the XML file")
                directory = str(input())

                if (LNM.create_model_xml(directory, name_model) == 0):
                    df.create_xml(name_model)
                    os.system('cls')
                    L.exit_input(f"{name_model} IS ADDED \n\n")
                    break
                else:
                    os.system('cls')
                    L.exit_input(f"{name_model} IS NOT ADDED \n\n")
                    break
            # model already exists
            else:
                os.system('cls')
                L.exit_input(f"{name_model} ALREADY EXISTS\n\n")
                break
                