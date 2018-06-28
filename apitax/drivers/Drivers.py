
from apitax.drivers.plugins.ApitaxTests import ApitaxTestsDriver

from apitax.drivers.plugins.commandtax.ApitaxTestsCommands import ApitaxTestsCommands


class Drivers:
    drivers = {
        "ApitaxTestsDriver": ApitaxTestsDriver(),
        "ApitaxTestsCommands": ApitaxTestsCommands()
    }
    
    def add(name, driver):
        Drivers.drivers[name] = driver
    
    def get(name):
        return Drivers.drivers[name]
    
        