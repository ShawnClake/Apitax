from apitax.drivers.Drivers import Drivers
from apitax.logs.Log import Log
from apitax.ah.State import State


class LoadedDrivers:
    drivers = {}

    default = {}

    @staticmethod
    def load(name):
        setDefaultDrivers = False
        if (not LoadedDrivers.default):
            setDefaultDrivers = True

        if (name + 'Driver' not in Drivers.drivers):
            Log().error("Driver '" + name + 'Driver' + "' does not exist or has not been imported/added.")
            return

        LoadedDrivers.drivers[name + 'Driver'] = Drivers.get(name + 'Driver')

        if (setDefaultDrivers):
            LoadedDrivers.default['base'] = Drivers.get(name + 'Driver')

        Log().log("> Driver '" + name + 'Driver' + "' is loaded.")
        Log().log('')

        if (name + 'Commands' in Drivers.drivers):
            LoadedDrivers.drivers[name + 'Commands'] = Drivers.get(name + 'Commands')
            Log().log("> Driver '" + name + 'Commands' + "' is loaded.")
            Log().log('')

            if (setDefaultDrivers):
                LoadedDrivers.default['commands'] = Drivers.get(name + 'Commands')

    @staticmethod
    def getDefaultBaseDriver():
        return LoadedDrivers.default['base']

    @staticmethod
    def getDefaultCommandsDriver():
        if ('commands' in LoadedDrivers.default):
            return LoadedDrivers.default['commands']
        else:
            Log().error('No default command driver is loaded')

    @staticmethod
    def getPrimaryDriver():
        if (not State.config.has("drivers-primary") or State.config.get("drivers-primary") == "default"):
            return LoadedDrivers.getDefaultBaseDriver()
        return LoadedDrivers.getBaseDriver(State.config.get('drivers-primary') + 'Driver')

    @staticmethod
    def getAuthDriver():
        if (not State.config.has("drivers-auth") or State.config.get("drivers-auth") == "default"):
            return LoadedDrivers.getDefaultBaseDriver()
        return LoadedDrivers.getBaseDriver(State.config.get('drivers-auth') + 'Driver')

    @staticmethod
    def getBaseDriver(name):
        if (name not in Drivers.drivers):
            Log().error("Driver '" + name + "' has not been loaded.")
        return LoadedDrivers.drivers[name]

    @staticmethod
    def getCommandsDriver(name):
        if (name + 'Commands' not in Drivers.drivers):
            Log().error("Driver '" + name + 'Commands' + "' has not been loaded.")
        return LoadedDrivers.drivers[name + 'Commands']
