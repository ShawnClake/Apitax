# Library import
import click

# Application import
from apitax.ah.commandtax.commands.Custom import Custom
from apitax.ah.HeaderBuilder import HeaderBuilder
from apitax.ah.Options import Options
from apitax.ah.State import State


# Handles creating an authentication request for tokenable drivers
# It does this by creating a command to an authentication endpoint with the applicable data
class AuthRequest(Custom):
    def __init__(self, credentials, driver, options):
        self.driver = driver
        self.log = State.log
        config = State.config

        if (not self.driver.isApiAuthenticated()):
            return

        header = HeaderBuilder()
        header.build(self.driver.getContentTypeJSON())

        if (not self.driver.isCredentialsPosted):
            header.build(self.driver.getPasswordAuthHeader(credentials))

        Custom.__init__(self, config, header, None, None, Options(debug=options.debug, sensitive=True))

        if (self.driver.isCredentialsPosted):
            self.setPostData(self.driver.getPasswordAuthData(credentials))

        if (self.options.debug):
            self.log.log('>> AuthRequest Created')

        self.custom = '--post --url ' + self.driver.getAuthEndpoint() + ' --data-path \'{"user":"' + credentials.username + '"}\''

    def isAuthenticated(self):
        if (not self.driver.isApiAuthenticated()):
            return True
        if(self.driver.isTokenable() and self.getToken()):
            return True
        if(self.getResponseStatusCode() >= 200 and self.getResponseStatusCode() < 300):
            return True
        return False

    def authenticate(self):
        if (not self.driver.isApiAuthenticated()):
            return
        self.handle(self.custom)

    def getToken(self):
        if (not self.driver.isApiAuthenticated()):
            return None
        return self.driver.getToken(self)  # request.headers.get('X-Subject-Token')
