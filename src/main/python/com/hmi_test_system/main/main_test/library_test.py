import sys
from test.sequence_test import SequenceTest

from data.define_and_fill_model import DefineAndFillModel as df
from data.model.model import Model
from report.log_library_test import LogLibraryTest
from data.settings import Settings
from main.constant_main import *
from report import *


class LibraryTest:

    @staticmethod
    def test_menu():

        # No model name
        if len(sys.argv) < 3:
            LogLibraryTest.test_library_missing_name()
            ExitCode.invalid_argument()
            return
        
        name_model = sys.argv[2]

        # Checks for bad model format
        if name_model[0].isdigit():
            LogLibraryTest.test_library_invalid_name()
            ExitCode.invalid_argument
            return

        # Model doesn't exist
        if(df.open_model_xml(name_model) is None):
            LogLibraryTest.test_library_error_name(name_model)
            ExitCode.model_not_found()
            return

        model = Settings.get_model(name_model)
        leds_name = []
        buttons_name = [] 

        # Specific tests
        if sys.argv[3].startswith('-'):
            
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
                    LogLibraryTest.test_library_invalid_argument()
                    ExitCode.invalid_argument()
                    return
                
                test_type.append(t_type)

                # Leds test type
                if (t_type == TEST_TYPE_LEDS):

                    if len(args) > 0:                

                        n_leds = args[0]
                        n_leds = str(n_leds)

                        if not n_leds.isdigit():
                            if len(args) == 1:
                                LogLibraryTest.test_library_invalid_argument()
                                ExitCode.invalid_argument()
                                return
                            else:
                                continue

                        args.pop(0)
                        
                        n_leds = int(n_leds)
                        if len(args) < n_leds:
                            LogLibraryTest.test_library_invalid_number_argument()
                            ExitCode.invalid_number_of_arguments()
                            return

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
                                LogLibraryTest.test_library_invalid_argument()
                                ExitCode.invalid_argument()
                                return
                            else:
                                continue
                        
                        args.pop(0)

                        n_buttons = int(n_buttons)
                        if len(args) < n_buttons-1:
                            LogLibraryTest.test_library_invalid_number_argument()
                            ExitCode.invalid_number_of_arguments()
                            return

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
                    LogLibraryTest.test_library_invalid_argument()
                    ExitCode.invalid_argument()
                    return
                    


            # Execute the tests
            for i in range(len(test_type)):

                # Led test
                if (test_type[i] == TEST_TYPE_LEDS):

                    # If user doesnt't choose the leds
                    if (len(leds_name) == 0):
                        leds_name = None

                    result_led = SequenceTest.seq_led(model, leds_name)
                    
                    # TODO: Log this
                    if (result_led == 0):
                        print("Leds tests passed sucessfully")
                    elif (result_led == -1): 
                        print("Leds test failed")

                # LCD test
                elif (test_type[i] == TEST_TYPE_DISPLAY):

                    result_display = SequenceTest.seq_display(model)
                    
                    # TODO: Log this
                    if (result_display == 0):
                        print("Display tests passed successfully")
                    elif (result_display == -1): 
                        print("Display tests failed")

                # Button test
                elif(test_type[i] == TEST_TYPE_BUTTONS):
                    
                    # If user doesnt't choose the buttons
                    if(len(buttons_name) == 0):
                        buttons_name = None 

                    result_button = SequenceTest.seq_button(model, buttons_name, key_code)      
                    
                    # TODO: Log this
                    if(result_button == 0):
                        print("Buttons test passed successfully")
                    elif(result_button == -1): 
                        print("Buttons test failed")

                # Board_info test
                elif(test_type[i] == TEST_TYPE_BOARD_INFO):

                    result_board = SequenceTest.seq_board_info(model, serial_number, manufacture_date, board_code)

                    # TODO: Log this
                    if(result_board == 0):
                        print("BoardInfo test passed successfully")
                    elif(result_board == -1): 
                        print("BoardInfo test failed")

                # Bootloader_info test
                elif(test_type[i] == TEST_TYPE_BOOTLOADER_INFO):

                    result_bootloader = SequenceTest.seq_boot_loader_info(model, bootloader_code)

                    # TODO: Log this
                    if(result_bootloader == 0):
                        print("BootloaderInfo test passed successfully")
                    elif(result_bootloader == -1): 
                        print("BootloaderInfo test failed")

                # Alight test
                elif(test_type[i] == TEST_TYPE_ALIGHT):

                    result_alight = SequenceTest.seq_alight(alight_code)

                    # TODO: Log this
                    if(result_alight == 0):
                        print("Alight test passed successfully")
                    elif(result_alight == -1): 
                        print("Alight test failed")           
        
        # Default -> all tests
        else:
            leds_name = None
            buttons_name = None

            serial_number = sys.argv[2]
            serial_number = str(serial_number)

            manufacture_date = sys.argv[3]
            manufacture_date = str(manufacture_date)

            result_all = SequenceTest.seq_all(model, serial_number, manufacture_date)   

            # TODO: Log this
            if(result_all == 0):
                print("All the tests passed successfully")
            elif(result_all == -1): 
                print("At least one of the tests failed")                  

        return
