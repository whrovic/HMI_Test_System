#import sys
#sys.path.append('c:/Users/filip/Desktop/ES/HMI_Test_System/src/main/python/com/hmi_test_system')
#sys.path.append('c:/Users/asus/ES/HMI_Test_System/src/main/python/com/hmi_test_system')

from data.Settings import Settings
from Library import create_model

M = Settings()

print("Nome do modelo: ")
name_model = input()
#Test File = "../data/m1.txt"

if(M.call_model(name_model) is None):
    print("MODELO NOVO")
    create_model(M, name_model)
else:
    print("MODELO EXISTENTE")

M.set_model_test(name_model)