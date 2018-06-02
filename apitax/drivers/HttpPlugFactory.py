# Import Drivers below here

from drivers import *


# End Driver Imports


# Factory class for creating HttpPlug Drivers
class HttpPlugFactory:

    @staticmethod
    def make(name):
        # import_submodules(drivers)
        constructor = globals()[name]
        return constructor()
