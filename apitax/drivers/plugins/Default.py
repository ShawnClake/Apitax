from apitax.drivers.HttpPlug import HttpPlug
from apitax.utilities.Files import getAllFiles
from pathlib import Path

class DefaultDriver(HttpPlug):
    def isAuthenticated(self):
        return False
        
    def isTokenable(self):
        return False
