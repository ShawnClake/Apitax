import base64
import json
from apitax.utilities.Files import getAllFiles
from apitax.utilities.Files import readFile
from apitax.utilities.Files import saveFile
from apitax.utilities.Files import deleteFile
from apitax.utilities.Files import renameFile
from apitax.utilities.Files import getPath
from apitax.ah.State import State
from apitax.config.Config import Config as ConfigConsumer


# Base class for driver plugs
# Defines many customizable properties for interfacing to a new API type
class Driver:

    def __init__(self):
        self.config = State.config
        self.driverConfig = None
        if (self.isConfigurable):
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

    def getPasswordAuthHeader(self, credentials):
        if (not self.isApiAuthenticated()):
            return {}
        temp = credentials.username + ':' + credentials.password
        return {'Authorization': 'Basic ' + base64.b64encode(temp.encode('utf-8'))}

    def getPasswordAuthData(self, credentials):
        if (not self.isApiAuthenticated()):
            return {}
        return {'username': credentials.username, 'password': credentials.password}

    def getTokenAuthHeader(self, credentials):
        if (not self.isApiAuthenticated()):
            return {}
        return {'Authorization': 'Token token="' + credentials.token + '"'}

    def getContentTypeJSON(self):
        # if(not self.isAuthenticated()):
        #   return {}
        return {'Content-type': 'application/json'}

    def getToken(self, response):
        return None

    # Whether or not authentication can produce a usable token or
    # whether to use the username and password for each further request
    def isTokenable(self):
        return True

    # Whether or not crendetials or put into the post data or the header of the
    # authentication request
    def isCredentialsPosted(self):
        return False

    def isApiAuthenticated(self):
        return True

    def piggyBackOffApiAuth(self):
        return False

    def apitaxAuth(self, authObj):
        authObj = authObj['credentials']
        try:
            if(authObj.password == self.users[authObj.username]['password']):
                return self.users[authObj.username]['role']
        except:
            return None
        return None


    def getCatalog(self, auth):
        return {"endpoints": {"tests": {"label": "Placeholder Test", "value": "https://jsonplaceholder.typicode.com"}},
                "selected": "https://jsonplaceholder.typicode.com"}

    def getScriptsCatalog(self):
        files = getAllFiles(self.getScriptsPath("scripts/**/*.ah"))
        returner = {"scripts": []}
        for file in files:
            returner['scripts'].append(
                {"label": file.split('/')[-1].split('.')[0].title(), "relative-path": file, "path": getPath(file)})
        # print(returner)
        return returner

    def getCommandsCatalog(self):
        from apitax.drivers.DriverCommandsFactory import DriverCommandsFactory
        customCommands = DriverCommandsFactory.make(self.config.get('driver') + 'Commands')
        customCommands.setup(self.config, None, None, {}, False, False)
        return customCommands.getCatalog()

    def readScript(self, path):
        return readFile(path)

    def renameScript(self, pathOriginal, pathNew):
        return renameFile(pathOriginal, pathNew)

    # Save does update and create
    def saveScript(self, path, content):
        return saveFile(path, content)

    def deleteScript(self, path):
        return deleteFile(path)

    def serialize(self):
        return {"authenticated": self.isApiAuthenticated(), "auth-tokens": self.isTokenable(),
                "auth-endpoint": self.getAuthEndpoint()}
