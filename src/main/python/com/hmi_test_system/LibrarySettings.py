from Library import open_model_xml
from Library import create_model_manual
from Library import create_xml
import os

def add_models(M):
    #------------------------------------ADD NEW MODEL------------------------------------#
    try:
        while True:
            os.system('cls') 
            print("Insert the name of the new model:" )
            print("(to go to the menu insert q)\n" )
            name_model = input()
            
            # back to menu
            if(name_model == 'q'):
                break
            
            # model doesn't exist -> new configuration
            elif(open_model_xml(M, name_model) is None):
                os.system('cls') 
                print(f"{name_model} DOESN'T EXIST\n")
                print("\n\n----------------------NEW MODEL CONFIGURATION----------------------\n")

                create_model_manual(M, name_model)
                create_xml(M, name_model)

                os.system('cls') 
                print(f"{name_model} IS ADDED \n\n")
                print("To go to the menu insert anything\n")
                c = input()
                break

            # model already exists
            else:
                os.system('cls') 
                print("MODEL ALREADY EXISTS\n\n")
                print("To go to the menu insert anything\n")
                c = input()
                break
    except:
        print("error")
        print("Do you want to repeat [y|n]")
        answer = input()
        if(answer == 'y'):
            add_models(M)
        