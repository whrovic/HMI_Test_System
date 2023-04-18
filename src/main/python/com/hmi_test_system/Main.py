from data.Settings import Settings
from Library import create_model
import os

M = Settings()

while(1):
    os.system('cls') 
    print("---------------Menu---------------\n\n")
    print("1- Add model         2- Test model\n")
    print("             3- Exit")
    print("\n\n----------------------------------\n")
    c = input()

    if (c== '1'):
        n = 1
    elif (c== '2'):
        n = 2
    elif(c=='3'):
        os.system('cls')
        break
    else:
        continue


    #------------------------------------ADICIONAR NOVO MODELO------------------------------------#
    while(n==1):
        os.system('cls') 
        print("Insert the name of the new model:" )
        print("(to go to the menu insert b)\n" )
        name_model = input()
        
        if(name_model == 'b'):
            break
        elif(M.call_model(name_model) is None):
            os.system('cls') 
            print(f"                       MODEL {name_model} DOESN'T EXIST\n")
            print("\n\n----------------------NEW MODEL CONFIGURATION----------------------\n")

            create_model(M, name_model)

            os.system('cls') 
            print(f"MODEL {name_model} IS ADDED \n\n")
            print("To go to the menu insert anything\n")
            c = input()
            break
        else:
            os.system('cls') 
            print("MODEL ALREADY EXISTS\n\n")
            print("To go to the menu insert anything\n")
            c = input()
            break
        

            

    #------------------------------------TESTAR MODELO------------------------------------#
    while(n==2):
        os.system('cls') 
        print('What model do you want to test?')
        print("(to go to the menu insert b)\n" )
        name_model = input()
        
        if(name_model == 'b'):
            break
        elif(M.call_model(name_model) is None):
            os.system('cls') 
            print(f"MODEL {name_model} DOESN'T EXIST\n")
            print("To go to the menu insert anything\n")
            c = input()
            break

        else:
            M.set_model_test(name_model)
            os.system('cls') 
            print(f"MODEL {name_model} IS READY TO TEST\n")
            print("To start the test insert anything\n")
            c = input()
            os.system('cls')
            os.system('cls') 
            print("---------------Menu---------------\n\n")
            print("1- Add model         2- Test model\n")
            print("             3- Exit")
            print("\n\n----------------------------------\n")
            c = input()

            
        