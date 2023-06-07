import sys

from data.define_and_fill_model import DefineAndFillModel as df
from data.model.model import Model
from data.settings import Settings
from main.constant_main import *

def test_menu(M: Settings):

    exit_code = 0

    # No model name
    if len(sys.argv) < 3:
        exit_code = 3
        return exit_code
    
    name_model = sys.argv[2]

    # Checks for bad model format
    if name_model[0].isdigit():
        exit_code = 3   # Invalid argument
        return exit_code

    # Model doesn't exist
    if(df.open_model_xml(M, name_model) is None):
        exit_code = 2   # Model doesn't exist
        return exit_code

    model = M.call_model(name_model)
    leds_name = []
    buttons_name = [] 


    # Specific tests
    if sys.argv[2].startswith('-'):
        
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
                exit_code = 3      # Invalid argument
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
                  
                else:
                    
                    if(args[0] == '-sp'):
                        args.pop(0)
                        key_code = 0    # Only serial port test
                    else:
                        key_code = 1    # Serial port and display test

    
            # Display test type
            elif (t_type == TEST_TYPE_DISPLAY):
                continue
            

            # Board_info test type
            elif(test_type[i] == TEST_TYPE_BOARD_INFO):
                if len(args) > 0:
                    
                    serial_number = args[0]
                    serial_number = str(serial_number)
                    args.pop(0)

                    manufacture_date = args[0]
                    manufacture_date = str(manufacture_date)
                    args.pop(0)

                    if(args[0] == '-sp'):
                        args.pop(0)
                        board_code = 0    # Only serial port test
                    else:
                        board_code = 1    # Serial port and display test

                

            # Bootloader_info test type
            elif(test_type[i] == TEST_TYPE_BOOTLOADER_INFO):
                
                if(args[0] == '-sp'):
                    args.pop(0)
                    bootloader_code = 0    # Only serial port test
                else:
                    bootloader_code = 1    # Serial port and display test


            # Alight test type
            elif(test_type[i] == TEST_TYPE_ALIGHT):
                
                if(args[0] == '-sp'):
                    args.pop(0)
                    alight_code = 0    # Only serial port test
                else:
                    alight_code = 1    # Serial port and display test
                
            else:
                exit_code = 3      # Invalid argument
                return exit_code
                


        # Execute the tests
        for i in range(len(test_type)):


            # Led test
            if(test_type[i] == TEST_TYPE_LEDS):

                # If user doesnt't choose the leds
                if(len(leds_name) == 0):
                    leds_name = None

                result_led = M.test.seq_led(model, leds_name)
                
                if(result_led == 0):
                    exit_code = 0     # Test passed
                elif(result_led == -1): 
                    exit_code = 8     # Led test failed


            # LCD test
            elif(test_type[i] == TEST_TYPE_DISPLAY):

                result_display = M.test.seq_display(model)
                
                if(result_display == 0):
                    exit_code = 0     # Test passed
                elif(result_display == -1): 
                    exit_code = 9     # LCD test failed  


            # Button test
            elif(test_type[i] == TEST_TYPE_BUTTONS):
                
                # If user doesnt't choose the buttons
                if(len(buttons_name) == 0):
                    buttons_name = None 

                result_button = M.test.seq_button(model, buttons_name, key_code)      
                
                if(result_button == 0):
                    exit_code = 0     # Test passed
                elif(result_button == -1): 
                    exit_code = 10    # Button test failed


            # Board_info test
            elif(test_type[i] == TEST_TYPE_BOARD_INFO):

                result_board = M.test.seq_board_info(model, serial_number, manufacture_date, board_code)

                if(result_board == 0):
                    exit_code = 0     # Test passed
                elif(result_board == -1): 
                    exit_code = 10    # Button test failed


            # Bootloader_info test
            elif(test_type[i] == TEST_TYPE_BOOTLOADER_INFO):

                result_bootloader = M.test.seq_boot_loader_info(model, bootloader_code)

                if(result_bootloader == 0):
                    exit_code = 0     # Test passed
                elif(result_bootloader == -1): 
                    exit_code = 10    # Button test failed


            # Alight test
            elif(test_type[i] == TEST_TYPE_ALIGHT):

                result_alight = M.test.seq_alight(alight_code)

                if(result_alight == 0):
                    exit_code = 0     # Test passed
                elif(result_alight == -1): 
                    exit_code = 10    # Button test failed            
    
    # Default -> all tests
    else:
        leds_name = None
        buttons_name = None

        serial_number = sys.argv[2]
        serial_number = str(serial_number)

        manufacture_date = sys.argv[3]
        manufacture_date = str(manufacture_date)

        result_all = M.test.seq_all(model, serial_number, manufacture_date)   

        if(result_all == 0):
            exit_code = 0     # Test passed
        elif(result_all == -1): 
            exit_code = 10    # Button test failed                    

    return exit_code
