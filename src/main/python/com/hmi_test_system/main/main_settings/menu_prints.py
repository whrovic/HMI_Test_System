import os

class MenuPrints:
    '''def main_menu_print():
        os.system('cls') 
        print("----------------Menu----------------\n\n")
        print("1- Menu Settings       2- Test model\n")
        print("             3- Exit")
        print("\n\n----------------------------------\n")'''

    def settings():
        os.system('cls') 
        print("-----------Menu Settings-----------\n\n")
        print("1- New model         2- Color\n")
        print("3- Edit model        4- Test Settings\n")
        print("5- Directory         6- Exit\n")
        print("\n\n----------------------------------\n")
    
    def new_model():
        os.system('cls') 
        print("-------------New Model-------------\n\n")
        print("1- Manually          2- Automatic\n")
        print("           3- XML\n")
        print("4- Back              5- Exit\n")
        print("\n\n----------------------------------\n")
    
    def test_settings():
        os.system('cls') 
        print("-------------Test Settings-------------\n\n")
        print("1- Camera            2- Serial Port\n")
        print("3- Back              4- Exit\n")
        print("\n\n----------------------------------\n")
    
    def directory():
        os.system('cls') 
        print("---------------Directory---------------\n\n")
        print("1- Camera            2- Serial Port\n")
        print("3- Back              4- Exit\n")
        print("\n\n----------------------------------\n")
