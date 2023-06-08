import logging

class LogDisplay:

    logger = logging.getLogger('LogDisplay')
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    @staticmethod
    def start_test(test_name):
        LogDisplay.logger.info(f"Starting {test_name}")

    @staticmethod
    def test_failed(test_name):
        LogDisplay.logger.warning(f"{test_name} Test Failed")

    @staticmethod
    def test_passed(test_name):
        LogDisplay.logger.info(f"{test_name} Test Passed")

    @staticmethod
    def test_canceled():
        LogDisplay.logger.warning("TestDisplay Canceled")

    @staticmethod
    def test_finished():
        LogDisplay.logger.info("TestDisplay Finished")
    