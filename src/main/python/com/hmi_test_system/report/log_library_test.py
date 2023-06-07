import logging


class LogLibraryTest:

    # prints for library tests

    def __init__(self):
        self.logger = logging.getLogger('LogLibraryTest')
        self.logger.setLevel(logging.DEBUG)
        self.handler = logging.StreamHandler()
        self.handler.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)

    def test_library_missing_name(self):
        self.logger.info("No model name")

    def test_library_invalid_name(self):
        self.logger.info("Invalid model name")

    def test_library_error_name(self, name_model):
        self.logger.info(f"Model {name_model} doesn't exist")

    def test_library_invalid_argument(self):
        self.logger.info("Invalid Argument")

    def test_library_invalid_number_argument(self):
        self.logger.info("Invalid Number Arguments")