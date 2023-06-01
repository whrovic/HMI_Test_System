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
        
    def edit_menu():
        os.system('cls')         
        print("-------------Edit Menu-------------\n\n")
        print("1- Edit model info   2- Edit led\n")
        print("3- Edit button       4- Edit LCD\n")
        print("             5- Save")
        print("6- Back              7- Exit\n")
        print("\n\n----------------------------------\n")

    def edit_led():
        os.system('cls') 
        print("-------------Edit Led-------------\n\n")
        print("1- Name          2- Colours\n")
        print("3- Position      4- Edit menu")
        print("\n\n----------------------------------\n")
        
    def edit_button():
        os.system('cls') 
        print("-------------Edit button-------------\n\n")
        print("1- Name          2- Position\n")
        print("      3- Edit menu")
        print("\n\n----------------------------------\n")
        
                