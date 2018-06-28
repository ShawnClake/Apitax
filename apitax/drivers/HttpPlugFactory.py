# Import Drivers below here

from apitax.drivers.Drivers import Drivers


# End Driver Imports


# Factory class for creating HttpPlug Drivers
class HttpPlugFactory:

    @staticmethod
    def make(name):
        return Drivers.get(name)

    #@staticmethod
    #def make(name):
    #    # import_submodules(drivers)
    #    constructor = globals()[name]
    #    return constructor()
