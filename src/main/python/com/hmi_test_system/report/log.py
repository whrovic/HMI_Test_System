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