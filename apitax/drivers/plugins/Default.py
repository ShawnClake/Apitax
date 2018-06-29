from apitax.drivers.Driver import Driver
from apitax.utilities.Files import getAllFiles
from pathlib import Path

class DefaultDriver(Driver):
    def isAuthenticated(self):
        return False
        
    def isTokenable(self):
        return False
