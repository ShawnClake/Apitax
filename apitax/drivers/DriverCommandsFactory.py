# Import Drivers
from ahRequests.drivers import *


# Used to create driver command instances
class DriverCommandsFactory:

    @staticmethod
    def make(name):
        if (name in globals()):
            constructor = globals()[name]
            return constructor()
        return False
