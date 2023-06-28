import logging
import sys
from datetime import datetime
from data.path import Path


class Log:
    logger = logging.getLogger('Log')
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.DEBUG)
    stdout_handler.setFormatter(formatter)

    file_name = datetime.now().strftime(Path.get_logs_directory() + '/log_%Y_%m_%d_%H_%M.log')
    file_handler = logging.FileHandler(file_name)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger.addHandler(stdout_handler)
    logger.addHandler(file_handler)

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

    @staticmethod
    def serial_port_closed():
        Log.error_log("Serial Port closed")

    @staticmethod
    def display_camera_closed():
        Log.error_log("Display camera closed")

    @staticmethod
    def leds_camera_closed():
        Log.error_log("Leds camera closed")

    @staticmethod
    def timeout():
        Log.info_log("Timeout tests didn't start")
    
    # TODO: not use generic log, swap all that using it
    @staticmethod
    def generic(str):
        Log.info_log(str)
