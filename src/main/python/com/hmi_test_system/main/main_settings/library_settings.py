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
from video.image_files import ImageFiles

from .library_edit_model import LibraryEditModel as LEM
from .library_new_model import LibraryNewModel as LNM
from .menu_prints import MenuPrints as MP
from .menu_settings import MenuSettings as MS


class LibrarySettings:
    
    @staticmethod
    def edit_camara_settings():
        pass

    @staticmethod
    def edit_SP_settings():
        pass

    
    def edit_model(M: Settings):

        os.system('cls') 

        # TODO: Change this
        img_path = "test_images/HMI.png"

        cap = ImageFiles([img_path])

        cap.start_capture()

        image = cap.get_image()

        cap.stop_capture()
        cap.clear_queue()

        # Get list of available models
        name_models = DefineAndFillModel.get_all_xml_file_names(M)
        if name_models is None:
            # TODO: Error code
            L.exit_input("Error path don't exist")
            '''print("Error path don't exist")
            input("Press Enter to continue...")'''
            return -1
        elif len(name_models) == 0:
            L.exit_input("No available models to edit")
            #input("Press Enter to continue...")
            return 0

        #------------------------------------EDIT MENU------------------------------------#
        #while True:  # Is not necessary, i think
        #os.system('cls') 

        print("Available models:")
        for n in name_models:
            print(n)
        
        '''
        print("\nWhat model do you want to edit?")
        print("(Write 'q' to back to menu)")
        name_model = input()
        
        # back to menu
        if(name_model == 'q'):
            return 0'''
            
        name_model = L.get_input("\nWhat model do you want to edit?")
        if (name_model is None):
            # back to menu
            return 0

        # model doesn't exist
        elif(df.open_model_xml(M, name_model) is None):
            os.system('cls') 
            L.exit_input(f"{name_model} DOESN'T EXIST\n")
            '''print(f"{name_model} DOESN'T EXIST\n")
            input("Press Enter to continue..." )'''
        
        # model  exists
        else:
            #df.delete_xml(name_model, directory) # Delete the xml file
            index = M.index_model(name_model)

            if(index == -1):
                return -1

            name_model = M.model[index].get_name()

            if (MS.edit_model_menu(M, index, image) == -1):
                return -1
            
        return 0
                        
        
    
    def add_models_mannually(M: Settings):
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
                