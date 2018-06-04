# Library import
import click

# Application import
from apitax.ah.commandtax.commands.Custom import Custom
from apitax.ah.HeaderBuilder import HeaderBuilder


# Handles creating an authentication request for tokenable drivers
# It does this by creating a command to an authentication endpoint with the applicable data
class AuthRequest(Custom):
    def __init__(self, username, password, http, debug, config):
        self.http = http

        if(not self.http.isAuthenticated()):
            return

        header = HeaderBuilder()
        header.build(http.getContentTypeJSON())

        if (not http.isCredentialsPosted):
            header.build(http.getPasswordAuthHeader(username, password))

        Custom.__init__(self, config, header, debug, True)

        if (http.isCredentialsPosted):
            self.setPostData(self.http.getPasswordAuthData(username, password))

        if (self.debug):
            print('AuthRequest Created')

        self.custom = '--post --url ' + http.getAuthEndpoint(config) + ' --data-path \'{"user":"' + username + '"}\''

    def authenticate(self):
        if(not self.http.isAuthenticated()):
            return
        self.handle(self.custom)

    def getToken(self):
        if(not self.http.isAuthenticated()):
            return None
        return self.http.getToken(self)  # request.headers.get('X-Subject-Token')
