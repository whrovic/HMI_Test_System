import os

class MenuPrints:
    def main_menu_print():
        os.system('cls') 
        print("----------------Menu----------------\n\n")
        print("1- Menu Settings       2- Test model\n")
        print("             3- Exit")
        print("\n\n----------------------------------\n")

    def settings_menu_print():
        os.system('cls') 
        print("-----------Menu Settings-----------\n\n")
        print("1- New model         2- New Sequence\n")
        print("3- Edit model        4- Video Settings\n")
        print("5- Back              6- Exit\n")
        print("\n\n----------------------------------\n")
    
    def new_model_print():
        os.system('cls') 
        print("-------------New Model-------------\n\n")
        print("1- Manually          2- Automatic\n")
        print("3- TextFile          4- XML\n")
        print("5- Back              6- Exit\n")
        print("\n\n----------------------------------\n")
