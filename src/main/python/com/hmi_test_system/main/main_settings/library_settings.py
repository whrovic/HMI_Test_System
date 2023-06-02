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
from main.constant_main import *
from main.library import Library as L
from opencv.define_model_cv import DefineModelCV
from video.image_files import ImageFiles

from .library_edit_model import LibraryEditModel as LEM
from .library_new_model import LibraryNewModel as LNM
from .menu_prints import MenuPrints as MP


class LibrarySettings:
    def edit_camara_settings(M: Settings):
        pass

    def edit_SP_settings(M: Settings):
        pass

    
    def add_models(M: Settings):
        #------------------------------------ADD NEW MODEL------------------------------------#
        while True:
            os.system('cls') 
            
            '''print("Insert the name of the new model:" )
            #print("(to go to the menu insert q)\n" )
            name_model = input('Write \'q\' to back to menu  ')
            
            # back to menu
            if(name_model == 'q'):
                break'''
                
            name_model = L.get_input("Insert the name of the new model:")
            if(name_model == None):
                # back to menu
                break
            
            # model doesn't exist -> new configuration
            elif(df.open_model_xml(M, name_model) is None):
                os.system('cls') 
                print(f"{name_model} DOESN'T EXIST\n")
                print("\n\n----------------------NEW MODEL CONFIGURATION----------------------\n")

                if ( LNM.create_model_manual(M, name_model) == 0):
                    df.create_xml(M, name_model)
                    os.system('cls') 
                    #print(f"{name_model} IS ADDED \n\n")
                    #print("To go to the menu insert anything\n")
                    #c = input()
                    L.exit_input(f"{name_model} IS ADDED \n\n")
                    break
                else:
                    os.system('cls') 
                    #print(f"{name_model} IS NOT ADDED \n\n")
                    #c = input('Press Enter ')
                    L.exit_input(f"{name_model} IS NOT ADDED \n\n")
                    break
            # model already exists
            else:
                os.system('cls') 
                #print(f"{name_model} ALREADY EXISTS\n\n")
                #c = input('Press Enter ')
                L.exit_input(f"{name_model} ALREADY EXISTS\n\n")
                break
