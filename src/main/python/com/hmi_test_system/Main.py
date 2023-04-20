from data.Settings import Settings
#from main.Library import create_model_manual
from Library import open_model_xml
#from main.Library import create_xml
from LibrarySettings import add_models
from LibraryTest import menu_model_test
import os
from data.Led import Led
from data.Button import Button
from data.Display import Display
import xml.etree.ElementTree as ET

M = Settings()



#------------------------------------MENU------------------------------------#

while(1):
    os.system('cls') 
    print("---------------Menu---------------\n\n")
    print("1- Add model         2- Test model\n")
    print("             3- Exit")
    print("\n\n----------------------------------\n")        
    c = input()

    # add model
    if (c== '1'):
        #n = 1
        add_models(M)

    # test model    
    elif (c== '2'):
        #n = 2
        menu_model_test(M)

    # turn off the program    
    elif(c=='3'):
        os.system('cls')
        break

    else:
        continue