from apitax.ah.State import State
from apitax.ah.commandtax.ApiAuthentication import AuthRequest
from apitax.ah.LoadedDrivers import LoadedDrivers


class ApitaxAuthentication:

    @staticmethod
    def login(credentials):
        driver = LoadedDrivers.getAuthDriver()
        role = None
        if(driver.piggyBackOffApiAuth()):
            apiDriver = LoadedDrivers.getPrimaryDriver()

            if('driver' in credentials.extra):
                apiDriver = LoadedDrivers.getBaseDriver(credentials.extra['driver'])

            apiAuth = AuthRequest(credentials, apiDriver, State.options)
            apiAuth.authenticate()

            if(not apiAuth.isAuthenticated()):
                return None

            role = driver.apitaxAuth({"credentials": credentials, "apiAuthDriver": apiAuth})
            if(apiDriver.isTokenable()):
                credentials.token = apiAuth.getToken()
        else:
            role = driver.apitaxAuth({"credentials": credentials})

        return {"role": role, "credentials": credentials}








