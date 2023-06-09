from .log import Log


class LogLibraryTest(Log):

    @staticmethod
    def test_library_missing_name():
        Log.info_log("No model name")

    @staticmethod
    def test_library_invalid_name():
        Log.info_log("Invalid model name")

    @staticmethod
    def test_library_error_name(name_model):
        Log.info_log(f"Model {name_model} doesn't exist")

    @staticmethod
    def test_library_invalid_argument():
        Log.info_log("Invalid Argument")

    @staticmethod
    def test_library_invalid_number_argument():
        Log.info_log("Invalid Number Arguments")