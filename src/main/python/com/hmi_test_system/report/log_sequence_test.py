from log import Log

class LogSequenceTest(Log):

    @staticmethod
    def sequence_test_invalid_parameters():
        Log.info_log("Invalid Parameter: Parameter is None")

    #@staticmethod
    #def