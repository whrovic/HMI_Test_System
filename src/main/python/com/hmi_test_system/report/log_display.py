from .log import Log


class LogDisplay(Log):

    @staticmethod
    def start_test(test_name):
        Log.info_log(f"Starting {test_name}")

    @staticmethod
    def test_failed(test_name):
        Log.error_log(f"{test_name} Test Failed")

    @staticmethod
    def test_passed(test_name):
        Log.info_log(f"{test_name} Test Passed")

    @staticmethod
    def test_finished():
        Log.info_log("TestDisplay Finished")
    