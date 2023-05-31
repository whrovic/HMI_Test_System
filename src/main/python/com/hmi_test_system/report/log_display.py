import logging

class LogDisplay:

     #prints for display tests

    def __init__(self):
        self.logger = logging.getLogger('LogDisplay')
        self.logger.setLevel(logging.DEBUG)
        self.handler = logging.StreamHandler()
        self.handler.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)

    def start_test(self, test_name):
        self.logger.info(f"Starting {test_name}")

    def test_failed(self, test_name):
        self.logger.warning(f"{test_name} Test Failed")

    def test_passed(self, test_name):
        self.logger.info(f"{test_name} Test Passed")

    def test_canceled(self):
        self.logger.warning("TestDisplay Canceled")

    def test_finished(self):
        self.logger.info("TestDisplay Finished")
   