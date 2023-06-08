import logging


class LogButton:

    logger = logging.getLogger('LogButtons')
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    @staticmethod
    def button_test_serial_error(button_name):
        LogButton.logger.info(f"Error in button {button_name}")

    @staticmethod
    def button_test_serial_error_final():
        LogButton.logger.info("Error on Button Test")

    @staticmethod
    def button_test_serial_pass():
        LogButton.logger.info("Button Test Serial passed")
