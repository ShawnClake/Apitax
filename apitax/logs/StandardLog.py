
from apitax.logs.LogDriver import LogDriver

class StandardLog(LogDriver):
    def __init__ (self):
        super().__init__()
        
    def log(self, line, type='info'):
        self.logger.info(line)
        print(self.injectStdColor(line))
