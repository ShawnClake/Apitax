from apitax.drivers.HttpPlug import HttpPlug


class ApitaxTestsDriver(HttpPlug):
    def isAuthenticated(self):
        return False
        
    def isTokenable(self):
        return False