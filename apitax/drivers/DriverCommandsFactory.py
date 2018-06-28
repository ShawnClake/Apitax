# Import Command Drivers
from apitax.drivers.Drivers import Drivers


# Used to create driver command instances
class DriverCommandsFactory:

    @staticmethod
    def make(name):
        return Drivers.get(name)

    #@staticmethod
    #def make(name):
    #    if (name in globals()):
    #        constructor = globals()[name]
    #        return constructor()
    #    return None
