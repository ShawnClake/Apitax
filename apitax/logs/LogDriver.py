

class LogDriver:
	
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
	
	
    def __init__ (self):
        self.logger = None
        self.settings = None
        self.buffer = []
        
    def setSettings(self, settings):
        self.settings = settings
        
    def setLogger(self, logger):
        self.logger = logger
        
    def log(self, line, type='info'):
        pass
        
    def outputLog(self):
        pass
        
    def injectStdColor(self, text):
        text = str(text)
        
        if(not self.settings.get('colorize')):
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