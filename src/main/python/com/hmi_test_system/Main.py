from data.Settings import Settings
from Library import create_model

M = Settings()

while(1): 
    print("\nQuer adicionar um novo modelo? y/n ")
    c = input()

    #------------------------------------ADICIONAR NOVO MODELO------------------------------------#
    if(c == 'y'):
        while(1):
            print("\nNome do modelo a adicionar: ")
            name_model = input()

            if(M.call_model(name_model) is None):
                print("\n\nMODELO NAO EXISTE\n")
                print("\n\n----------------------CONFIGURAÇAO DO NOVO MODELO----------------------\n")

                create_model(M, name_model)
                print("\n\nMODELO ADICIONADO\n")
            else:
                print("\n\nMODELO JA EXISTE\n")

            while(1):
                print("\nQuer adicionar um novo modelo? y/n")
                c = input()
                if(c == 'y'):
                    break
                elif(c == 'n'):
                    break
            if(c == 'y'):
                continue
            elif(c == 'n'):
                    break
        break

    elif(c == 'n'):
        break

    else:
        continue

        

#------------------------------------TESTAR MODELO------------------------------------#
while(1):
    print('\nQue modelo quer testar?')
    name_model = input()
    if(M.call_model(name_model) is None):
        print("\n\nMODELO NAO EXISTE\n")
        continue
    else:
        M.set_model_test(name_model)
        print("\nMODELO PRONTO A TESTAR\n")
        break


