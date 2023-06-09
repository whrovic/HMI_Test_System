from .log import Log


class LogButton(Log):

    @staticmethod
    def button_test_serial_error(button_name):
        Log.error_log(f"Error in button {button_name}")

    @staticmethod
    def button_test_serial_error_final():
        Log.error_log("Error on Button Test")

    @staticmethod
    def button_test_serial_pass():
        Log.info_log("Button Test Serial passed")
