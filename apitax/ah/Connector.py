from apitax.ah.commandtax.Commandtax import Commandtax
from apitax.ah.commandtax.Authentication import *
from apitax.ah.LoadedDrivers import LoadedDrivers
from apitax.ah.HeaderBuilder import HeaderBuilder
from apitax.config.Config import Config
from apitax.logs.Log import Log
from apitax.ah.Credentials import Credentials
from apitax.ah.Options import Options

from time import time

# The 'heart' of the application
# Connector facilitates the initialization of the connection to an API
# Connector handles setting up the driver, authetnication, headers, and then
# using all of that to execute a command
#
# Additional interfaces to this utility should directly communicate with connector
# and likely nothing else. Connector handles the rest.
class Connector:

    def __init__(self, options=Options(), command='', username='', password='', token='', credentials=None, json=True, parameters={}):
        
        self.options=options
        self.parameters = parameters
        
        if(credentials):
            self.credentials = credentials
        else:
            self.credentials = Credentials(username=username,password=password,token=token)

        self.command = command
        self.command = self.command.replace('\\"', '"');
        self.command = self.command.replace('\\\'', '\'');
        
        self.executionTime = None 
        self.commandHandler = None
        self.logBuffer = []

        self.config = Config.read()
        
        if(self.options.driver):
            self.http = LoadedDrivers.getBaseDriver(self.options.driver)
        else:
            self.http = LoadedDrivers.getDefaultBaseDriver()

        self.header = HeaderBuilder()
        if (json):
            self.header.build(self.http.getContentTypeJSON())

        if (self.credentials.token == ''):
            preHeader = self.header.header.copy()
            if (self.http.isTokenable()):
                auth = AuthRequest(self.credentials.username, self.credentials.password, self.http, self.options, self.config)
                auth.authenticate()
                self.credentials.token = auth.getToken()
                self.header.header = preHeader
                self.header.build(self.http.getTokenAuthHeader(self.credentials.token))
            else:
                self.header.build(self.http.getPasswordAuthHeader(self.credentials.username, self.credentials.password))
        else:
            #print(self.http.getTokenAuthHeader(self.token))
            self.header.build(self.http.getTokenAuthHeader(self.credentials.token))

        # print(self.token)

    def getCredentials(self):
        return self.credentials

    def execute(self, command=''):
        if (command != ''):
            self.command = command
        t0 = time()
        self.commandHandler = Commandtax(self.header, self.command, self.config, options=self.options, parameters=self.parameters, auth=self.getCredentials())
        
        self.executionTime = time() - t0
        
        log = Log()
        self.logBuffer = log.getLoggerDriver().buffer
        log.getLoggerDriver().outputLog()
        
        return self.commandHandler
        