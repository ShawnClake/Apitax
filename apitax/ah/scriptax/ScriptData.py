# System Imports
import json
import re

from apitax.utilities.Numbers import isNumber

# Container for all the data returned by a sequence of script requests
class ScriptData:
    def __init__(self):
        self.dataStore = dict(
            {
              "flow": {
                'return': False, 
                'exit': False, 
                'error': False
              }, 
              "urls": {"current": ""}, 
              "auth": None, 
              "vars": {"params": {}}, 
              "requests": {}, 
              "exports": {
                "urls": {}, 
                "vars": {}, 
                "requests": {}, 
                "return": None
              }
            }
        )
        self.name = ""
        self.index = 1

    def getStore(self):
        returner = {}
        returner['vars'] = self.dataStore['vars']
        returner['requests'] = self.dataStore['requests']
        return returner
        
    def getStatus(self):
        returner = {}
        returner['vars'] = self.dataStore['vars']
        returner['requests'] = self.dataStore['requests']
        returner['flow'] = self.dataStore['flow']
        returner['exports'] = self.dataStore['exports']
        returner['urls'] = self.dataStore['urls']
        return returner

    # Used for current script interactions
    def storeUrl(self, name, url):
        key = "urls." + name
        self.storeDotNotation(url, key)
        if (self.isExistDotNotation("exports." + key)):
            self.exportUrl(name)

    def getUrl(self, name):
        key = "urls." + name
        return self.getDotNotation(key)

    # Used for current script interactions
    def storeVar(self, name, var):
        key = "vars." + name
        self.storeDotNotation(var, key)
        if (self.isExistDotNotation("exports." + key)):
            self.exportVar(name)

    def getVar(self, name):
        key = "vars." + name
        return self.getDotNotation(key)
        
    def deleteVar(self, name):
        key = "vars." + name
        return self.deleteDotNotation(key)
        
    def isVarExist(self, name):
        return self.isExistDotNotation("vars." + name)
        
    def setReturn(self, value):
        key = "exports.return"
        self.storeDotNotation(value, key)
        
    def getReturn(self):
        key = "exports.return"
        return self.getDotNotation(key)
        
    def setAuth(self, value):
        key = "auth"
        self.storeDotNotation(value, key)
        
    def getAuth(self):
        key = "auth"
        return self.getDotNotation(key)
        
    def setFlow(self, name, value):
        key = "flow." + name 
        self.storeDotNotation(value, key)
        
    def getFlow(self, name):
        key = "flow." + name
        return self.getDotNotation(key)

    def error(self, message, logprefix=''):
        if(isinstance(message, dict)):
            self.setFlow('error', message)
        else:
            self.setFlow('error', {'message': message, 'logprefix': logprefix})
    
    def getError(self):
        return self.getFlow('error')

    # Used for current script interactions
    def storeRequest(self, data, export=False):
        key = "requests." + str(self.index)
        self.storeDotNotation(data, key)
        if (export):
            self.exportRequest(str(self.index))
        self.index += 1

    def getRequest(self, index):
        key = "requests." + str(index)
        return self.getDotNotation(key)

    def getRequestData(self):
        newData = self.dataStore.copy()
        # newData.pop("0")
        return newData

    def importVar(self, data, dottedKey):
        key = "vars." + dottedKey
        self.storeDotNotation(data, key)

    def importRequest(self, data, dottedKey):
        key = "requests." + dottedKey
        self.storeDotNotation(data, key)

    def importUrl(self, data, dottedKey):
        key = "urls." + dottedKey
        self.storeDotNotation(data, key)

    def exportVar(self, dottedVarName):
        key = "exports.vars." + dottedVarName
        self.storeDotNotation(self.getVar(dottedVarName), key)
        # self.dataStore["exports"]["vars"][varName] = self.getVar(varName)

    def getVarExports(self):
        return self.getDotNotation("exports.vars")

    def exportRequest(self, dottedRequestName):
        key = "exports.requests." + dottedRequestName
        self.storeDotNotation(self.getRequest(dottedRequestName), key)

    def getRequestExports(self):
        return self.getDotNotation("exports.requests")

    def exportUrl(self, dottedUrlName):
        key = "exports.urls." + dottedUrlName
        self.storeDotNotation(self.getVar(dottedUrlName), key)

    def getUrlExports(self):
        return self.getDotNotation("exports.urls")

    def getExports(self):
        return self.getDotNotation("exports")

    def storeDotNotation(self, data, key):
        components = key.split('.')
        #finalIndex = components[-1]
        finalIndex = components.pop()
        navigation = self.dataStore

        for component in components:
            if (component not in navigation):
                if (isinstance(navigation, list)):
                    if(not(isNumber(component) and len(navigation) > int(component))):
                        navigation[int(component)] = {}
                else:
                    navigation[component] = {}
            if (isinstance(navigation, list)):
                navigation = navigation[int(component)]
            else:
                navigation = navigation[str(component)]


        #if (finalIndex not in navigation):
        #    navigation[finalIndex] = {}

        if (self.isJson(data)):
            data = json.loads(data)
            
        if(isinstance(navigation, list)):
            finalIndex = int(finalIndex)
            if(len(navigation) <= finalIndex):
                navigation.insert(finalIndex, data)
            else:
                navigation[finalIndex] = data
        else:
            navigation[finalIndex] = data

    def getDotNotation(self, key):
        components = key.split('.')
        navigation = self.dataStore
        for component in components:
            if(navigation is None):
                self.error('Cannot access variable past a None type parent => \'' + key+'\'')

            if (component not in navigation and not isinstance(navigation, list)):
                self.error('Variable does not exist | Variable access is undefined => \'' + key+'\'')

            if (isinstance(navigation, list)):
                navigation = navigation[int(component)]
            else:
                navigation = navigation[str(component)]

        return navigation

    def isExistDotNotation(self, key):
        components = key.split('.')
        navigation = self.dataStore
        for component in components:
            if (component not in navigation and not isinstance(navigation, list)):
                return False
            if (isinstance(navigation, list)):
                navigation = navigation[int(component)]
            else:
                navigation = navigation[str(component)]

        return True
        
    def deleteDotNotation(self, key):
        components = key.split('.')
        navigation = self.dataStore
        for component in components[:-1]:
            if(navigation is None):
                self.error('Cannot access variable past a None type parent => \'' + key+'\'')

            if (component not in navigation and not isinstance(navigation, list)):
                self.error('Variable does not exist | Variable access is undefined => \'' + key+'\'')
                #pass

            if (isinstance(navigation, list)):
                navigation = navigation[int(component)]
            else:
                navigation = navigation[str(component)]

        if (components[-1] not in navigation):
            self.error('Variable does not exist | Variable access is undefined => \'' + key+'\'')

        return navigation.pop(components[-1])

        #return navigation

    def importScriptsExports(self, scriptData, prefix="", export=False):
        if (prefix == ""):
            prefix = scriptData.name
        if (prefix != ""):
            prefix += '.'

        # print(scriptData.dataStore)

        for varName, varVal in scriptData.getVarExports().items():
            self.importVar(varVal, prefix + varName)
            if (export):
                self.exportVar(prefix + varName)

        for urlName, urlVal in scriptData.getUrlExports().items():
            self.importUrl(urlVal, prefix + urlName)
            if (export):
                self.exportUrl(prefix + urlName)

        for requestIndex, request in scriptData.getRequestExports().items():
            self.importRequest(request, prefix + requestIndex)
            if (export):
                self.exportRequest(prefix + requestIndex)

    def isJson(self, x):
        try:
            json.loads(x)
            return True
        except:
            return False

    def isJsonable(self, x):
        try:
            json.dumps(x)
            return True
        except:
            return False
