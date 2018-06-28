from apitax.drivers.plugins.ApitaxTests import ApitaxTestsDriver

from apitax.drivers.plugins.commandtax.ApitaxTestsCommands import ApitaxTestsCommands

from apitax.drivers.plugins.Openstack import OpenstackDriver

from apitax.drivers.plugins.Default import DefaultDriver

class Drivers:
    drivers = {
        "ApitaxTestsDriver": ApitaxTestsDriver(),
        "ApitaxTestsCommands": ApitaxTestsCommands(),
        "OpenstackDriver": OpenstackDriver(),
        "DefaultDriver": DefaultDriver(),
    }
    
    def add(name, driver):
        Drivers.drivers[name] = driver
    
    def get(name):
        return Drivers.drivers[name]
    
        