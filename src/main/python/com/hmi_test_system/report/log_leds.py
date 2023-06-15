from .log import Log


class LogLeds(Log):

    @staticmethod
    def test_leds_sequence_colour_failed(model_LED, state_model_LED, state_failed_LED):
        Log.info_log(f"Error on LED: {model_LED}. It should be {state_model_LED}, got {state_failed_LED} instead.")
    
    @staticmethod
    def test_leds_sequence_state_failed(model_LED, state_model_LED, state_failed_LED):
        Log.info_log(f"Error on LED: {model_LED}. It should be {state_model_LED}, got {state_failed_LED} instead.")
    
    @staticmethod
    def test_failed(led_name):
        Log.error_log(f"Test Failed in LED {led_name}")

    @staticmethod
    def test_failed_off():
        Log.error_log("Test LEDs OFF Failed")

    @staticmethod
    def test_failed_on():
        Log.error_log("Test LEDs ON Failed")

    @staticmethod
    def test_leds_on_passed():
        Log.info_log("All the LEDs turned ON")

    @staticmethod
    def test_leds_off_passed():
        Log.info_log("All the LEDs turned OFF")

    @staticmethod
    def test_leds_sequence_passed():
        Log.info_log("Right Sequence: Yes")

    @staticmethod
    def test_leds_sequence_failed():
        Log.error_log("Right Sequence: No")

    @staticmethod
    def test_leds_sequence_not_completed():
        Log.error_log("The sequence wasn't completed before the end of the tests")

    @staticmethod
    def test_leds_finished():
        Log.info_log("TestLeds Finished")
    
    @staticmethod
    def test_leds_detected(led_name, colour_name):
        Log.info_log(f"Correctly detected {colour_name} in {led_name}")