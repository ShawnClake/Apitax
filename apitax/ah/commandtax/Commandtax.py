# System import
import shlex

# Application import
from apitax.ah.commandtax.commands.Script import Script
from apitax.ah.commandtax.commands.Custom import Custom
from apitax.drivers.DriverCommandsFactory import DriverCommandsFactory


# Command is used to distribute the workload amoung a heirarchy of possible handlers
# Command is the 'brain' of the application
class Commandtax:
    def __init__(self, header, command, config, debug=False, sensitive=False):

        if (type(command) is not list):
            command = shlex.split(command.strip())
        if (len(command) < 1):
            return
        self.request = None
        if (command[0] == 'script'):
            self.request = Script(config, header, debug, sensitive)
        elif (command[0] == 'custom'):
            self.request = Custom(config, header, debug, sensitive)
        else:
            customCommands = DriverCommandsFactory.make(config.get('driver') + 'Commands')
            self.request = customCommands.handle(config, header, command, debug, sensitive)
            
        self.request.handle(command[1:])

    def getRequest(self):
        return self.request
