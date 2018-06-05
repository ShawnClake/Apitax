# Import Drivers below here

from apitax.drivers.plugins import *


# End Driver Imports


# Factory class for creating HttpPlug Drivers
class HttpPlugFactory:

    @staticmethod
    def make(name):
        # import_submodules(drivers)
        constructor = globals()[name]
        return constructor()
