# Base class for driver command classes
class DriverCommands(object):

    def handle(self, config, header, command, debug=False, sensitive=False):
        self.config = config
        self.header = header
        self.command = command
        self.debug = debug
        self.sensitive = sensitive
        self.request = None

    def getRequest(self):
        return self.request
