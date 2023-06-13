from .log import Log


class LogButton(Log):

    @staticmethod
    def button_test_serial_pass(type):
        Log.info_log(f"Keys Test [{type}]: Test Passed")

    @staticmethod
    def button_test_serial_error_final(type, expected_button):
        Log.error_log(f"Keys Test [{type}]: Received end of tests, instead of {expected_button}")

    @staticmethod
    def button_test_sequence_failed(type, button_name, expected_button):
        Log.error_log(f"Keys Test [{type}]: Received {button_name} instead of {expected_button}")

    @staticmethod
    def button_test_detected_consecutivelly(type, received_button, expected_button):
        Log.error_log(f"Keys Test [{type}]: Received {received_button} consecutivelly, instead of {expected_button}")

    @staticmethod
    def button_test_detected_button_after_end(type, button_name):
        Log.error_log(f"Keys Test [{type}]: Received {button_name} but all the buttons were already received")

    @staticmethod
    def button_test_detected_two_times(type, button_name, expected_button):
        Log.error_log(f"Keys Test [{type}]: Error received {button_name} for the 2nd time, instead of {expected_button}")

    @staticmethod
    def button_tests_canceled(type):
        Log.info_log("Keys Test [{type}]: Canceled by the user")

    @staticmethod
    def button_test_unrelated_data(type):
        Log.error_log(f"Keys Test [{type}]: Received data not related to the current test")

    @staticmethod
    def button_test_sp_timeout(type):
        Log.error_log(f"Keys Test [{type}]: SP timeout")
