from .log import Log

class LogSequenceTest(Log):

    @staticmethod
    def sequence_test_invalid_parameters():
        Log.info_log("Invalid Parameter: Parameter is None")

    @staticmethod
    def button_not_found():
        Log.info_log("Button not found")

    @staticmethod
    def led_not_found():
        Log.info_log("Led not found")