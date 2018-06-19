
from apitax.logs.LogDriver import LogDriver

class BufferedLog(LogDriver):
    def __init__ (self):
        self.buffer = []
        super().__init__()
        
    def log(self, line, type='info'):
        self.buffer.append({'line': line, 'type': type})
        	
    def outputLog(self):
        for line in self.buffer:
            self.logger.info(line['line'])
            print(self.injectStdColor(line['line']))
        self.buffer = []