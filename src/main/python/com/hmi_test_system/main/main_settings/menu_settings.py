import os

from data.define_and_fill_model import DefineAndFillModel as df
from data.settings import Settings
from main.constant_main import *
from main.library import Library as L

from .library_edit_model import LibraryEditModel as LEM
from .library_new_model import LibraryNewModel as LNM
from .menu_prints import MenuPrints as MP


class MenuSettings:

    @staticmethod
    def settings_menu():
        count = 0
        while True:
            MP.settings()
            menu_choice = input().strip()
            
            if len(menu_choice) == 0:
                continue

            match (menu_choice):
                #new model
                case '1':
                    count = 0
                    if ( MenuSettings.new_model_menu() == -1 ):
                        return -1
                
                # color
                case '2':                    
                    count = 0
                    if (MenuSettings.edit_color_menu() == -1):
                        return -1
            
                # edit model 
                case '3':
                    count = 0
                    if ( MenuSettings.edit_model_menu() == -1 ):
                        return -1

                # test setting
                case '4':
                    count = 0
                    if ( MenuSettings.edit_test_settings() == -1 ):
                        return -1
            
                # directory
                case '5':
                    count = 0
                    if ( MenuSettings.edit_directory_menu() == -1 ):
                        return -1

                # exit 
                case '6':
                    os.system('cls')
                    return 0
            
                case _:
                    count = count + 1
                    if (count > NTIMEOUT_MENUS):
                        return -1
                    L.exit_input("Invalid input")
                    #print("Invalid input")
                    #input("Press Enter to continue...")
                    continue
    
    @staticmethod
    def new_model_menu():
        count = 0
        while True:
            
            MP.new_model()
            menu_choice = input()
            
            match (menu_choice):
                # create
                case '1':
                    count = 0
                    LNM.new_model_mannually()

                # Import XML  
                case '2':
                    count = 0
                    LNM.new_model_import_xml()
            
                # back  
                case '3':
                    os.system('cls')
                    return 0

                # exit  
                case '4':
                    os.system('cls')
                    return -1
                
                case _:
                    count = count + 1
                    if (count > NTIMEOUT_MENUS):
                        return -1
                    L.exit_input("Invalid input")
                    continue
    
    @staticmethod
    def edit_model_menu():
        
        model = MenuSettings.edit_model_choose_model()
        if model is None:
            return 0
        
        count = 0        
        while True:
            
            MP.edit_menu()
            menu_choice = input()

            match (menu_choice):
                # edit model info
                case '1':
                    LEM.edit_model_info(model)
                        
                # edit led
                case '2':
                    LEM.edit_model_led(model)
                
                # edit button
                case '3':
                    LEM.edit_model_button(model)
                
                # edit display
                case '4':
                    LEM.edit_model_display(model)
                
                # save
                case '5':
                    df.create_xml(model)
                    L.exit_input("Changes saved!")
                    continue
                
                #back
                case '6':
                    LEM.save_changes(model)
                    return 0
                
                #exit
                case '7':
                    LEM.save_changes(model)
                    return -1
                
                case _:
                    count = count + 1
                    if (count > NTIMEOUT_MENUS):
                        return -1
                    L.exit_input("Invalid input")
                    continue

    @staticmethod
    def edit_model_choose_model():
        
        os.system('cls')

        # Get list of available models
        name_models = df.get_all_xml_file_names()
        if name_models is None:
            # TODO: Error code
            L.exit_input("Error path don't exist")
            #print("Error path don't exist")
            #input("Press Enter to continue...")
            return None
        elif len(name_models) == 0:
            L.exit_input("No available models to edit")
            #print("No available models to edit")
            #input("Press Enter to continue...")
            return None
        
        # Choose which model to edit
        while True:

            os.system('cls') 

            # Print all available models
            print("Available models:")
            for i, name in enumerate(name_models):
                print(str(i+1) + ' - ' + name)
            
            '''print("\nWhat model do you want to edit?")
            print("(Write 'q' to back to menu)")
            name_model = input()
            # Return to menu
            if (name_model == 'q'):
                return None'''
            name_model=L.get_name_or_index("\nWhat model do you want to edit?", name_models)
            if (name_model is None):
                # back to menu
                return None
            
            '''if name_model.isdigit():
                model_index = int(name_model)
                if model_index > 0 and model_index <= len(name_models):
                    name_model = name_models[model_index - 1]
                else:
                    L.exit_input("Invalid input")
                    continue'''
            
            if (df.open_model_xml(name_model) is None):
                os.system('cls')
                L.exit_input(f"{name_model} doesn't exist\n")
                continue
            else:
                return Settings.get_model(name_model)
    
    #TODO
    @staticmethod
    def edit_color_menu():
        print("In construction")
        input("Please come later...")
        pass
    
    @staticmethod
    def edit_test_settings():
        count = 0
        while True:
            
            MP.directory()        
            menu_choice = input()
            
            match (menu_choice):
                #camera
                case '1':
                    count = 0
                    print("In construction")
                    menu_choice = input('Press Enter')
                    continue
                
                #serial port
                case '2':
                    count = 0
                    print("In construction")
                    menu_choice = input('Press Enter')
                    continue
                
                #back
                case '3':
                    return 0
                
                #exit
                case '4':
                    return -1
                
                case _:
                    count = count + 1
                    if (count > NTIMEOUT_MENUS):
                        return -1

    # TODO
    @staticmethod
    def edit_directory_menu():
        count = 0
        while True:
            MP.directory()        
            menu_choice = input()
            
            match (menu_choice):
                #camera
                case '1':
                    count = 0
                    print("In construction")
                    menu_choice = input('Press Enter')
                    continue
                
                #serial port
                case '2':
                    count = 0
                    print("In construction")
                    menu_choice = input('Press Enter')
                    continue
                
                #back
                case '3':
                    return 0
                
                #exit
                case '4':
                    return -1
                
                case _:
                    count = count + 1
                    if (count > NTIMEOUT_MENUS):
                        return -1
                    L.exit_input("Invalid input")
                    continue