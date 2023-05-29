from .constant_exit_code import *


class ExitCode:
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        ExitCode.exit_code = OK
    
    @staticmethod
    def aborted():
        ExitCode.update_value(ABORTED)

    @staticmethod
    def failure_in_excetution():
        ExitCode.update_value(FAILURE_IN_EXECUTION)

    @staticmethod
    def xml_files_folder_not_found():
        ExitCode.update_value(XML_FILES_FOLDER_NOT_FOUND)

    @staticmethod
    def settings_folder_not_found():
        ExitCode.update_value(SETTINGS_FOLDER_NOT_FOUND)

    @staticmethod
    def model_not_found():
        ExitCode.update_value(MODEL_NOT_FOUND)

    @staticmethod
    def invalid_argument():
        ExitCode.update_value(INVALID_ARGUMENT)

    @staticmethod
    def invalid_number_of_arguments():
        ExitCode.update_value(INVALID_NUMBER_OF_ARGUMENTS)
    
    @staticmethod
    def led_name_not_found():
        ExitCode.update_value(LED_NAME_NOT_FOUND_IN_MODEL)
    
    @staticmethod
    def key_name_not_found():
        ExitCode.update_value(KEY_NAME_NOT_FOUND_IN_MODEL)
    
    @staticmethod
    def camera_connection_failure():
        ExitCode.update_value(CAMERA_CONNECTION_FAILURE)

    @staticmethod
    def camera_timeout_reception():
        ExitCode.update_value(CAMERA_TIMEOUT_RECEPTION)

    @staticmethod
    def serialport_connection_failure():
        ExitCode.update_value(SERIALPORT_CONNECTION_FAILURE)
    
    @staticmethod
    def serialport_timeout_reception():
        ExitCode.update_value(SERIALPORT_TIMEOUT_RECEPTION)

    @staticmethod
    def leds_test_not_passed():
        ExitCode.update_value(LEDS_TEST_NOT_PASSED)
    
    @staticmethod
    def leds_test_not_turn_all_on():
        ExitCode.update_value(LEDS_TEST_NOT_TURN_ALL_ON)

    @staticmethod
    def leds_test_not_turn_all_off():
        ExitCode.update_value(LEDS_TEST_NOT_TURN_ALL_OFF)

    @staticmethod
    def leds_test_colour_sequence_error():
        ExitCode.update_value(LEDS_TEST_COLOUR_SEQUENCE_ERROR)

    @staticmethod
    def leds_test_state_sequence_error():
        ExitCode.update_value(LEDS_TEST_STATE_SEQUENCE_ERROR)

    @staticmethod
    def leds_test_no_changes_timeout():
        ExitCode.update_value(LEDS_TEST_NO_CHANGES_TIMEOUT)
    
    @staticmethod
    def keys_test_not_passed():
        ExitCode.update_value(KEYS_TEST_NOT_PASSED)

    @staticmethod
    def keys_test_key_detected_consecutivelly():
        ExitCode.update_value(KEYS_TEST_KEY_DETECTED_CONSECUTIVELLY)

    @staticmethod
    def keys_test_key_detect_two_times():
        ExitCode.update_value(KEYS_TEST_KEY_DETECTED_TWO_TIMES)
    
    @staticmethod
    def keys_test_sequence_error():
        ExitCode.update_value(KEYS_TEST_SEQUENCE_ERROR)

    @staticmethod
    def keys_test_no_changes_timeout():
        ExitCode.update_value(KEYS_TEST_NO_CHANGES_TIMEOUT)

    @staticmethod
    def display_test_not_passed():
        ExitCode.update_value(DISPLAY_TEST_NOT_PASSED)

    @staticmethod
    def display_test_pix_not_passed():
        ExitCode.update_value(DISPLAY_TEST_PIX_NOT_PASSED)

    @staticmethod
    def display_test_chr_not_passed():
        ExitCode.update_value(DISPLAY_TEST_CHR_NOT_PASSED)

    @staticmethod
    def display_test_pal_not_passed():
        ExitCode.update_value(DISPLAY_TEST_PAL_NOT_PASSED)

    @staticmethod
    def bootloader_test_not_passed():
        ExitCode.update_value(BOOTLOADER_TEST_NOT_PASSED)

    @staticmethod
    def board_info_test_not_passed():
        ExitCode.update_value(BOARD_INFO_TEST_NOT_PASSED)

    @staticmethod
    def alight_test_not_passed():
        ExitCode.update_value(ALIGHT_TEST_NOT_PASSED)
    
    @staticmethod
    def update_value(new):
        if ExitCode.exit_code is OK:
            ExitCode.exit_code = new