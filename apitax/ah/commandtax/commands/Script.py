# System import
import json
import re
import os

# Application import
from apitax.logs.Log import Log
from apitax.ah.commandtax.Request import Request
from apitax.ah.scriptax.ScriptData import ScriptData


# TODO:
#  Change the way request is saved to include status code & command run
#  Add additional syntaxes for import & exporting


# Script is used to automate the execution of many commands
class Script(Request):
    def __init__(self, header, debug, sensitive):
        self.header = header
        self.debug = debug
        self.sensitive = sensitive
        self.config = None
        self.data = ScriptData()
        self.log = Log('logs/log.log')

        self.regexSetVar = '^set[ ]{1,}[A-z0-9_.\-]{2,}[ ]{0,}=[ ]{0,}[A-z0-9:/&$#@%?<>.,\-{}_ ]{1,}[ ]{0,}$'  # {{ someVarName = someVarValue }}
        self.regexSetUrl = '^{{[ ]{0,}url:[ ]{0,}[A-z0-9:/&$#@%?<>.,\-{}[\] _"\']{1,}[ ]{0,}}}'  # {{url: {"url":"https://stackoverflow.com/questions/4426663/{id.test}/how-to-remove-the-first-item-from-a-list", "name":"auth"}}}

        self.regexExportVar = '^export[ ]{1,}[A-z0-9_.\-]{1,}[ ]{0,}$'  # export someVar
        self.regexExportNewVar = '^export[ ]{1,}[A-z0-9_.\-]{2,}[ ]{0,}=[ ]{0,}[A-z0-9:/&$#@%?<>.,\-{}_]{1,}[ ]{0,}$'  # export user_id = {{user_id}}
        self.regexExportRequest = '^export[ ]{1,}[A-z0-9:/&$#@%?<>.,-{}_ \'"]{2,}[ ]{0,}$'

        self.regexImport = '^import[ ]{1,}[A-z0-9:/&$#@%?<>.,-{}_ \'"]{2,}[ ]{0,}$'

        self.regexName = '^name[ ]{1,}[A-z0-9_]{1,}[ ]{0,}$'  # name OpenStackURLs5

        self.regexExecuteCommandtax = '^{%[ ]{0,}[A-z0-9:/&$#@%?<>.,\-{}[\] _"\']{1,}[ ]{0,}%}$'  # {% some command tax %}
        self.regexCommandtax = '^>[ ]{1,}[A-z0-9:/&$#@%?<>.,\-{}[\] _"\']{1,}[ ]{0,}$'  # {% some command tax %}

        self.regexVar = '{{[ ]{0,}[A-z0-9_.\-]{1,}[ ]{0,}}}'
        self.regexUrl = '{{[ ]{0,}u[ ]{0,}:[ ]{0,}[A-z0-9_.]{1,}[ ]{0,}}}'
        self.regexRequest = '{{[ ]{0,}r[ ]{0,}:[ ]{0,}[A-z0-9_.\-]{1,}(?:[.][A-z0-9_.\-]{1,}){1,}[ ]{0,}}}'

        Request.__init__(self, '', header.get(), '', debug=debug, sensitive=sensitive, customResponse=True)

    def setConfig(self, config):
        self.config = config

    def detectScriptax(self, command, lineNumber=0):
        detected = False
        regexVar = '^{{[ ]{0,}[A-z0-9_.\-]{2,}[ ]{0,}=[ ]{0,}[A-z0-9:/&$#@%?<>.,\-{}_]{1,}[ ]{0,}}}'  # {{ someVarName = someVarValue }}
        regexUrl = '^{{[ ]{0,}url:[ ]{0,}[A-z0-9:/&$#@%?<>.,\-{}[\] _"\']{1,}[ ]{0,}}}'  # {{url: {"url":"https://stackoverflow.com/questions/4426663/{id.test}/how-to-remove-the-first-item-from-a-list", "name":"auth"}}}

        regexExportVar = '^export[ ]{1,}[A-z0-9_.\-]{1,}[ ]{0,}$'  # export someVar
        regexExportNewVar = '^export[ ]{1,}[A-z0-9_.\-]{2,}[ ]{0,}=[ ]{0,}[A-z0-9:/&$#@%?<>.,\-{}_]{1,}[ ]{0,}$'  # export user_id = {{user_id}}

        regexImport = '^import[ ]{1,}[A-z0-9:/&$#@%?<>.,-{}_ \'"]{2,}[ ]{0,}$'

        regexName = '^name[ ]{1,}[A-z0-9_]{1,}[ ]{0,}$'  # name OpenStackURLs5

        # Variable
        matches = re.findall(regexVar, command)
        for match in matches:
            detected = True
            matchStr = match[2:-2]
            var = matchStr.split('=')
            vName = var[0].strip()
            vVal = var[1].strip()
            self.data.storeVar(vName, vVal)
            if (self.debug):
                self.log.log('> Assigning Variable: ' + vName + ' = ' + vVal)
                self.log.log('')

        # URL
        matches = re.findall(regexUrl, command)
        for match in matches:
            detected = True
            matchStr = match[2:-2]
            urlData = json.loads(matchStr[matchStr.find(':') + 1:].strip())
            uName = urlData['name'].strip()
            uVal = urlData['url'].strip()
            self.data.storeUrl(uName, uVal)
            if (self.debug):
                self.log.log('> Assigning URL: ' + uName + ' = ' + uVal)
                self.log.log('')

        # Export Existing Variable
        matches = re.findall(regexExportVar, command)
        for match in matches:
            detected = True
            matchStr = (match[6:])
            varName = matchStr.strip()
            self.data.export(varName)
            if (self.debug):
                self.log.log('> Exporting Variable: ' + varName + ' = ' + self.data.getVar(varName))
                self.log.log('')

        # Export New Variable
        matches = re.findall(regexExportNewVar, command)
        for match in matches:
            detected = True
            matchStr = (match[6:]).strip()
            var = matchStr.split('=')
            vName = var[0].strip()
            vVal = var[1].strip()
            self.data.storeVar(vName, vVal)
            self.data.export(vName)
            if (self.debug):
                self.log.log('> Exporting New Variable: ' + vName + ' = ' + vVal)
                self.log.log('')

        # Import
        matches = re.findall(regexImport, command)
        for match in matches:
            from apitax.ah.commandtax.Command import Command
            detected = True
            matchStr = (match[6:])
            importCommand = matchStr.strip()
            commandHandler = Command(self.header, importCommand, self.config, debug=self.debug,
                                     sensitive=self.sensitive)
            if (commandHandler.getRequest().getResponseBody().strip() != ''):
                if (isinstance(commandHandler.getRequest(), Script)):
                    if (commandHandler.getRequest().data.name == ""):
                        fileName = os.path.basename(importCommand[6:].strip())
                        if ("." in fileName):
                            fileName = fileName.split('.')[0]
                        commandHandler.getRequest().data.name = fileName
                    scriptName = commandHandler.getRequest().data.name

                    # self.data.store(commandHandler.getRequest().data.getRequestData(), prefix=scriptName)
                    self.data.importExports(commandHandler.getRequest().data.getExports(), prefix=scriptName)
                    # print(json.dumps(self.data.dataStore))
                else:
                    self.data.store(commandHandler.getRequest().getResponseBody())
                    # self.data.store(commandHandler.getRequest().getResponseBody())
                self.request['text'][lineNumber] = {"command": importCommand.strip(),
                                                    "status": commandHandler.getRequest().getResponseStatusCode(),
                                                    "body": json.loads(commandHandler.getRequest().getResponseBody())}
            else:
                self.request['text'][lineNumber] = {"command": importCommand.strip(),
                                                    "status": commandHandler.getRequest().getResponseStatusCode(),
                                                    "body": ""}
            if (self.debug):
                self.log.log('> Importing: ' + importCommand)
                self.log.log('')

        # Name
        matches = re.findall(regexName, command)
        for match in matches:
            detected = True
            matchStr = (match[4:])
            name = matchStr.strip()
            self.data.name = name
            if (self.debug):
                self.log.log('> Setting Script Name: ' + name)
                self.log.log('')

        if (detected and self.debug):
            self.log.log('')
            self.log.log('')

        return detected

    def inject(self, command):

        # regexVar = '{{[ ]{0,}v[ ]{0,}:[ ]{0,}[A-z0-9]{1,}[ ]{0,}}}'
        regexVar = '{{[ ]{0,}[A-z0-9_.\-]{1,}[ ]{0,}}}'
        regexUrl = '{{[ ]{0,}u[ ]{0,}:[ ]{0,}[A-z0-9_.]{1,}[ ]{0,}}}'
        regexRequest = '{{[ ]{0,}r[ ]{0,}:[ ]{0,}[0-9]{1,}(?:[.][A-z0-9]{1,}){1,}[ ]{0,}}}'

        # Variable
        matches = re.findall(regexVar, command)
        for match in matches:
            matchStr = match[2:-2]
            # varName = matchStr[matchStr.find(':') + 1:].strip()
            varName = matchStr.strip()
            command = command.replace(match, self.data.getVar(varName))
            self.log.log('> Injecting Variable \'' + varName + '\': ' + command)
            self.log.log('')

        # URL
        matches = re.findall(regexUrl, command)
        for match in matches:
            matchStr = match[2:-2]
            urlName = matchStr[matchStr.find(':') + 1:].strip()
            command = command.replace(match, self.data.getUrl(urlName))
            self.log.log('> Injecting URL \'' + urlName + '\': ' + command)
            self.log.log('')

        # Request
        matches = re.findall(regexRequest, command)
        for match in matches:
            matchStr = match[2:-2]
            reqName = matchStr[matchStr.find(':') + 1:].strip()
            # print(reqName)
            # print(json.dumps(self.data.dataStore))
            command = command.replace(match, self.data.getData(reqName))
            self.log.log('> Injecting Request \'' + reqName + '\': ' + command)
            self.log.log('')
        return command

    # Begins executing the script from top to bottom & handles nested scripts
    def handle(self, filepath):
        from apitax.ah.commandtax.Command import Command
        if (self.debug):
            self.log.log('>>> Opening Script: ' + filepath[0])
            self.log.log('')
            self.log.log('')
        commandHandler = None
        with open(filepath[0]) as fileObj:
            i = 0
            self.request = {}
            self.request['text'] = {}
            for line in fileObj:
                if (line.strip() == ''):
                    continue
                line = ''.join(line.splitlines())

                self.log.log('> Now processing: ' + line)
                self.log.log('')

                self.evaluateScriptax(line)
                self.log.log('')

                # line = self.inject(line)

                # if(not self.detectScriptax(line, lineNumber = i)):
                #  commandHandler = Command(self.header, line, self.config, debug = self.debug, sensitive = self.sensitive)

                #  if(commandHandler.getRequest().getResponseBody().strip() != ''):
                # if(isinstance(commandHandler.getRequest(), Script)):
                # if(commandHandler.getRequest().data.name == ""):
                #  fileName = os.path.basename(line[6:].strip())
                #  if("." in fileName):
                #    fileName = fileName.split('.')[0]
                #  commandHandler.getRequest().data.name = fileName
                # scriptName = commandHandler.getRequest().data.name
                # self.data.store(commandHandler.getRequest().data.getRequestData()) # Imports the request data from embedded scripts - this should eventually be removed in favor of exports
                # print('THE EXPORTS:')
                # print(commandHandler.getRequest().data.getExports())
                # print(self.data.dataStore)
                # self.data.importExports(commandHandler.getRequest().data.getExports(), prefix=scriptName)
                # else:
                #  self.data.store(commandHandler.getRequest().getResponseBody())
                #    self.data.store(commandHandler.getRequest().getResponseBody())
                #    self.request['text'][i] = {"command": line.strip(), "status": commandHandler.getRequest().getResponseStatusCode(),"body":json.loads(commandHandler.getRequest().getResponseBody())}
                #  else:
                #    self.request['text'][i] = {"command": line.strip(), "status": commandHandler.getRequest().getResponseStatusCode(),"body":""}

                i += 1
            self.request['text'] = json.dumps(self.request['text'])
            self.request['status_code'] = 200

    def evaluateScriptax(self, line, injectorsOnly=False):
        line = ''.join(line.splitlines())
        while (True):
            result = self.scriptax(line.strip(), injectorsOnly=injectorsOnly)
            if (result is None):
                return line
            else:
                line = result

    def scriptax(self, line, injectorsOnly=False):

        if (line == ""):
            return None

        # INJECTORS

        # Variable
        matches = re.findall(self.regexVar, line)
        for match in matches:
            return self.stVariable(line, match)

        # URL
        matches = re.findall(self.regexUrl, line)
        for match in matches:
            return self.stUrl(line, match)

        # Request
        matches = re.findall(self.regexRequest, line)
        for match in matches:
            return self.stRequest(line, match)

        # Execute Commandtax
        matches = re.findall(self.regexExecuteCommandtax, line)
        for match in matches:
            return self.stExecuteCommandtax(line, match)

        # CONSUMERS

        if (not injectorsOnly):

            # Set Variable
            matches = re.findall(self.regexSetVar, line)
            for match in matches:
                return self.stSetVariable(line, match)

                # Set URL
            matches = re.findall(self.regexSetUrl, line)
            for match in matches:
                return self.stSetUrl(line, match)

                # Export Existing Variable
            matches = re.findall(self.regexExportVar, line)
            for match in matches:
                return self.stExportVariable(line, match)

                # Export New Variable
                # Needs more work, maybe a method for determining this
            matches = re.findall(self.regexExportNewVar, line)
            for match in matches:
                return self.stExportVariable(line, match)

                # Import
            matches = re.findall(self.regexImport, line)
            for match in matches:
                return self.stImport(line, match)

            # Export
            matches = re.findall(self.regexExportRequest, line)
            for match in matches:
                return self.stExportRequest(line, match)

                # Name
            matches = re.findall(self.regexName, line)
            for match in matches:
                return self.stName(line, match)

                # Commandtax
            matches = re.findall(self.regexCommandtax, line)
            for match in matches:
                return self.stCommandtax(line, match)

                # self.stExecuteCommandtax(line, line)

                # matches = re.findall(self.regexCommandtax, line)
                # for match in matches:
                #  return self.stExecuteCommandtax(line, match)

        return None

    # Consumer
    def stName(self, line, match):
        matchStr = (match[4:])
        name = matchStr.strip()
        name = self.evaluateScriptax(name)
        self.data.name = name
        if (self.debug):
            self.log.log('> Setting Script Name: ' + name)
            self.log.log('')
        return ""

    def stRequire(self, line, match):
        return ""

    # Consumer
    def stExecuteCommandtax(self, line, match):
        matchStr = match[2:-2]
        importCommand = self.evaluateScriptax(matchStr, injectorsOnly=True)
        response = self.executeCommand(importCommand, returnRequest=True)
        return response.getResponseBody()

    # Consumer
    def stCommandtax(self, line, match):
        matchStr = match[1:]
        importCommand = self.evaluateScriptax(matchStr, injectorsOnly=True)
        self.executeCommand(importCommand)
        return ""

    # Consumer
    def stSetVariable(self, line, match):
        matchStr = match[3:]
        var = matchStr.split('=')
        vName = self.evaluateScriptax(var[0].strip())
        vVal = self.evaluateScriptax(var[1].strip())
        self.data.storeVar(vName, vVal)
        if (self.debug):
            self.log.log('> Assigning Variable: ' + vName + ' = ' + vVal)
            self.log.log('')
        return ""

    # Consumer
    def stSetUrl(self, line, match):
        matchStr = match[2:-2]
        matchStr = matchStr[matchStr.find(':') + 1:].strip()
        matchStr = self.evaluateScriptax(matchStr)
        urlData = json.loads(matchStr)
        uName = urlData['name'].strip()
        uVal = urlData['url'].strip()
        self.data.storeUrl(uName, uVal)
        if (self.debug):
            self.log.log('> Assigning URL: ' + uName + ' = ' + uVal)
            self.log.log('')
        return ""

        # Consumer

    def stImport(self, line, match):
        matchStr = (match[6:])
        importCommand = matchStr.strip()
        importCommand = self.evaluateScriptax(importCommand)

        request = self.executeCommand(importCommand, returnRequest=True)

        self.importCommandRequest(importCommand, request)

        if (self.debug):
            self.log.log('> Importing: ' + importCommand)
            self.log.log('')

        return ""

    # Consumer
    def stExportVariable(self, line, match):
        matchStr = (match[6:])
        varName = matchStr.strip()
        self.data.exportVar(varName)
        if (self.debug):
            self.log.log('> Exporting Variable: ' + varName + ' = ' + self.data.getVar(varName))
            self.log.log('')
        return ""

    # Consumer
    def stExportRequest(self, line, match):
        matchStr = (match[6:])
        importCommand = matchStr.strip()
        importCommand = self.evaluateScriptax(importCommand)

        request = self.executeCommand(importCommand, returnRequest=True)

        scriptName = self.importCommandRequest(importCommand, request, export=True)

        # self.data.exportRequest(scriptName)

        if (self.debug):
            self.log.log('> Exporting Request: ' + importCommand)
            self.log.log('')

        return ""

    # Injecter
    def stRequest(self, line, match):
        matchStr = match[2:-2]
        reqName = matchStr[matchStr.find(':') + 1:].strip()
        reqName = self.evaluateScriptax(reqName)
        # print(reqName)
        replacer = self.data.getRequest(reqName)
        try:
            line = line.replace(match, replacer)
        except:
            self.log.log('')
            self.log.error('Injection Failure. Cannot access request for data: ' + json.dumps(replacer))
            self.log.log('')
            return ""
        self.log.log('> Injecting Request \'' + reqName + '\': ' + line)
        self.log.log('')
        return line

    # Injecter
    def stUrl(self, line, match):
        matchStr = match[2:-2]
        urlName = matchStr[matchStr.find(':') + 1:].strip()
        urlName = self.evaluateScriptax(urlName)
        replacer = self.data.getUrl(urlName)
        try:
            line = line.replace(match, replacer)
        except:
            self.log.log('')
            self.log.error('Injection Failure. Cannot access url for data: ' + json.dumps(replacer))
            self.log.log('')
            return ""
        self.log.log('> Injecting URL \'' + urlName + '\': ' + line)
        self.log.log('')
        return line

    # Injecter
    def stVariable(self, line, match):
        matchStr = match[2:-2]
        # varName = matchStr[matchStr.find(':') + 1:].strip()
        varName = matchStr.strip()
        varName = self.evaluateScriptax(varName)
        replacer = self.data.getVar(varName)
        try:
            line = line.replace(match, replacer)
        except:
            self.log.log('')
            self.log.error('Injection Failure. Cannot access variable for data: ' + json.dumps(replacer))
            self.log.log('')
            return ""
        self.log.log('> Injecting Variable \'' + varName + '\': ' + line)
        self.log.log('')
        return line

    def importCommandRequest(self, command, request, export=False):

        scriptName = ""

        if (request.getResponseBody().strip() != ''):

            if (isinstance(request, Script)):

                if (request.data.name == ""):
                    # Gets the name of the script file when a name scriptax is not specified
                    fileName = os.path.basename(command[6:].strip())
                    if ("." in fileName):
                        fileName = fileName.split('.')[0]
                    request.data.name = fileName

                scriptName = request.data.name

                # self.data.store(commandHandler.getRequest().data.getRequestData(), prefix=scriptName)
                self.data.importScriptsExports(request.data, prefix=scriptName, export=export)
                # print(json.dumps(self.data.dataStore))
            else:
                self.data.storeRequest(request.getResponseBody(), export=export)
                # self.data.store(commandHandler.getRequest().getResponseBody())
            # self.request['text'][lineNumber] = {"command": importCommand.strip(), "status": commandHandler.getRequest().getResponseStatusCode(),"body":json.loads(commandHandler.getRequest().getResponseBody())}
        else:
            pass
            # self.request['text'][lineNumber] = {"command": importCommand.strip(), "status": commandHandler.getRequest().getResponseStatusCode(),"body":""}

        return scriptName

    def executeCommand(self, importCommand, returnRequest=False):
        from apitax.ah.commandtax.Command import Command

        commandHandler = Command(self.header, importCommand, self.config, debug=self.debug, sensitive=self.sensitive)

        if (returnRequest):
            return commandHandler.getRequest()
            # return json.dumps(dict({"command": importCommand.strip(), "status": commandHandler.getRequest().getResponseStatusCode(),"body":json.loads(commandHandler.getRequest().getResponseBody())}))

    # return json.dumps({"command": importCommand.strip(), "status": commandHandler.getRequest().getResponseStatusCode(),"body":json.loads(commandHandler.getRequest().getResponseBody())})
