import base64
import json
from apitax.utilities.Files import getAllFiles
from apitax.utilities.Files import getPath
from apitax.config.Config import Config as ConfigConsumer
from pathlib import Path

# Base class for driver plugs
# Defines many customizable properties for interfacing to a new API type
class Driver:

    def __init__(self):
        self.config = ConfigConsumer.read()
        self.driverConfig = None
        if(self.isConfigurable):
            #print(self.__class__.__name__)
            self.driverConfig = ConfigConsumer.read(sectionName=self.__class__.__name__)
        
    def isConfigurable(self):
        return False

    def getDefaultUsername(self):
        return self.driverConfig.get('default-username')
        
    def getDefaultPassword(self):
        return self.driverConfig.get('default-password')

    def getAuthEndpoint(self):
        try:
            return self.driverConfig.get('base-endpoint') + self.driverConfig.get('auth-endpoint')
        except:
            return '`base-endpoint` and/or `auth-endpoint` not specified in driver configuration.'
        
    def getCatalogEndpoint(self):
        try:
            return self.driverConfig.get('base-endpoint') + self.driverConfig.get('catalog-endpoint')
        except:
            return '`base-endpoint` and/or `catalog-endpoint` not specified in driver configuration.'

    def getScriptsPath(self, append=''):
        return getPath(self.config.path + '/drivers/plugins/scriptax/' + self.__class__.__name__ + '/' + append)

    def getPasswordAuthHeader(self, username, password):
        if(not self.isAuthenticated()):
            return {}
        temp = username + ':' + password
        return {'Authorization': 'Basic ' + base64.b64encode(temp.encode('utf-8'))}

    def getPasswordAuthData(self, username, password):
        if(not self.isAuthenticated()):
            return {}
        return {'username': username, 'password': password}

    def getTokenAuthHeader(self, token):
        if(not self.isAuthenticated()):
            return {}
        return {'Authorization': 'Token token="' + token + '"'}

    def getContentTypeJSON(self):
        #if(not self.isAuthenticated()):
         #   return {}
        return {'Content-type': 'application/json'}

    def getToken(self, response):
        return json.loads(response.getResponseBody())['token']

    # Whether or not authentication can produce a usable token or
    # whether to use the username and password for each further request
    def isTokenable(self):
        return True

    # Whether or not crendetials or put into the post data or the header of the
    # authentication request
    def isCredentialsPosted(self):
        return False
        
    def isAuthenticated(self):
        return True
        
    def getCatalog(self, auth):
        return {"endpoints": {"tests": {"label": "Placeholder Test", "value": "https://jsonplaceholder.typicode.com"}}, "selected": "https://jsonplaceholder.typicode.com"}
        	
    def getScriptsCatalog(self):
        files = getAllFiles(self.getScriptsPath("scripts/**/*.ah"))
        returner = {"scripts": []}
        for file in files:
            returner['scripts'].append({"label": file.split('/')[-1].split('.')[0].title(),"relative-path":file,"path": getPath(file)})
        # print(returner)
        return returner
        
    def getCommandsCatalog(self):
        from apitax.drivers.DriverCommandsFactory import DriverCommandsFactory
        customCommands = DriverCommandsFactory.make(config.get('driver') + 'Commands')
        customCommands.setup(config, None, None, {}, debug, sensitive)
        return customCommands.getCatalog()
        
    def serialize(self):
        return {"authenticated": self.isAuthenticated(), "auth-tokens": self.isTokenable(), "auth-endpoint": self.getAuthEndpoint()}
