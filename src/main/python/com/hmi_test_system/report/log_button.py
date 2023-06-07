import logging


class LogButton:

    # prints for button tests

    def __init__(self):
        self.logger = logging.getLogger('LogButtons')
        self.logger.setLevel(logging.DEBUG)
        self.handler = logging.StreamHandler()
        self.handler.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)

    def button_test_serial_error(self, button_name):
        self.logger.info(f"Error in button {button_name}")

    def button_test_serial_error_final(self):
        self.logger.info("Error on Button Test")

    def button_test_serial_pass(self):
        self.logger.info("Button Test Serial passed")
