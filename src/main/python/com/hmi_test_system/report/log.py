import logging


class Log:
    logger = logging.getLogger('Log')
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    @staticmethod
    def info_log(message):
        Log.logger.info(message)

    @staticmethod
    def warning_log(message):
        Log.logger.warning(message)

    @staticmethod
    def error_log(message):
        Log.logger.error(message)

    @staticmethod
    def serial_port_connected():
        Log.info_log("Serial port connected successfully")
    
    @staticmethod
    def display_camera_connected():
        Log.info_log("Display camera connected successfully")

    @staticmethod
    def leds_camera_connected():
        Log.info_log("Leds camera connected successfully")
