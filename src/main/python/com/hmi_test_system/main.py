import sys
from tkinter import Tk

from data.color.list_of_colors import ListOfColors
from data.settings import Settings
from main.constant_main import *
from main.library import Library as Lib
from main.main_settings import *
from main.main_test import *
from report import ExitCode
from report.exit_code import ExitCode

# Necessary to choose or change path on the settings
Tk().withdraw() 

# Read all the colors from the local file
ListOfColors.read_from_file()

# TODO: This code is temporary

from data.hardware_settings.camera_settings import CameraSettings
from data.hardware_settings.parameter import Parameter
from data.hardware_settings.test_settings import TestSettings

def_params = Parameter()
dsp_params = Parameter(auto_focus=0.0, manual_focus=20, 
                       auto_exposure=0.0, exposure=-9, gain=0,
                       auto_white_balance=0.0, white_balance=6500)
led_params = Parameter(auto_focus=0.0, manual_focus=45,
                       auto_exposure=0.0, exposure=-11, gain=0,
                       auto_white_balance=0.0, white_balance=3800,
                       brightness=80, saturation=255)
logi_cam = CameraSettings('LogiCam', 0)
logi_cam.set_parameters('default', def_params)
logi_cam.set_parameters('display', dsp_params)
logi_cam.set_parameters('leds', led_params)
TestSettings.add_new_cam_settings(logi_cam)
TestSettings.set_cam_display('LogiCam')
TestSettings.set_cam_leds('LogiCam')

TestSettings.add_new_sp_settings('SerialPort', 'COM5', 115200)
TestSettings.set_sp_main('SerialPort')

#################################

#------------------------------------CODE BEGIN------------------------------------#

if len(sys.argv) < 2:
    print("Miss arguments: main.py [type: set or test]")
    print("Ex: main.py set")
    print("Ex: main.py test [name_model] [(optional)type_test] [optionals]")
    ExitCode.failure_in_excetution()
    sys.exit(ExitCode.get_current_value())

value = sys.argv[1]
if value == TYPE_TEST:
    # Test    
    exit_code = LT.test_menu()
    print("Test Exit Code =", ExitCode.get_current_value())
elif value == TYPE_SET:
    # Menu Settings
    MS.sett()
elif value == TYPE_HELP:
    # Menu Settings
    Lib.arguments_help()
else:
    Lib.exit_input("Wrong arguments, write main.py -help for help")

sys.exit(ExitCode.get_current_value())