from apitax.ah.commandtax.Command import Command
from apitax.ah.commandtax.Authentication import *
from apitax.drivers.HttpPlugFactory import HttpPlugFactory
from apitax.ah.HeaderBuilder import HeaderBuilder
from apitax.config.Config import Config


# The 'heart' of the application
# Connector facilitates the initialization of the connection to an API
# Connector handles setting up the driver, authetnication, headers, and then
# using all of that to execute a command
#
# Additional interfaces to this utility should directly communicate with connector
# and likely nothing else. Connector handles the rest.
class Connector:

    def __init__(self, debug=False, sensitive=False, command='', username='', password='', token='', json=True):
        self.debug = debug
        self.sensitive = sensitive
        self.command = command
        self.username = username
        self.password = password
        self.token = token
        self.commandHandler = None

        self.config = Config()
        self.http = HttpPlugFactory.make(self.config.get('driver') + 'Driver')

        self.auth = AuthRequest(self.username, self.password, self.http, self.debug, self.config)

        self.header = HeaderBuilder()
        if (json):
            self.header.build(self.http.getContentTypeJSON())

        if (token == ''):
            # self.auth = AuthRequest(self.username, self.password, self.http, self.debug, self.config)
            preHeader = self.header.header.copy()
            self.header.build(self.http.getPasswordAuthHeader(self.username, self.password))
            if (self.http.isTokenable()):
                self.auth.authenticate()
                self.token = self.auth.getToken()
                self.header.header = preHeader
                self.header.build(self.http.getTokenAuthHeader(self.token))
        else:
            self.header.build(self.http.getTokenAuthHeader(self.token))

        # print(self.token)

    def execute(self, command=''):
        if (command != ''):
            self.command = command
        self.commandHandler = Command(self.header, self.command, self.config, debug=self.debug,
                                      sensitive=self.sensitive)
        return self.commandHandler
