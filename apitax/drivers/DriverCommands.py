# Base class for driver command classes
class DriverCommands(object):

    def handle(self, header, command, debug=False, sensitive=False):
        self.header = header
        self.command = command
        self.debug = debug
        self.sensitive = sensitive
        self.request = None

    def getRequest(self):
        return self.request
