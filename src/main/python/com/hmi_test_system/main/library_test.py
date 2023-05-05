from data.settings import Settings
from data.define_and_fill_model import DefineAndFillModel as df
import os
from reportlab.pdfgen import canvas
from datetime import datetime
import sys
from data.model.led import Led 
from data.model.display import Display
from data.model.button import Button

def test_menu(M: Settings):

    name_model = sys.argv[0]

    if isinstance(name_model, str):
        pass
    else:
        exit_code = 3    # invalid argument

    # model doesn't exist
    if(df.open_model_xml(M, name_model) is None):
        print(f"{name_model} DOESN'T EXIST\n")
        exit_code = 2

    # specific tests
    if len(sys.argv) >= 2:
        test_type = []

        for i in len(sys.argv)-1:
            test_type[i] = sys.argv[i+1]

        for i in len(test_type):
            
            if (test_type[i] != 'led' or test_type[i] != 'display' or test_type[i] != 'key'):
                exit_code = 3    # invalid argument
        
        
        for i in len(test_type):

            model = M.call_model(name_model)

            # led test
            if(test_type[i] == "led"): 
                leds = model.get_leds()      
                result_led =led_test(M, leds)
                if(result_led == 0):
                    exit_code = 0     # test passed
                elif(result_led == -1): 
                    exit_code = 8     # led test failed
                
            # lcd test
            elif(test_type[i] == "display"):   
                display = model.get_display()    
                result_display =  display_test(M, display, 4) # 1 - pixel | 2 - rgb | 3- char | 4 - all 
                if(result_display == 0):
                    exit_code = 0     # test passed
                elif(result_display == -1): 
                    exit_code = 9     # led test failed  

            # button test
            elif(test_type[i] == "key"):
                buttons = model.get_buttons()    
                result_button = button_test(M, 3, buttons) # 1 - sp | 2 - dsp | 3- all
                if(result_button == 0):
                    exit_code = 0     # test passed
                elif(result_button == -1): 
                    exit_code = 10    # led test failed
    
    # default -> all tests
    else:
        result_led =led_test(M)
        result_display = display_test(M, 4)
        result_button = button_test(M)

        if(result_led + result_display + result_button == 0):
            exit_code = 0     # all tests passed
        elif(result_led == -1): 
            exit_code = 8     # led test failed
        elif(result_display== -1): 
            exit_code = 9     # display test failed 
        elif(result_button == -1): 
            exit_code = 10    # button test failed                        
                


    return exit_code



#------------------------------------LED TEST------------------------------------#
def led_test(M: Settings, leds: list[Led] = []):

    M.test.seq_led(leds)
    result: list[bool] = []
    for i in len(leds):
        led_result = leds[int(i)].result_test_Led()
        result.append(led_result)
        print(f"{leds[int(i)].get_name()} test: ")
        print("ok" if led_result==1 else "not ok")     

    if sum(result) == len(result): 
        return 0    # test passed
    else:
        return -1   # test failed          


#------------------------------------BUTTON TEST------------------------------------#
def button_test(M:Settings, code: int, buttons: list[Button] = []):
    
    if code == 1:
        result = M.test.seq_button(buttons, 1, 0)
    elif code == 2:
        result = M.test.seq_button(buttons, 0, 1)
    elif code == 3:
        result = M.test.seq_button(buttons, 1, 1)

    print("Keys test:")
    print("ok" if result == 0 else "not ok")

    return result
                                  
#------------------------------------LCD TEST------------------------------------#
def display_test(M:Settings, display: Display, code: int):
    
    if code == 1:
        result = M.test.seq_display(display, 1, 0, 0)
    elif code == 2:
        result = M.test.seq_display(display, 0, 0, 1)
    elif code == 3:
        result = M.test.seq_display(display, 0, 1, 0)
    elif code == 4:
        result = M.test.seq_display(display, 1, 1, 1)


    print("LCD test:")
    print("ok" if result == 0 else "not ok")
    return result   # 0 is sucess | -1 is failure