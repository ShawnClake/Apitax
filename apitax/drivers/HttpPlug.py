import base64
import json


# Base class for driver plugs
# Defines many customizable properties for interfacing to a new API type
class HttpPlug:

    def getAuthEndpoint(self, config):
        return config.get('auth-endpoint')

    def getPasswordAuthHeader(self, username, password):
        temp = username + ':' + password
        return {'Authorization': 'Basic ' + base64.b64encode(temp.encode('utf-8'))}

    def getPasswordAuthData(self, username, password):
        return {'username': username, 'password': password}

    def getTokenAuthHeader(self, token):
        return {'Authorization': 'Token token="' + token + '"'}

    def getContentTypeJSON(self):
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