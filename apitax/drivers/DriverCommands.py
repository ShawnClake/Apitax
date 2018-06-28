# Base class for driver command classes

from apitax.utilities.Files import getPath

class DriverCommands():

    def setup(self, config, header, auth, parameters, debug=False, sensitive=False):
        self.config = config
        self.header = header
        self.auth = auth
        self.debug = debug
        self.sensitive = sensitive
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
        
    def handle(self, command):
        from apitax.ah.commandtax.commands.Script import Script
        if(self.override(command)):
            return
        self.request = Script(self.config, self.header, self.auth, self.parameters, self.debug, self.sensitive)
        path = self.basePath
        for element in command:
            path += '/' + element
        path += '.ah'
        path = getPath(path)
        self.request.handle([path])
        return self.request