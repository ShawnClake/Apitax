
# Application import
from apitax.logs.Log import Log
from apitax.ah.commandtax.Request import Request
from apitax.ah.scriptax.Scriptax import Scriptax

from time import time
from apitax.utilities.Numbers import round2str
from apitax.ah.Options import Options

# TODO:
#  Change the way request is saved to include status code & command run
#  Add additional syntaxes for import & exporting


# Script is used to automate the execution of many commands
class Script(Request):
    def __init__(self, config, header, auth, parameters, options):
        Request.__init__(self, '', header.get(), '', options=options, customResponse=True)
        self.config = config
        self.header = header
        self.auth = auth
        self.options = options
        self.parameters = parameters
        self.scriptax = Scriptax(self.config, self.header, self.auth, self.parameters, self.options)
        self.parser = None
        self.executionTime = None
        self.log = Log()
        
    def handle(self, command):
        t0 = time()
        self.parser = self.scriptax.execute(command[0])
        self.executionTime = time() - t0
        if(self.options.debug):
            self.log.log('>> Script Finished Processing in ' + round2str(self.executionTime) + 's')
            self.log.log('')
        #print("thing: " + self.parser)
        self.request = {}
        self.request['text'] = {}
        self.request['text']['result'] = self.parser.data.getStore()
        self.request['text']['commandtax'] = command[0]
        self.request['text']['execution-time'] = round2str(self.executionTime)
        if(self.parser.isError()):
            self.request['text']['error'] = self.parser.data.getError()
            self.request['status_code'] = 500
        else:
            self.request['status_code'] = 200

        # Todo: Generate a suitable response for the command and save it into the inheirted request obj
        # Possibly just a status code & the dataStore object saved in the visitor