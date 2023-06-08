import logging


class LogLeds:

    logger = logging.getLogger('LogLeds')
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    @staticmethod
    def test_leds_sequence_colour_failed(model_LED, state_model_LED, state_failed_LED):
        LogLeds.logger.info(f"Error on LED: {model_LED}. It should be {state_model_LED}, got {state_failed_LED} instead.")
    
    @staticmethod
    def test_leds_sequence_state_failed(model_LED, state_model_LED, state_failed_LED):
        LogLeds.logger.info(f"Error on LED: {model_LED}. It should be {state_model_LED}, got {state_failed_LED} instead.")
    
    @staticmethod
    def test_failed(led_name):
        LogLeds.logger.error(f"Test Failed in LED {led_name}")

    @staticmethod
    def test_failed_off():
        LogLeds.logger.info("Test LEDs OFF Failed")

    @staticmethod
    def test_failed_on():
        LogLeds.logger.info("Test LEDs ON Failed")

    @staticmethod
    def test_leds_on_passed():
        LogLeds.logger.info("All the LEDs turned ON")

    @staticmethod
    def test_leds_off_passed():
        LogLeds.logger.info("All the LEDs turned OFF")

    @staticmethod
    def test_leds_sequence_passed():
        LogLeds.logger.info("Right Sequence: Yes")

    @staticmethod
    def test_leds_sequence_failed():
        LogLeds.logger.info("Right Sequence: No")

    @staticmethod
    def test_leds_finished():
        LogLeds.logger.info("TestLeds Finished")

    @staticmethod
    def test_leds_timeout():
        LogLeds.logger.info("Error Timeout")
