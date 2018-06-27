from apitax.ah.commandtax.Commandtax import Commandtax
from apitax.ah.commandtax.Authentication import *
from apitax.drivers.HttpPlugFactory import HttpPlugFactory
from apitax.ah.HeaderBuilder import HeaderBuilder
from apitax.config.Config import Config
from apitax.logs.Log import Log

from time import time

# The 'heart' of the application
# Connector facilitates the initialization of the connection to an API
# Connector handles setting up the driver, authetnication, headers, and then
# using all of that to execute a command
#
# Additional interfaces to this utility should directly communicate with connector
# and likely nothing else. Connector handles the rest.
class Connector:

    def __init__(self, debug=False, sensitive=False, command='', username='', password='', token='', json=True, parameters=[]):
        self.executionTime = None
        self.debug = debug
        self.sensitive = sensitive
        self.command = command
        self.username = username
        self.password = password
        self.token = token
        self.commandHandler = None
        self.parameters = parameters
        self.logBuffer = []

        self.command = self.command.replace('\\"', '"');
        self.command = self.command.replace('\\\'', '\'');


        self.config = Config()
        self.http = HttpPlugFactory.make(self.config.get('driver') + 'Driver')

        self.auth = AuthRequest(self.username, self.password, self.http, self.debug, self.config)

        self.header = HeaderBuilder()
        if (json):
            self.header.build(self.http.getContentTypeJSON())

        if (token == ''):
            # self.auth = AuthRequest(self.username, self.password, self.http, self.debug, self.config)
            preHeader = self.header.header.copy()
            if (self.http.isTokenable()):
                self.auth.authenticate()
                self.token = self.auth.getToken()
                self.header.header = preHeader
                self.header.build(self.http.getTokenAuthHeader(self.token))
            else:
                self.header.build(self.http.getPasswordAuthHeader(self.username, self.password))
        else:
            self.header.build(self.http.getTokenAuthHeader(self.token))

        # print(self.token)

    def execute(self, command=''):
        if (command != ''):
            self.command = command
        t0 = time()
        self.commandHandler = Commandtax(self.header, self.command, self.config, debug=self.debug,
                                      sensitive=self.sensitive, parameters=self.parameters)
        self.executionTime = time() - t0
        
        log = Log()
        self.logBuffer = log.getLoggerDriver().buffer
        log.getLoggerDriver().outputLog()
        
        return self.commandHandler
        