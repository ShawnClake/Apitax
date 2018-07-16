from apitax.drivers.plugins.BasicGit import BasicGitDriver
from apitax.drivers.plugins.BasicAuth import BasicAuthDriver

from apitax.drivers.plugins.ApitaxTests import ApitaxTestsDriver
from apitax.drivers.plugins.commandtax.ApitaxTestsCommands import ApitaxTestsCommands
from apitax.drivers.plugins.ApitaxInfo import ApitaxInfoDriver
from apitax.drivers.plugins.commandtax.ApitaxInfoCommands import ApitaxInfoCommands

from apitax.drivers.plugins.Openstack import OpenstackDriver

from apitax.drivers.plugins.Github import GithubDriver


from apitax.logs.Log import Log


class Drivers:

    drivers = None

    @staticmethod
    def initialize():
        Drivers.drivers = {
            "BasicGitDriver": BasicGitDriver(),
            "BasicAuthDriver": BasicAuthDriver(),

            "ApitaxTestsDriver": ApitaxTestsDriver(),
            "ApitaxTestsCommands": ApitaxTestsCommands(),
            "ApitaxInfoDriver": ApitaxInfoDriver(),
            "ApitaxInfoCommands": ApitaxInfoCommands(),

            "OpenstackDriver": OpenstackDriver(),

            "GithubDriver": GithubDriver(),
        }

    @staticmethod
    def add(name, driver):
        if(name == 'Default' or name == 'DefaultDriver'):
            Log().error("A driver cannot be named default for driver: " + name)
            return None
        Drivers.drivers[name] = driver

    @staticmethod
    def get(name):
        if (name not in Drivers.drivers):
            Log().error("Driver '" + name + "' does not exist or has not been imported/added.")
            return None
        return Drivers.drivers[name]
