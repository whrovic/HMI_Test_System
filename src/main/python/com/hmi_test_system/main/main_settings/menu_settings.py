import os

from data.define_and_fill_model import DefineAndFillModel as df
from data.model.model import Model
from data.settings import Settings
from main.constant_main import *
from main.library import Library as Lib

from .library_color import LibraryColor as LC
from .library_directory import LibraryDirectory as LD
from .library_edit_model import LibraryEditModel as LEM
from .library_new_model import LibraryNewModel as LNM
from .menu_prints import MenuPrints as MP


class MenuSettings:

    @staticmethod
    def sett():
        count = 0
        while True:
            MP.sett()
            menu_choice = input().strip()
            if len(menu_choice) == 0: continue

            match (menu_choice):
                #new model
                case '1':
                    count = 0
                    if ( MenuSettings.sett_newmodel() == -1 ):
                        os.system('cls')
                        return -1
                # color
                case '2':                    
                    count = 0
                    if (MenuSettings.sett_color() == -1):
                        os.system('cls')
                        return -1
                # edit model 
                case '3':
                    count = 0
                    if (MenuSettings.sett_editmenu() == -1 ):
                        os.system('cls')
                        return -1
                # test setting
                case '4':
                    count = 0
                    if (MenuSettings.sett_testsettings() == -1 ):
                        os.system('cls')
                        return -1
                # directory
                case '5':
                    count = 0
                    if ( MenuSettings.sett_directory() == -1 ):
                        os.system('cls')
                        return -1
                # exit 
                case '6':
                    os.system('cls')
                    return 0
                case _:
                    count = count + 1
                    if (count > NTIMEOUT_MENUS): 
                        os.system('cls')
                        return -1
                    Lib.exit_input("Invalid input")
                    continue
    
    @staticmethod
    def sett_newmodel():
        count = 0
        while True:
            MP.sett_newmodel()
            menu_choice = input()
            if len(menu_choice) == 0: continue
            
            match (menu_choice):
                # create
                case '1':
                    count = 0
                    LNM.new_model_create()
                # Import XML  
                case '2':
                    count = 0
                    LNM.new_model_import_xml()
                # back  
                case '3':
                    return 0
                # exit  
                case '4':
                    return -1
                case _:
                    count = count + 1
                    if (count > NTIMEOUT_MENUS):  return -1
                    Lib.exit_input("Invalid input")
                    continue
    
    @staticmethod
    def sett_color():
        count = 0
        while True:
            MP.sett_color()
            menu_choice = input()
            if len(menu_choice) == 0: continue

            match (menu_choice):
                # Edit colors
                case '1':
                    count = 0
                    MenuSettings.sett_color_editcolors()
                # Add color
                case '2':
                    count = 0
                    if (LC.edit_color_new_color() == -1):
                        Lib.exit_input("Was not possible add the Color")
                # Delete color
                case '3':
                    count = 0
                    if (LC.edit_color_delete_color() == -1):
                        Lib.exit_input("Was not possible delete the Color")  
                # Back
                case '4':
                    return 0
                # Exit
                case '5':
                    return -1
                case _:
                    count += 1
                    if (count > NTIMEOUT_MENUS):  return -1
                    Lib.exit_input("Invalid input")
                    continue

    @staticmethod
    def sett_color_editcolors():
        count = 0
        color = LC.sett_color_editcolor_first()
        if color is None: return 0
        while True:            
            MP.sett_color_editcolor()
            menu_choice = input().strip()

            match (menu_choice):
                # Edit name
                case '1':
                    if (LC.edit_color_edit_color_edit_name(color) == -1):
                        Lib.exit_input("Was not possible to edit the name")
                # Edit 1st range
                case '2':
                    if (LC.edit_color_edit_color_edit_1st_range(color) == -1):
                        Lib.exit_input("Was not possible to edit 1st range")
                # Edit 2nd range
                case '3':
                    if (LC.edit_color_edit_color_edit_2nd_range(color) == -1):
                        Lib.exit_input("Was not possible to edit 2st range")
                # Delete
                case '4':
                    if (LC.edit_color_edit_color_edit_delete(color) == -1):
                        Lib.exit_input("Was not possible to delete")
                # Back
                case '5':
                    break
                case _:
                    count += 1
                    if (count >= NTIMEOUT_MENUS): return -1
                    Lib.exit_input("Invalid input")
                    continue
        return 0
    
    @staticmethod
    def sett_editmenu():
        #TODO: changes not discard in the atual session
        # must replace them by the original xml (??)
        count = 0    
        save = False    
        model = LEM.sett_editmenu_first()
        if model is None: return 0
        while True:            
            MP.sett_editmenu()
            menu_choice = input().strip()

            match (menu_choice):
                # edit model info
                case '1':
                    LEM.edit_model_info(model)
                # edit led
                case '2':
                    MenuSettings.sett_editmenu_editled(model)
                # edit button
                case '3':
                    MenuSettings.sett_editmenu_editbutton(model)
                # edit display
                case '4':
                    LEM.edit_model_display(model)
                # save
                case '5':
                    df.create_xml(model)
                    Lib.exit_input("Changes saved!")
                    save = True
                    continue
                #back
                case '6':
                    if not save:
                        LEM.save_changes(model)
                    return 0
                #exit
                case '7':
                    if not save:
                        LEM.save_changes(model)
                    return -1
                case _:
                    count = count + 1
                    if (count > NTIMEOUT_MENUS):
                        return -1
                    Lib.exit_input("Invalid input")
                    continue

    @staticmethod
    def sett_editmenu_editled(model: Model):
        led, image = LEM.sett_editmenu_editled_first(model)
        if led is None: return 0
        #TODO confirm is led is the type Led
        while True:
            MP.sett_editmenu_editled()
            menu_choice = input()

            match(menu_choice):
                # edit name
                case '1':
                    LEM.edit_menu_edit_led_name(led)
                # edit colours
                case '2':
                    LEM.edit_menu_edit_led_colours(led)
                # edit position 
                case '3':
                    LEM.edit_menu_edit_led_position(led, image)
                # save
                case '4':
                    #df.create_xml(model)
                    #Lib.exit_input("Changes saved!")
                    save = True
                    continue
                #back
                case '5':
                    #if not save:
                        #LEM.save_changes(model)
                    return 0
                #exit
                case '6':
                    #if not save:
                        #LEM.save_changes(model)
                    return -1
                case _:
                    count = count + 1
                    if (count > NTIMEOUT_MENUS):
                        return -1
                    Lib.exit_input("Invalid input")
                    continue
                
    
    @staticmethod
    def sett_editmenu_editbutton(model: Model):

        image, button = LEM.sett_editmenu_editbutton_first(model)
        while True:
            
            MP.sett_editmenu_editbutton()
            c = input()

            # edit name
            if c=='1':
                c = LEM.edit_model_edit_button_name(button)
                continue

            # edit position 
            elif c=='2':
                c = LEM.edit_model_edit_button_position(image, button)
            
            # back to menu
            elif c == '3':
                break
    
    @staticmethod
    def sett_testsettings():
        count = 0
        while True:
            MP.sett_testsettings()        
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
                    Lib.exit_input("Invalid input")
                    continue

    @staticmethod
    def sett_directory():
        count = 0
        while True:
            MP.sett_directory()        
            menu_choice = input()
            
            match (menu_choice):
                #settings
                case '1':
                    count = 0
                    #TODO: Log of not sucessly change
                    LD.change_settings_directory()
                    #print("In construction")
                    #menu_choice = input('Press Enter')
                    continue
                
                #resource
                case '2':
                    count = 0
                    LD.change_resource_directory()
                    continue
                
                #xml
                case '3':
                    count = 0
                    LD.change_xml_directory()
                    continue
                
                #back
                case '4':
                    return 0
                
                #exit
                case '5':
                    return -1
                
                case _:
                    count = count + 1
                    if (count > NTIMEOUT_MENUS):
                        return -1
                    Lib.exit_input("Invalid input")
                    continue