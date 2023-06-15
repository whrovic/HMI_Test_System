from .log import Log

class LogSequenceTest(Log):

    @staticmethod
    def sequence_test_invalid_parameters():
        Log.error_log("Invalid Parameter: Parameter is None")

    @staticmethod
    def image_none():
        Log.error_log("Images Reference is None")

    @staticmethod
    def button_not_found():
        Log.error_log("Button not found")

    @staticmethod
    def led_not_found():
        Log.error_log("Led not found")

    @staticmethod
    def start_buttons_test():
        Log.info_log("Buttons Tests started")

    @staticmethod
    def start_board_info_test():
        Log.info_log("Board Info Test started")

    @staticmethod
    def start_boot_loader_test():
        Log.info_log("Bootloader Test started")

    @staticmethod
    def start_test_alight():
        Log.info_log("Light Test started")

    @staticmethod
    def start_test_leds():
        Log.info_log("Leds Tests started")

    @staticmethod
    def start_test_display():
        Log.info_log("Display Tests started")