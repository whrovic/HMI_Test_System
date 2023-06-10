import os
from tkinter import Tk
from tkinter.filedialog import askdirectory

from main.library import Library as L
from data.path import Path


class LibraryDirectory:
    @staticmethod
    def change_settings_directory():
        os.system('cls') 
        filename = LibraryDirectory._ask_directory()
        if filename is None:
            return -1
        elif os.path.exists(filename):
            Path.set_settings_directory(filename)
            return 0
        else:
            return -1
    
    @staticmethod
    def change_resource_directory():
        os.system('cls') 
        filename = LibraryDirectory._ask_directory()
        if os.path.exists(filename):
            Path.set_resources_directory(filename)
            return 0
        else:
            return -1
    
    @staticmethod
    def change_xml_directory():
        os.system('cls') 
        filename = LibraryDirectory._ask_directory()
        if os.path.exists(filename):
            Path.set_xml_direcory(filename)
            return 0
        else:
            return -1
    
    @staticmethod
    def _ask_directory():
        #Tk().withdraw() 
        filename = askdirectory()    
        L.exit_input(f"Path choose: {filename} \n\n")  
        #menu_choice = input()
        return filename
        



'''def open_xml_settings(): 
    while True:
        try:
            files = os.listdir(Settings.path.get_settings_directory())   # files in directory
            break
        except:
            print("Error path don't exist")
            print("To go to the menu insert anything\n")
            c = input()
            return -1
            
    xml_files = [file for file in files if file.endswith('.xml')]   # xml files in directory


    for filename in xml_files:
        # check if it is the asked file
        if filename == f'{"ADICIONAR"}.xml': 
            #...
            pass
            
def create_xml_settings():
    # Create the XML document and write it to a file
    tree = ET.ElementTree("")
    ET.indent(tree, '  ')
    tree.write(f"{Settings.path.get_settings_directory()}/{"ADICIONAR"}.xml")


def delete_xml_settings():
    file_path = f"{Settings.path.get_settings_directory()}/{"ADICIONAR"}.xml"

    # check if the file exists
    if os.path.exists(file_path):
        # delete the file
        os.remove(file_path)
        return 1
    else:
        return -1'''
    