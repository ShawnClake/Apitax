from apitax.drivers.Driver import Driver
from apitax.utilities.Json import read
from apitax.ah.State import State
from apitax.utilities.Files import getPath


class BasicAuthDriver(Driver):

    def __init__(self):
        super().__init__()
        self.users = read(getPath(State.paths['root'] + "/users.json"))

    def isApiAuthenticated(self):
        return False

    def isTokenable(self):
        return False
