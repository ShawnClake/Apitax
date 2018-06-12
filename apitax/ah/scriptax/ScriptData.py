# System Imports
import json
import re

# Application import
from apitax.logs.Log import Log


# Container for all the data returned by a sequence of script requests
class ScriptData:
    def __init__(self):
        self.dataStore = dict(
            {"urls": {}, "vars": {"params": []}, "requests": {}, "exports": {"urls": {}, "vars": {}, "requests": {}, "return": None}}
        )
        self.name = ""
        self.index = 1
        # self.log = Log('logs/log.log')

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
        
    def setReturn(self, value):
        key = "exports.return"
        self.storeDotNotation(value, key)
        
    def getReturn(self):
        key = "exports.return"
        return self.getDotNotation(key)

    # Used for current script interactions
    def storeRequest(self, data, export=False):
        key = "requests." + str(self.index)
        self.storeDotNotation(data, key)
        if (export):
            self.exportRequest(str(self.index))
        self.index += 1
        # if(isinstance(data, dict)):
        #  self.dataStore[str(self.index)] = data
        # else:
        #  self.dataStore[str(self.index)] = json.loads(data)
        # if(prefix == ""):
        #  prefix = self.name
        # if(prefix != ""):
        #  prefix += '.'
        # if(isinstance(data, dict)):
        # self.dataStore[prefix+str(self.index)] = data
        #  self.dataStore[len(self.dataStore)] = data
        # else:
        # self.dataStore[prefix+str(self.index)] = json.loads(data)
        #  self.dataStore[len(self.dataStore)] = json.loads(data)

        # self.log.log(self.dataStore)

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

        finalIndex = components.pop()
        navigation = self.dataStore

        for component in components:
            if (component not in navigation):
                if (isinstance(navigation, list)):
                    navigation[int(component)] = {}
                else:
                    navigation[component] = {}
            if (isinstance(navigation, list)):
                navigation = navigation[int(component)]
            else:
                navigation = navigation[str(component)]
            # navigation = navigation[component]

        if (finalIndex not in navigation):
            navigation[finalIndex] = {}

        if (self.isJson(data)):
            data = json.loads(data)

        navigation[finalIndex] = data

    def getDotNotation(self, key):
        components = key.split('.')
        navigation = self.dataStore
        for component in components:
            # if(isinstance(navigation, list) and int(component) not in navigation):
            #  navigation[int(component)] = {}

            if(navigation is None):
                raise ValueError('Variable does not exist | Variable access is undefined')

            if (component not in navigation and not isinstance(navigation, list)):
                pass
                # navigation[component] = {}
                # if(isinstance(navigation, list)):
                #  navigation[int(component)] = {}
                # else:
                #  navigation[component] = {}
            if (isinstance(navigation, list)):
                navigation = navigation[int(component)]
            else:
                navigation = navigation[str(component)]
            # navigation = navigation[component]
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
            # navigation = navigation[component]
        return True

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

    # DotString is the form   7.someIndex.someOther.andTheLast
    # def getData(self, dotString):
    #  components = dotString.split('.')
    #  response = self.getResponse(components.pop(0))
    #  for identifier in components:
    #    if(isinstance(response, list)):
    #      response = response[int(identifier)]
    #    else:
    #      response = response[str(identifier)]
    #  #self.log.log(response)
    #  return response

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
