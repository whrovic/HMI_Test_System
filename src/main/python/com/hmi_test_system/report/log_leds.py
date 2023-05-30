import logging


class LogLeds:
    def __init__(self):
        self.logger = logging.getLogger('LogLEDs')
        self.logger.setLevel(logging.DEBUG)
        self.handler = logging.StreamHandler()
        self.handler.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)

    def test_leds_sequence_colour_failed(self, model_LED, state_model_LED, state_failed_LED):
        self.logger.info(f"Error on LED: {model_LED}. It should be {state_model_LED}, got {state_failed_LED} instead.")

    def test_leds_sequence_state_failed(self, model_LED, state_model_LED, state_failed_LED):
        self.logger.info(f"Error on LED: {model_LED}. It should be {state_model_LED}, got {state_failed_LED} instead.")
    def test_failed(self):
        self.logger.warning("Test Failed")

    def test_leds_on_passed(self):
        self.logger.info("All the LEDs turned ON")

    def test_leds_off_passed(self):
        self.logger.info("All the LEDs turned OFF")

    def test_leds_sequence_passed(self):
        self.logger.info("Right Sequence: Yes")

    def test_leds_sequence_failed(self):
        self.logger.info("Right Sequence: No")

    def test_canceled(self):
        self.logger.warning("TestLeds Canceled")

    def test_finished(self):
        self.logger.info("TestLeds Finished")
