from LibraryFile import create_model_file
from data.Settings import Settings

from tkinter import Tk
from tkinter.filedialog import askopenfilename

#xml_directory='c:/Users/asus/ES/HMI_Test_System/src/main/python/com/hmi_test_system/m1.txt'
Tk().withdraw() # Isto torna oculto a janela principal
xml_directory = askopenfilename() # Isto te permite selecionar um arquivo
print(xml_directory) # printa o arquivo selecionado      
menu_choice = input()

name_model = "M1_simple"

M = Settings()
create_model_file(M,name_model, xml_directory)

M.set_model_test(name_model)


