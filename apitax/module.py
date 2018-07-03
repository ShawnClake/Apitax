# Apitax
# Originally created by Shawn Clake
# shawn.clake@gmail.com
# May 2018
#
# Contains Scriptax and Commandtax
#
# This application is used to automate API processes using arbitrary API's
# It includes a CLI as well as web interface
# However the web interface will need to be customized per API usage

# System imports
import json
import sys
import os
import inspect
from pathlib import Path
from time import time

# Default imports
import click

# Application imports
from apitax.ah.Connector import Connector
from .config.Config import Config as ConfigConsumer
from .grammar.grammartest import GrammarTest
from .logs.Log import Log
from .logs.BufferedLog import BufferedLog
from .logs.StandardLog import StandardLog
from apitax.utilities.Numbers import round2str
from apitax.utilities.Npm import Npm
from apitax.ah.Options import Options
from apitax.ah.LoadedDrivers import LoadedDrivers
from apitax.utilities.Files import getRootPath


def serialize(obj):
    return obj.serialize()


class Apitax:

    # Entry point of the program
    def __init__(self, args: list):
        # General procedure is as follows
        # Sets up logical defaults for parameters
        # Checks config for any overrides to those params
        # Checks cli params for any overrides to those params
        # CLI > Config > Default

        t0 = time()

        if(len(args) == 0):
            args = sys.argv[1:]

        usage = 'cli'
        
        debug = False
        sensitive = False
        
        reloader = False
        watcher = False
        
        username = ''
        password = ''
        
        command = ''
        script = ''
        
        build = True
        
        doLog = True
        logPath = 'logs/apitax.log'
        logColorize = True
        logPrefixes = True
        logHumanReadable = False
        
        #print(getRootPath('/config.txt'))
        configFile = getRootPath('/config.txt')
        config = ConfigConsumer.read(configFile)
        config.path = str(Path(os.path.dirname(os.path.abspath(inspect.stack()[0][1]))).resolve())
        #print(getRootPath())

        if (config.has('default-username')):
            username = config.get('default-username')

        if (config.has('default-password')):
            password = config.get('default-password')

        if (config.has('default-mode')):
            usage = config.get('default-mode')
            
        if (config.has('log')):
            doLog = config.get('log')
            
        if (config.has('log-file')):
            logPath = config.get('log-file')
            
        if (config.has('log-colorize')):
            logColorize = config.get('log-colorize')
            
        if (config.has('log-human-readable')):
            logHumanReadable = config.get('log-human-readable')
            
        if (config.has('log-prefixes')):
            logPrefixes = config.get('log-prefixes')

        log = Log(StandardLog(), logFile=logPath, doLog=doLog, logColorize=logColorize, logPrefixes=logPrefixes, logHumanReadable=logHumanReadable)
        
        log.log('')
        log.log('')
        log.log(">>>  Apitax - Combining the power of Commandtax and Scriptax")
        log.log('')
        log.log('') 

        if ('--cli' in args):
            usage = 'cli'
        elif ('--web' in args):
            usage = 'web'
        elif ('--build-only' in args):
            usage = 'build'
        elif('--grammar-test' in args):
            usage = 'grammar-test'
        elif('--feature-test' in args):
            usage = 'feature-test'

        if ('--debug' in args):
            debug = True

        if ('--sensitive' in args):
            sensitive = True
            
        if ('--reloader' in args):
            reloader = True
            
        if ('--watcher' in args):
            watcher = True
            
        if ('--dev' in args):
            watcher = True
            reloader = True
            
        if ('--no-build' in args):
            build = False

        if ('-u' in args):
            username = args[args.index('-u') + 1]

        if ('-p' in args):
            password = click.prompt('Enter Your Password', hide_input=True)

        if ('-s' in args):
            script = args[args.index('-s') + 1]

        if ('-r' in args):
            command = args[args.index('-r') + 1]
        elif (script == '' and usage == 1):
            command = click.prompt('R')

        # This is to turn the '-s' flag into a command behind the scenes
        if (script != ''):
            command = 'script ' + script
        
        options = Options(debug=debug, sensitive=sensitive)    
        
        loggingSettings = log.getLoggerSettings()
        
        log.log('>> Runtime Settings:')

        log.log('    * Using config: ' + configFile)

        log.log('    * Debug: ' + str(debug))
               
        log.log('    * Sensitive: ' + str(sensitive))

        log.log('    * Operating out of: ' + str(config.path))

        log.log('    * Logging: ' + str(loggingSettings.get('doLog')))
        
        if(loggingSettings.get('doLog')):
            log.log('      * Log Filepath: ' + str(loggingSettings.get('path')))
            log.log('      * Colorize CLI: ' + str(loggingSettings.get('colorize')))
            
        log.log('')
        log.log('')
        
        if(options.debug):
            log.log('>> Loading Drivers')
            log.log('')
            drivers = config.getAsList('drivers')
            for driver in drivers:
                LoadedDrivers.load(driver)
            log.log('>> Finished Loading Drivers')
        
            log.log('')
            log.log('')        

        if (usage == 'cli'):
            # Authentication is incorporated into Connector
            
            if(options.debug):
                log.log(">>> Starting Processing")
                log.log("")
                log.log("")
            
            connector = Connector(options=options, command=command, username=username, password=password,
                                  json=True)
            result = connector.execute()
            
            #print(str(connector.http.getCatalog()))
            
            if(options.debug):
                log.log(">>> Finished Processing")
                log.log("")
                log.log("")
            
            if(options.debug and command.split(' ')[0] == 'script'):
                for t in result.getRequest().parser.threads:
                    t.join()
                log.log(">> Dumping Current DataStore Status:")
                log.log("    * I recommend this website for looking at the data: http://json.parser.online.fr/")
                log.log("")
                log.log("")
                log.log(json.dumps(result.getRequest().parser.data.getStatus(), default=serialize))
                log.log("")
                log.log("")
            # print(result.getRequest().data.getData('5.3.role_assignments.0.links.assignment'))
            
            if(options.debug):
                log.log(">> Apitax finished processing in " + round2str(time() - t0) + "s")
                log.log("")
                log.log("")

        elif (usage == 'web'):
            from .ah.web.WebServer import bottleServer
            if(build):
                log.log(">> Building Website Assets:")
                log.log("")
                path = config.path + '/ah/web/node/node'
                npm = Npm(path)
                npm.install()
                npm.build()
                if(watcher):
                    npm.buildWatch(True)
                log.log("")
                log.log(">> Done Building Website Assets")
            log.log(">> Booting Up WebServer:")
            log.log("")
            bSrv = bottleServer()
            bSrv.start(config.get("ip"), config.get("port"), config=config, options=options, reloader=reloader)

        elif(usage == 'grammar-test'):
            GrammarTest(script)
        
        elif(usage == 'feature-test'):
            from apitax.drivers.DriverCommandsFactory import DriverCommandsFactory
            customCommands = DriverCommandsFactory.make(config.get('driver') + 'Commands')
            customCommands.setup(config, None, None, {}, debug, sensitive)
            print(str(customCommands.getCatalog()))

        elif(usage == 'build'):
            log.log(">> Building:")
            log.log("> This can take several minutes")
            log.log("")
            path = config.path + '/ah/web/node/node'
            npm = Npm(path)
            npm.install()
            npm.build()
            log.log("")
            log.log(">> Building Complete")


        else:
            log.log("### Error: Unknown mode")
            
        log.getLoggerDriver().outputLog()
            
        #print(">> Apitax finished processing in {0:.2f}s".format(t1 - t0))




