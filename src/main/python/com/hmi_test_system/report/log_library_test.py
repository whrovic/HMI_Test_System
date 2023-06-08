import logging


class LogLibraryTest:

    logger = logging.getLogger('LogLibraryTest')
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    @staticmethod
    def test_library_missing_name():
        LogLibraryTest.logger.info("No model name")

    @staticmethod
    def test_library_invalid_name():
        LogLibraryTest.logger.info("Invalid model name")

    @staticmethod
    def test_library_error_name(name_model):
        LogLibraryTest.logger.info(f"Model {name_model} doesn't exist")

    @staticmethod
    def test_library_invalid_argument():
        LogLibraryTest.logger.info("Invalid Argument")

    @staticmethod
    def test_library_invalid_number_argument():
        LogLibraryTest.logger.info("Invalid Number Arguments")
    