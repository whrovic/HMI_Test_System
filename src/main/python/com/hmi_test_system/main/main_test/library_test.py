import sys
from test.sequence_test import SequenceTest

from data.define_and_fill_model import DefineAndFillModel as df
from data.settings import Settings
from main.constant_main import *
from report import *


class LibraryTest:
    

    @staticmethod
    def test_menu():
        leds_name = []
        buttons_name = []

        # No model name
        if len(sys.argv) < 3:
            LogLibraryTest.test_library_missing_name()
            ExitCode.invalid_argument()
            return
        
        model = LibraryTest.check_model_name()
        if model is None: return
        
        if(sys.argv[3] is None):
            ExitCode.invalid_number_of_arguments()
            return
        
        # Specific tests
        if sys.argv[3].startswith('-'):            
            t_type = sys.argv[3]
            
            # Leds test type
            if (t_type == TEST_TYPE_LEDS):                
                if len(sys.argv) > 4:  
                    n_leds = sys.argv[4]

                    if not n_leds.isdigit():
                        LogLibraryTest.test_library_invalid_argument()
                        ExitCode.invalid_argument()
                        return
                    
                    n_leds = int(n_leds)
                    if len(sys.argv) - 5 != n_leds:
                        LogLibraryTest.test_library_invalid_number_argument()
                        ExitCode.invalid_number_of_arguments()
                        return

                    for i in range(n_leds):
                        led_name = sys.argv[i+5]
                        leds_name.append(led_name)

            # Buttons test type
            elif (t_type == TEST_TYPE_BUTTONS):
                if len(sys.argv) > 4:
                    key_code = 1

                    n_buttons = sys.argv[4]
                    if n_buttons == '-sp':
                        n_buttons = 0
                        key_code = 0
                    elif not n_buttons.isdigit():
                        LogLibraryTest.test_library_invalid_argument()
                        ExitCode.invalid_argument()
                        return
                    else:
                        n_buttons = int(n_buttons)
                        if len(sys.argv) - 5 < n_buttons:
                            LogLibraryTest.test_library_invalid_number_argument()
                            ExitCode.invalid_number_of_arguments()
                            return

                        buttons_name = []
                        for i in range(n_buttons):
                            button_name = sys.argv[5+i]
                            buttons_name.append(button_name)
                    
                        if len(sys.argv) > 5 + n_buttons:
                            if sys.argv[5+n_buttons] == '-sp':
                                key_code = 0 # Only serial port test
                            else:
                                LogLibraryTest.test_library_invalid_argument()
                                ExitCode.invalid_argument()
                                return

            # Display test type
            elif (t_type == TEST_TYPE_DISPLAY):
                if len(sys.argv) > 4:
                    LogLibraryTest.test_library_invalid_number_argument()
                    ExitCode.invalid_number_of_arguments()
                    return
            
            # Board_info test type
            elif (t_type == TEST_TYPE_BOARD_INFO):
                
                if len(sys.argv) < 6:
                    LogLibraryTest.test_library_invalid_number_argument()
                    ExitCode.invalid_number_of_arguments()
                    return
                

                serial_number = sys.argv[4]
                manufacture_date = sys.argv[5]

                board_code = 1
                if len(sys.argv) > 6:
                    if sys.argv[6] == '-sp':
                        board_code = 0          # Only serial port test
                    else:
                        LogLibraryTest.test_library_invalid_argument()
                        ExitCode.invalid_argument()
                        return

            # Bootloader_info test type
            elif(t_type == TEST_TYPE_BOOTLOADER_INFO):
                
                bootloader_code = 1             # Serial port and display test
                if len(sys.argv) > 4:
                    if sys.argv[4] == '-sp':
                        bootloader_code = 0     # Only serial port test
                    else:
                        LogLibraryTest.test_library_invalid_argument()
                        ExitCode.invalid_argument()
                        return

            # Alight test type
            elif(t_type == TEST_TYPE_ALIGHT):
                
                alight_code = 1                 # Serial port and display test
                if len(sys.argv) > 4:
                    if sys.argv[4] == '-sp':
                        alight_code = 0         # Only serial port test
                    else:
                        LogLibraryTest.test_library_invalid_argument()
                        ExitCode.invalid_argument()
                        return

            else:
                LogLibraryTest.test_library_invalid_argument()
                ExitCode.invalid_argument()
                return
            
            # Execute the tests

            # Led test
            if (t_type == TEST_TYPE_LEDS):

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
            elif (t_type == TEST_TYPE_DISPLAY):
                
                result_display = SequenceTest.seq_display(model)
                
                # TODO: Log this
                if (result_display == 0):
                    print("Display tests passed successfully")
                elif (result_display == -1): 
                    print("Display tests failed")

            # Button test
            elif(t_type == TEST_TYPE_BUTTONS):
                
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
            elif(t_type == TEST_TYPE_BOARD_INFO):
                
                result_board = SequenceTest.seq_board_info(model, serial_number, manufacture_date, board_code)

                # TODO: Log this
                if(result_board == 0):
                    print("BoardInfo test passed successfully")
                elif(result_board == -1): 
                    print("BoardInfo test failed")

            # Bootloader_info test
            elif(t_type == TEST_TYPE_BOOTLOADER_INFO):

                result_bootloader = SequenceTest.seq_boot_loader_info(model, bootloader_code)

                # TODO: Log this
                if(result_bootloader == 0):
                    print("BootloaderInfo test passed successfully")
                elif(result_bootloader == -1): 
                    print("BootloaderInfo test failed")

            # Alight test
            elif(t_type == TEST_TYPE_ALIGHT):

                result_alight = SequenceTest.seq_alight(alight_code)

                # TODO: Log this
                if(result_alight == 0):
                    print("Alight test passed successfully")
                elif(result_alight == -1):
                    print("Alight test failed")

        # Default -> all tests
        else:

            if len(sys.argv) < 5 or len(sys.argv) > 6:
                LogLibraryTest.test_library_invalid_number_argument()
                ExitCode.invalid_number_of_arguments()
                return

            leds_name = None
            buttons_name = None
            all_code = True

            serial_number = sys.argv[3]
            serial_number = str(serial_number)

            manufacture_date = sys.argv[4]
            manufacture_date = str(manufacture_date)
            
            if len(sys.argv) > 5:
                if sys.argv[5] == '-sp':
                    all_code = False
                else:
                    LogLibraryTest.test_library_invalid_argument()
                    ExitCode.invalid_argument()
                    return
            
            result_all = SequenceTest.seq_all(model, serial_number, manufacture_date, all_code)   

            # TODO: Log this
            if(result_all == 0):
                print("All the tests passed successfully")
            elif(result_all == -1):
                print("At least one of the tests failed")

        return
    
    @staticmethod
    def check_model_name():
        name_model = sys.argv[2]        
        # Checks for bad model format
        if name_model[0].isdigit():
            LogLibraryTest.test_library_invalid_name()
            ExitCode.invalid_argument
            return None

        # Model doesn't exist
        if(df.open_model_xml(name_model) is None):
            LogLibraryTest.test_library_error_name(name_model)
            ExitCode.model_not_found()
            return None
        
        return Settings.get_model(name_model)
