import os


class MenuPrints:

    @staticmethod
    def settings():
        os.system('cls')
        print("------------ Menu Settings ------------\n\n")
        print("1- New model        2- Color           \n")
        print("3- Edit model       4- Test Settings   \n")
        print("5- Directory        6- Exit            \n\n")
        print("---------------------------------------\n")
    
    @staticmethod
    def new_model():
        os.system('cls')
        print("-------------- New Model --------------\n\n")
        print("1- Create           2- Import XML   \n")
        print("3- Back             4- Exit            \n\n")
        print("---------------------------------------\n")
    
    @staticmethod
    def test_settings():
        os.system('cls')
        print("------------ Test Settings ------------\n\n")
        print("1- Camera           2- Serial Port     \n")
        print("3- Back             4- Exit            \n\n")
        print("---------------------------------------\n")
    
    @staticmethod
    def directory():
        os.system('cls')
        print("------------ Test Settings ------------\n\n")
        print("1- Settings         2- Resource     \n")
        print("               3- XML                 \n")
        print("4- Back             5- Exit            \n\n")
        print("---------------------------------------\n")
    
    @staticmethod
    def edit_menu():
        os.system('cls')
        print("-------------- Edit Menu --------------\n\n")
        print("1- Edit model info  2- Edit led        \n")
        print("3- Edit button      4- Edit LCD        \n")
        print("               5- Save                 \n")
        print("6- Back             7- Exit            \n\n")
        print("---------------------------------------\n")

    @staticmethod
    def edit_led():
        os.system('cls') 
        print("--------------- Edit Led --------------\n\n")
        print("1- Name             2- Colours         \n")
        print("3- Position         4- Edit menu       \n\n")
        print("---------------------------------------\n")
    
    @staticmethod
    def edit_button():
        os.system('cls') 
        print("------------- Edit button -------------\n\n")
        print("1- Name             2- Position        \n")
        print("             3- Edit menu              \n\n")
        print("---------------------------------------\n")
    