import sys
sys.path.append('../')
from data.Settings import Settings
from Library import create_model

M = Settings()

print("Nome do modelo: ")
name_model = input()

if(M.call_model(name_model) is None):
    print("MODELO NOVO")
    create_model(M, name_model)
else:
    print("MODELO EXISTENTE")

M.set_model_test(name_model)







