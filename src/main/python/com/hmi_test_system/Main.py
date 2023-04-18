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


    while(n==1):
        os.system('cls') 
        print("------------Add Model------------\n\n")
        print("1- Add new model         2- Menu")
        print("\n\n---------------------------------\n")
        c = input()

        #------------------------------------ADICIONAR NOVO MODELO------------------------------------#
        if(c == '1'):
            while(1):
                os.system('cls') 
                print("\nInsira o nome do modelo a adicionar:" )
                print("(para voltar ao menu digite b)\n" )
                name_model = input()
                
                if(name_model == 'b'):
                    break
                if(M.call_model(name_model) is None):
                    os.system('cls') 
                    print("\n\nMODELO NAO EXISTE\n")
                    print("\n\n----------------------CONFIGURAÇAO DO NOVO MODELO----------------------\n")

                    create_model(M, name_model)
                    os.system('cls') 
                    print("\n\nMODELO ADICIONADO\n")
                else:
                    os.system('cls') 
                    print("\n\nMODELO JA EXISTE\n")
                
            break

        elif(c == '2'):
            break

        else:
            continue

            

    #------------------------------------TESTAR MODELO------------------------------------#
    while(n==2):
        os.system('cls') 
        print("-----------Test Model-----------\n\n")
        print("1- Test model         2- Menu")
        print("\n\n--------------------------------\n")
        c = input()
        if(c == '1'):
            os.system('cls') 
            print('\nQue modelo quer testar?')
            print("(para voltar ao menu digite b)\n" )
            name_model = input()
            if(M.call_model(name_model) is None):
                os.system('cls') 
                print("\n\nMODELO NAO EXISTE\n")
                continue
            elif(name_model == 'b'):
                break
            else:
                M.set_model_test(name_model)
                os.system('cls') 
                print("\nMODELO PRONTO A TESTAR\n")
                break
        elif(c == '2'):
            break
        else:
            c = None
            continue