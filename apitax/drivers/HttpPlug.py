import base64
import json
from apitax.utilities.Files import getAllFiles
from pathlib import Path

# Base class for driver plugs
# Defines many customizable properties for interfacing to a new API type
class HttpPlug:

    def getAuthEndpoint(self, config):
        return config.get('auth-endpoint')

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
        
    def getCatalog(self):
        return {"endpoints": {"tests": {"label": "Placeholder Test", "value": "https://jsonplaceholder.typicode.com"}}, "selected": "https://jsonplaceholder.typicode.com"}
        	
    def getScriptsCatalog(self, config):
        files = getAllFiles("scripts/**/*.ah")
        returner = {"scripts": []}
        for file in files:
            returner['scripts'].append({"label": file.split('/')[-1].split('.')[0].title(),"relative-path":file,"path": str(Path(file).resolve())})
        # print(returner)
        return returner
        
    def serialize(self, config):
        return {"authenticated": self.isAuthenticated(), "auth-tokens": self.isTokenable(), "auth-endpoint": self.getAuthEndpoint(config)}
