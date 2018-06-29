# Base class for driver command classes

from apitax.utilities.Files import getPath
from apitax.utilities.Files import getAllFiles
from apitax.ah.Options import Options

class DriverCommands():

    def setup(self, config, header, auth, parameters, options=Options()):
        self.config = config
        self.header = header
        self.auth = auth
        self.options = options
        self.request = None
        self.parameters = parameters
        if(self.getDriverPath() is None):
            self.basePath = str(config.path) + '/drivers/plugins/commandtax/' + self.getDriverName()
        else:
            self.basePath = self.getDriverPath() + '/' + self.getDriverName()
        self.basePath = getPath(self.basePath)
        return self
        
    def getDriverName(self):
        return None
        
    def getDriverPath(self):
        return None

    def getRequest(self):
        return self.request
        
    def override(self, command: list):
        return False
        
    def getCatalog(self):
        path = self.basePath
        baseLength = len(path)
        files = getAllFiles(path+"/**/*.ah")
        catalog = []
        for file in files:
            fPath = getPath(file)
            command = fPath[baseLength+1:-3].replace('/', ' ').replace('\\', ' ')
            catalog.append(command)
        return catalog
        
    def handle(self, command):
        from apitax.ah.commandtax.commands.Script import Script
        if(self.override(command)):
            return
        self.request = Script(self.config, self.header, self.auth, self.parameters, self.options)
        path = self.basePath
        i = 0
        for element in command:
            element = element.strip()
            if(element == '--driver'):
                i += 2
            elif(element[:2] == '--'):
                i += 1
                
            if(i > 0):
                i -= 1
            else:
                path += '/' + element
            #print(element+":"+str(i))
        path += '.ah'
        path = getPath(path)
        self.request.handle([path])
        return self.request