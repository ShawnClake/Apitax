# System import
import json
import re
import os
import sys


# Application import
from apitax.logs.Log import Log
from apitax.ah.scriptax.ScriptData import ScriptData

from apitax.grammar.build.Ah210Lexer import Ah210Lexer
from apitax.grammar.build.Ah210Parser import Ah210Parser
from apitax.grammar.Ah2Listener import Ah2Listener
from apitax.grammar.Ah2Visitor import Ah2Visitor

from antlr4 import *


# TODO:
#  Change the way request is saved to include status code & command run
#  Add additional syntaxes for import & exporting


# Script is used to automate the execution of many commands
class Scriptax():
    def __init__(self, config, header, parameters, debug, sensitive):
        self.header = header
        self.debug = debug
        self.sensitive = sensitive
        self.parameters = parameters
        self.config = config
        self.log = Log('logs/log.log')

    # Begins executing the script from top to bottom & handles nested scripts
    def execute(self, filepath):
        if (self.debug):
            self.log.log('>>> Opening Script: ' + filepath)
            self.log.log('')
            self.log.log('')
            
        input = FileStream(filepath)
        lexer = Ah210Lexer(input)
        stream = CommonTokenStream(lexer)
        parser = Ah210Parser(stream)
        tree = parser.prog()
        printer = Ah2Listener()

        visitor = Ah2Visitor(self.config, self.header, parameters=self.parameters, debug=self.debug, sensitive=self.sensitive)
        return visitor.visit(tree)
        
        
        # commandHandler = None
        # with open(filepath) as fileObj:
        #    i = 0
        #    self.request = {}
        #    self.request['text'] = {}
        #    for line in fileObj:
        #        if (line.strip() == ''):
        #            continue
        #        line = ''.join(line.splitlines())

        #        self.log.log('> Now processing: ' + line)
        #        self.log.log('')

        #        self.evaluateScriptax(line)
        #        self.log.log('')

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

        #        i += 1
        #    self.request['text'] = json.dumps(self.request['text'])
        #    self.request['status_code'] = 200
