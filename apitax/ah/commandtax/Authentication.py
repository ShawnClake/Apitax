# Library import
import click

# Application import
from apitax.ah.commandtax.commands.Custom import Custom
from apitax.ah.HeaderBuilder import HeaderBuilder
from apitax.logs.Log import Log
from apitax.ah.Options import Options


# Handles creating an authentication request for tokenable drivers
# It does this by creating a command to an authentication endpoint with the applicable data
class AuthRequest(Custom):
    def __init__(self, username, password, http, options, config):
        self.http = http
        self.log = Log()

        if(not self.http.isAuthenticated()):
            return

        header = HeaderBuilder()
        header.build(http.getContentTypeJSON())

        if (not http.isCredentialsPosted):
            header.build(http.getPasswordAuthHeader(username, password))

        Custom.__init__(self, config, header, None, None, Options(debug=options.debug, sensitive=True))

        if (http.isCredentialsPosted):
            self.setPostData(self.http.getPasswordAuthData(username, password))

        if (self.options.debug):
            self.log.log('>> AuthRequest Created')

        self.custom = '--post --url ' + http.getAuthEndpoint() + ' --data-path \'{"user":"' + username + '"}\''

    def authenticate(self):
        if(not self.http.isAuthenticated()):
            return
        self.handle(self.custom)

    def getToken(self):
        if(not self.http.isAuthenticated()):
            return None
        return self.http.getToken(self)  # request.headers.get('X-Subject-Token')
