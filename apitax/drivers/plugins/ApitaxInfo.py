from apitax.drivers.Driver import Driver
from apitax.utilities.Files import getAllFiles
from apitax.ah.Options import Options
from pathlib import Path
from apitax.ah.Credentials import Credentials

class ApitaxInfoDriver(Driver):
    def isAuthenticated(self):
        return False
        
    def isTokenable(self):
        return False



