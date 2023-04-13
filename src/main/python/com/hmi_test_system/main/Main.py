from hmi_test_system.data.Settings import Settings
from Library import createModel

M = Settings()

print("Nome do modelo: ")
name_model = input()

if(M.callModel(name_model) is None):
    print("MODELO NOVO")
    createModel(M, name_model)
else:
    print("MODELO EXISTENTE")

M.setModelTest(name_model)







