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
    def new_model(): #sett_newmodel
        os.system('cls')
        print("-------------- New Model --------------\n\n")
        print("1- Create           2- Import XML   \n")
        print("3- Back             4- Exit            \n\n")
        print("---------------------------------------\n")
    
    @staticmethod
    def test_settings(): #sett_testsettings
        os.system('cls')
        print("------------ Test Settings ------------\n\n")
        print("1- Camera           2- Serial Port     \n")
        print("3- Back             4- Exit            \n\n")
        print("---------------------------------------\n")
    
    @staticmethod
    def color(): #sett_color
        os.system('cls')
        print("------------ Color Settings -----------\n\n")
        print("1 - Edit Colors      2 - Add Color     \n")
        print("3 - Delete a color                     \n")
        print("4 - Back             5 - Exit          \n")
        print("---------------------------------------\n")

    @staticmethod
    def edit_color(): #sett_color_editcolor
        os.system('cls')
        print("--------- Edit Color Settings ---------\n\n")
        print("1 - Edit name        2 - Edit 1st range\n")
        print("3 - Edit 2nd range   4 - Delete color  \n")
        print("               5 - Back                \n")
        print("---------------------------------------\n")

    @staticmethod
    def directory(): #sett_directory
        os.system('cls')
        print("------------ Test Settings ------------\n\n")
        print("1- Settings         2- Resource     \n")
        print("               3- XML                 \n")
        print("4- Back             5- Exit            \n\n")
        print("---------------------------------------\n")
    
    @staticmethod
    def edit_menu(): #sett_editmenu
        os.system('cls')
        print("-------------- Edit Menu --------------\n\n")
        print("1- Edit model info  2- Edit led        \n")
        print("3- Edit button      4- Edit LCD        \n")
        print("               5- Save                 \n")
        print("6- Back             7- Exit            \n\n")
        print("---------------------------------------\n")

    @staticmethod
    def edit_led(): #sett_editmenu_editled
        os.system('cls') 
        print("--------------- Edit Led --------------\n\n")
        print("1- Name             2- Colours         \n")
        print("3- Position         4- Back            \n\n")
        print("---------------------------------------\n")
    
    @staticmethod
    def edit_button(): #sett_editmenu_editbutton
        os.system('cls') 
        print("------------- Edit button -------------\n\n")
        print("1- Name             2- Position        \n")
        print("               3- Back                 \n\n")
        print("---------------------------------------\n")
    