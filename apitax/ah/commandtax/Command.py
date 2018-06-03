# System import
import shlex

# Application import
from apitax.ah.commandtax.commands.Script import Script
from apitax.ah.commandtax.commands.Custom import Custom
from apitax.drivers.DriverCommandsFactory import DriverCommandsFactory


# Command is used to distribute the workload amoung a heirarchy of possible handlers
# Command is the 'brain' of the application
class Command:
    def __init__(self, header, command, config, debug=False, sensitive=False):

        if (type(command) is not list):
            command = shlex.split(command.strip())
        if (len(command) < 1):
            return
        self.request = None
        if (command[0] == 'script'):
            self.request = Script(header, debug, sensitive)
            self.request.setConfig(config)
        elif (command[0] == 'custom'):
            self.request = Custom(header, debug, sensitive)
        else:
            customCommands = DriverCommandsFactory.make(config.get('driver') + 'Commands')

            self.request = customCommands.handle(header, command, debug, sensitive)
        self.request.handle(command[1:])

    def getRequest(self):
        return self.request
