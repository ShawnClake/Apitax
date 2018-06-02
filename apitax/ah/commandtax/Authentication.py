# Library import
import click

# Application import
from custom import Custom
from httpPlug import HttpPlug
from headerBuilder import HeaderBuilder


# Handles creating an authentication request for tokenable drivers
# It does this by creating a command to an authentication endpoint with the applicable data
class AuthRequest(Custom):
    def __init__(self, username, password, http, debug, config):
        self.http = http

        header = HeaderBuilder()
        header.build(http.getContentTypeJSON())

        if (not http.isCredentialsPosted):
            header.build(http.getPasswordAuthHeader(username, password))

        Custom.__init__(self, header, debug, True)

        if (http.isCredentialsPosted):
            self.setPostData(self.http.getPasswordAuthData(username, password))

        if (self.debug):
            print('AuthRequest Created')

        self.custom = '--post --url ' + http.getAuthEndpoint(config) + ' --data-path \'{"user":"' + username + '"}\''

    def authenticate(self):
        self.handle(self.custom)

    def getToken(self):
        return self.http.getToken(self)  # request.headers.get('X-Subject-Token')
