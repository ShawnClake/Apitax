from apitax.drivers.plugins.ApitaxTests import ApitaxTestsDriver
from apitax.drivers.plugins.commandtax.ApitaxTestsCommands import ApitaxTestsCommands
from apitax.drivers.plugins.Openstack import OpenstackDriver
from apitax.drivers.plugins.Default import DefaultDriver
from apitax.drivers.plugins.DefaultGit import DefaultGitDriver

from apitax.logs.Log import Log

class Drivers:
    drivers = {
        "ApitaxTestsDriver": ApitaxTestsDriver(),
        "ApitaxTestsCommands": ApitaxTestsCommands(),
        "OpenstackDriver": OpenstackDriver(),
        "DefaultDriver": DefaultDriver(),
        "DefaultGitDriver": DefaultGitDriver(),
    }
    
    def add(name, driver):
        Drivers.drivers[name] = driver
    
    def get(name):
        if(name not in Drivers.drivers):
            Log().error("Driver '" + name + "' does not exist or has not been imported/added.")
        return Drivers.drivers[name]
    
        