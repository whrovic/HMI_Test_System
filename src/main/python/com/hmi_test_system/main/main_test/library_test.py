import sys

from data.define_and_fill_model import DefineAndFillModel as df
from data.model.model import Model
from data.settings import Settings
from main.constant_main import *

def test_menu(M: Settings):

    exit_code = 0

    if len(sys.argv) < 3:
        print("No model name")
        exit_code = 3
        return exit_code
    
    name_model = sys.argv[2]

    # Checks for bad model format
    if name_model[0].isdigit():
        # TODO: Move this print to logs
        print("Invalid model name")
        exit_code = 3   # invalid argument
        return exit_code

    # Model doesn't exist
    if(df.open_model_xml(M, name_model) is None):
        # TODO: Move this print to logs
        print(f"Model {name_model} doesn't exist\n")
        exit_code = 2   # model doesn't exist
        return exit_code

    model = M.call_model(name_model)
    leds_name = []
    buttons_name = [] 


    # specific tests
    if len(sys.argv) > 3:
        
        args = []
        for i in range(3, len(sys.argv)):
            args.append(sys.argv[i])

        test_type = []

        while len(args) > 0:
            
            t_type = args[0]
            t_type = str(t_type)
            args.pop(0)

            # Check if it's a declaration of a new test
            if not t_type.startswith('-'):
                exit_code = 3      # invalid argument
                return exit_code
            
            test_type.append(t_type)

            # Leds test type
            if (t_type == TEST_TYPE_LEDS):

                if len(args) > 0:                

                    n_leds = args[0]
                    n_leds = str(n_leds)

                    if not n_leds.isdigit():
                        if len(args) == 1:
                            exit_code = 3      # Invalid argument
                            return exit_code
                        else:
                            continue

                    args.pop(0)
                    
                    n_leds = int(n_leds)
                    if len(args) < n_leds:
                        exit_code = 4      # Invalid number of arguments
                        return exit_code

                    for i in range(n_leds):
                        led_name = args[0]
                        args.pop(0)
                        leds_name.append(led_name)
            

            # Buttons test type
            elif (t_type == TEST_TYPE_BUTTONS):

                if len(args) > 1:
                    n_buttons = args[0]
                    n_buttons = str(n_buttons)

                    if not n_buttons.isdigit():
                        if len(args) == 1:
                            exit_code = 3      # Invalid argument
                            return exit_code
                        else:
                            continue
                    
                    args.pop(0)

                    n_buttons = int(n_buttons)
                    if len(args) < n_buttons-1:
                        exit_code = 4      # Invalid number of arguments
                        return exit_code

                    buttons_name = []
                    for i in range(n_buttons):
                        button_name = args[0]
                        args.pop(0)
                        buttons_name.append(button_name)
                  
                if(args[0] == '-sp'):
                    args.pop(0)
                    key_code = 0    # only serial port test
                else:
                    key_code = 1    # serial port and display test

    
            # Display test type
            elif (t_type == TEST_TYPE_DISPLAY):
                continue
            else:
                exit_code = 3      # invalid argument
                return exit_code


        # Execute the tests
        for i in range(len(test_type)):

            # led test
            if(test_type[i] == TEST_TYPE_LEDS):

                # if user doesnt't choose the leds
                if(len(leds_name) == 0):
                    leds_name = None

                result_led = led_test(M, model, leds_name)
                
                if(result_led == 0):
                    exit_code = 0     # test passed
                elif(result_led == -1): 
                    exit_code = 8     # led test failed

            # lcd test
            elif(test_type[i] == TEST_TYPE_DISPLAY):

                result_display =  display_test(M, model)
                
                if(result_display == 0):
                    exit_code = 0     # test passed
                elif(result_display == -1): 
                    exit_code = 9     # lcd test failed  

            # button test
            elif(test_type[i] == TEST_TYPE_BUTTONS):
                
                # if user doesnt't choose the buttons
                if(len(buttons_name) == 0):
                    buttons_name = None 

                # w/ dsp test -> key_code = 1  | only sp test -> key_code = 0                
                result_button = button_test(M, model, key_code, buttons_name)      
                
                if(result_button == 0):
                    exit_code = 0     # test passed
                elif(result_button == -1): 
                    exit_code = 10    # button test failed
                    
    
    # default -> all tests
    else:
        leds_name = None
        buttons_name = None

        result_led = led_test(M, model, leds_name)
        result_display = display_test(M, model)
        result_button = button_test(M, model, 1, buttons_name)

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
def led_test(M: Settings, model: Model, leds_name: list[str] = []):
    return M.test.seq_led(model, leds_name)
         
#------------------------------------BUTTON TEST------------------------------------#
def button_test(M:Settings,  model: Model, code: int, buttons_name: list[str] = []):
    return M.test.seq_button(model, buttons_name, code)     # w/ dsp test -> code = 1  | only sp test -> code = 0

#------------------------------------LCD TEST------------------------------------#
def display_test(M:Settings, model: Model):
    return M.test.seq_display(model)