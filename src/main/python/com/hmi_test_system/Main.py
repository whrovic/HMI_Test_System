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


    #------------------------------------ADD NEW MODEL------------------------------------#
    while(n==1):
        os.system('cls') 
        print("Insert the name of the new model:" )
        print("(to go to the menu insert b)\n" )
        name_model = input()
        
        if(name_model == 'b'):
            break
        elif(M.call_model(name_model) is None):
            os.system('cls') 
            print(f"                            {name_model} DOESN'T EXIST\n")
            print("\n\n----------------------NEW MODEL CONFIGURATION----------------------\n")

            create_model(M, name_model)

            os.system('cls') 
            print(f"{name_model} IS ADDED \n\n")
            print("To go to the menu insert anything\n")
            c = input()
            break
        else:
            os.system('cls') 
            print("MODEL ALREADY EXISTS\n\n")
            print("To go to the menu insert anything\n")
            c = input()
            break
        

            

    #------------------------------------MODEL TEST------------------------------------#
    while(n==2):
        os.system('cls') 
        print('What model do you want to test?')
        print("(to go to the menu insert b)\n" )
        name_model = input()
        
        if(name_model == 'b'):
            break
        elif(M.call_model(name_model) is None):
            os.system('cls') 
            print(f"{name_model} DOESN'T EXIST\n")
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
            print("1- Led test         2- Button test\n")
            print("3- LCD test         4- Menu")
            print("\n\n----------------------------------\n")
            c = input()
            if (c== '1'):
                n = 1
            elif (c== '2'):
                n = 2
            elif (c== '3'):
                n=3
            elif(c=='4'):
                break
            else:
                continue

            #------------------------------------LED TEST------------------------------------#
            while(n==1):
                os.system('cls')
                print("What led do you want to test?\n")
                led_name = input()
                index_led = M.index_led(led_name)
                if(index_led is None):
                    print(f"{led_name} DOESN'T EXIST")
                else:
                    pass
                

            #------------------------------------BUTTON TEST------------------------------------#
            while(n==2):
                os.system('cls')
                print("What button do you want to test?\n")
                button_name = input()
                index_button = M.index_led(button_name)
                if(index_button is None):
                    print(f"{button_name} DOESN'T EXIST")
                else:
                    pass
                
            #------------------------------------BUTTON TEST------------------------------------#
            while(n==3):
                pass
            


            
        