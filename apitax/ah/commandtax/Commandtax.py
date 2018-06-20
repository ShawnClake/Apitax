# System import
import shlex

# Application import
from apitax.ah.commandtax.commands.Script import Script
from apitax.ah.commandtax.commands.Custom import Custom
from apitax.drivers.DriverCommandsFactory import DriverCommandsFactory


# Command is used to distribute the workload amoung a heirarchy of possible handlers
# Command is the 'brain' of the application
class Commandtax:
    def __init__(self, header, command, config, debug=False, sensitive=False, parameters={}):

        if (type(command) is not list):
            command = shlex.split(command.strip())
        if (len(command) < 1):
            return
        self.request = None
        
        if('--debug' in command):
            debug = True
        if('--sensitive' in command):
            sensitive = True
        
        if (command[0] == 'script'):
            self.request = Script(config, header, parameters, debug, sensitive)
        elif (command[0] == 'custom'):
            self.request = Custom(config, header, parameters, debug, sensitive)
        else:
            customCommands = DriverCommandsFactory.make(config.get('driver') + 'Commands')
            self.request = customCommands.handle(config, header, parameters, command, debug, sensitive)
            
        self.request.handle(command[1:])

    def getRequest(self):
        return self.request

    def getReturnedData(self):
        returned = None
        if (isinstance(self.getRequest(), Script)):
            returned = self.getRequest().parser.data.getReturn()
        if (returned is not None):
            return returned
        else:
            return self.getRequest().getResponseBody()
