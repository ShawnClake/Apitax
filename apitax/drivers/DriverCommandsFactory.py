# Import Command Drivers
from apitax.drivers.plugins.commandtax import *


# Used to create driver command instances
class DriverCommandsFactory:

    @staticmethod
    def make(name):
        if (name in globals()):
            constructor = globals()[name]
            return constructor()
        return None
