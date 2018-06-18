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

    WHITE = '\033[97m'
    CYAN = '\033[96m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def __init__(self, logFile = "logs/log.log", doLog=True, logColorize=True):
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

            loggers.update({'main': app_log, 'settings':{'doLog': doLog, 'colorize':logColorize,'path':directorypath.resolve()}})

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

    def log(self, text, prefix=''):
        # logging.info(' '+text)
        text = self.inject(text, prefix)
        if(loggers.get('settings').get('doLog')):
            loggers.get('main').info(text)
            print(self.injectStdColor(text))

    def error(self, text, prefix=''):
        # logging.info(' '+text)
        text = self.inject(text, prefix)
        if(loggers.get('settings').get('doLog')):
            loggers.get('main').info('### Error: ' + text)
            print(self.injectStdColor('### Error: ' + text))
        
    def getLogger(self):
        return loggers.get('main')
        
    def getLoggerSettings(self):
        return loggers.get('settings')
        
    def injectStdColor(self, text):
        text = str(text)
        
        if(not self.getLoggerSettings().get('colorize')):
            return text
        
        if(text[:3] == '>>>'):
            return self.HEADER + text + self.ENDC
        elif(text[:2] == '>>'):
            return self.OKBLUE + text + self.ENDC
        elif(text[:1] == '>'):
            if(text[:17] == '> Now processing:'):
                return self.OKGREEN + text + self.ENDC
            else:
                return self.WARNING + text + self.ENDC
        elif(text[:3] == '###'):
            return self.FAIL + text + self.ENDC
        elif(text.strip()[:1] == '*'):
            return self.CYAN + text + self.ENDC
            
        return self.WHITE + text + self.ENDC
        
    def stripColor(self, text):
        ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
        return ansi_escape.sub('', text)
        
