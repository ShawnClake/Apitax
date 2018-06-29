# System import
import shlex

# Application import
from apitax.ah.commandtax.commands.Script import Script
from apitax.ah.commandtax.commands.Custom import Custom
from apitax.ah.LoadedDrivers import LoadedDrivers
from apitax.ah.Credentials import Credentials
from apitax.ah.Options import Options


# Command is used to distribute the workload amoung a heirarchy of possible handlers
# Command is the 'brain' of the application
class Commandtax:
    def __init__(self, header, command, config, options=Options(), parameters={}, auth=Credentials()):

        if (type(command) is not list):
            command = shlex.split(command.strip())
        if (len(command) < 1):
            return
        self.request = None
        
        if('--debug' in command):
            options.debug = True
        if('--sensitive' in command):
            options.sensitive = True
        if ('--driver' in command):
            options.driver = command[command.index('--driver') + 1]
        
        if (command[0] == 'script'):
            self.request = Script(config, header, auth, parameters, options)
        elif (command[0] == 'custom'):
            self.request = Custom(config, header, auth, parameters, options)
        else:
            if(options.driver):
                customCommands = LoadedDrivers.getCommandsDriver(options.driver)
            else:
                customCommands = LoadedDrivers.getDefaultCommandsDriver()
            self.request = customCommands.setup(config, header, auth, parameters, options)
            self.request = self.request.handle(command)
            return
            #command.insert(0, 'driver')
            
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
