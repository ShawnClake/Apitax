# System import

# Application import
from apitax.logs.Log import Log

from apitax.grammar.build.Ah210Lexer import Ah210Lexer
from apitax.grammar.build.Ah210Parser import Ah210Parser
from apitax.grammar.Ah2Listener import Ah2Listener
from apitax.grammar.Ah2Visitor import Ah2Visitor
from apitax.utilities.Files import getPath
from apitax.ah.LoadedDrivers import LoadedDrivers

from antlr4 import *

# Script is used to automate the execution of many commands
class Scriptax():
    def __init__(self, config, header, auth, parameters, options):
        self.header = header
        self.auth = auth
        self.options = options
        self.parameters = parameters
        self.config = config
        self.log = Log('logs/log.log')

    # Begins executing the script from top to bottom & handles nested scripts
    def execute(self, filepath):
        
        #if(filepath[:1] != '/'):  
        #    if(self.options.driver):
        #        driver = LoadedDrivers.getBaseDriver(self.options.driver)
        #    else:
        #        driver = LoadedDrivers.getDefaultBaseDriver()
        # 
        #    filepath = driver.getScriptsPath(filepath)
        
        if (self.options.debug):
            self.log.log('>>> Opening Script: ' + filepath)
            self.log.log('')
            self.log.log('')

        if(self.options.driver):
            driver = LoadedDrivers.getBaseDriver(self.options.driver)
        else:
            driver = LoadedDrivers.getDefaultBaseDriver()

        input = InputStream(driver.readScript(filepath))

        #input = FileStream(filepath)
        lexer = Ah210Lexer(input)
        stream = CommonTokenStream(lexer)
        parser = Ah210Parser(stream)
        tree = parser.prog()
        printer = Ah2Listener()

        visitor = Ah2Visitor(self.config, self.header, self.auth, parameters=self.parameters, options=self.options)
        visitor.setState(file=getPath(filepath))
        return visitor.visit(tree)
        