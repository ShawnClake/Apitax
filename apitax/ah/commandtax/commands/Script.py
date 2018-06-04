
# Application import
from apitax.logs.Log import Log
from apitax.ah.commandtax.Request import Request
from apitax.ah.scriptax.Scriptax import Scriptax


# TODO:
#  Change the way request is saved to include status code & command run
#  Add additional syntaxes for import & exporting


# Script is used to automate the execution of many commands
class Script(Request):
    def __init__(self, config, header, debug, sensitive):
        Request.__init__(self, '', header.get(), '', debug=debug, sensitive=sensitive)
        self.config = config
        self.header = header
        self.debug = debug
        self.sensitive = sensitive
        self.scriptax = Scriptax(self.config, self.header, self.debug, self.sensitive)
        
    def handle(self, command):
        returnedVisitor = self.scriptax.execute(command[0])
        # Todo: Generate a suitable response for the command and save it into the inheirted request obj
        # Possibly just a status code & the dataStore object saved in the visitor