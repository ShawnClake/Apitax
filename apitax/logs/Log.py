# System import
import logging
import re
from logging.handlers import RotatingFileHandler
from pathlib import Path

# Logging object to prevent duplicate handler adding
# global loggers
loggers = {}


# Handles printing to CLI as well as printing to log file
class Log:

    def __init__(self, logDriver=None, logFile='logs/apitax.log', doLog=True, logColorize=True, logPrefixes=True, logHumanReadable=False):
        # logging.basicConfig(filename=filepath,level=logging.INFO)
        # log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s')

        self.prefix = ''

        if (not loggers.get('main')):

            directorypath = Path(logFile)
            # print("/".join(directorypath.parts[:-1]))
            Path("/".join(directorypath.parts[:-1])).mkdir(parents=True, exist_ok=True) 

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

            loggers.update({'main': app_log, 'driver': logDriver, 'settings':{'doLog': doLog, 'colorize':logColorize, 'prefixes':logPrefixes, 'human-readable': logHumanReadable, 'path':directorypath.resolve()}})

            logDriver.setLogger(self.getLogger())
            logDriver.setSettings(self.getLoggerSettings())
                        

    def inject(self, text, prefix=''):
        
        if(prefix == ''):
            prefix = self.prefix
        
        if(prefix == '' or text == ''):
            return text

        text = str(text)

        if (text[:3] == '>>>' or text[:3] == '###'):
            return text[:3] + ' ' + prefix + ' ' + text[3:]
        elif (text[:2] == '>>'):
            return text[:2] + ' ' + prefix + ' ' + text[2:]
        elif (text[:1] == '>' or text.strip()[:1] == '*'):
            return text[:1] + ' ' + prefix + ' ' + text[1:]

        return prefix + ' ' + text

    def isLoggable(self, prefix=''):
        if((prefix != '' or self.prefix != '') and not loggers.get('settings').get('prefixes')):
            return False
        return loggers.get('settings').get('doLog')

    def log(self, text, prefix=''):
        # logging.info(' '+text)
        text = self.inject(text, prefix)
        if(self.isLoggable(prefix)):
            self.getLoggerDriver().log(text)

    def error(self, text, prefix=''):
        # logging.info(' '+text)
        text = self.inject(text, prefix)
        if(self.isLoggable(prefix)):
            self.getLoggerDriver().log('### Error: ' + text)
        
    def getLogger(self):
        return loggers.get('main')
        
    def getLoggerSettings(self):
        return loggers.get('settings')
        
    def getLoggerDriver(self):
        return loggers.get('driver')
        

        
