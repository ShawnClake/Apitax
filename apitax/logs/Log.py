# System import
import logging
from logging.handlers import RotatingFileHandler

# Logging object to prevent duplicate handler adding
# global loggers
loggers = {}


# Handles printing to CLI as well as printing to log file
class Log:
    def __init__(self, logFile = "logs/log.log"):
        # logging.basicConfig(filename=filepath,level=logging.INFO)
        # log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s')

        if (not loggers.get('main')):
            log_formatter = logging.Formatter('%(asctime)s %(levelname)s  %(message)s')

            # Each log file can be up to 25MB big and keeps a max of 3 backup files.
            # Thus, the largest size of the log folder is 100MB
            my_handler = RotatingFileHandler(logFile, mode='a', maxBytes=25 * 1024 * 1024,
                                             backupCount=3, encoding=None, delay=0)
            my_handler.setFormatter(log_formatter)
            my_handler.setLevel(logging.INFO)

            app_log = logging.getLogger('root')
            app_log.setLevel(logging.INFO)

            app_log.addHandler(my_handler)
            loggers.update({'main': app_log})

    def log(self, text):
        # logging.info(' '+text)
        loggers.get('main').info(text)
        print(text)

    def error(self, text):
        # logging.info(' '+text)
        loggers.get('main').info('### Error: ' + text)
        print('### Error: ' + text)
