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


def serialize(obj):
    return obj.serialize()


class Apitax:

    # Entry point of the program
    def apitax(self, args: list):
        # General procedure is as follows
        # Sets up logical defaults for parameters
        # Checks config for any overrides to those params
        # Checks cli params for any overrides to those params
        # CLI > Config > Default
        # args = sys.argv[1:]

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
        logPrexies = True
        logHumanReadable = False
        
        config = ConfigConsumer()
        config.path = str(Path(os.path.dirname(os.path.abspath(inspect.stack()[0][1]))).resolve())
        #print(config.path)

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
        elif('--grammar-test' in args):
            usage = 'grammar-test'
        elif('--build' in args):
            usage = 'build'
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
            
        
        loggingSettings = log.getLoggerSettings()
        
        log.log('>> Runtime Settings:')

        log.log('    * Debug: ' + str(debug))
               
        log.log('    * Sensitive: ' + str(sensitive))

        log.log('    * Operating out of: ' + str(config.path))

        log.log('    * Logging: ' + str(loggingSettings.get('doLog')))
        
        if(loggingSettings.get('doLog')):
            log.log('      * Log Filepath: ' + str(loggingSettings.get('path')))
            log.log('      * Colorize CLI: ' + str(loggingSettings.get('colorize')))
            
        log.log('')
        log.log('')

        if (usage == 'cli'):
            # Authentication is incorporated into Connector
            
            if(debug):
                log.log(">>> Starting Processing")
                log.log("")
                log.log("")
            
            connector = Connector(debug=debug, sensitive=sensitive, command=command, username=username, password=password,
                                  json=True)
            result = connector.execute()
            
            print(str(connector.http.getCatalog()))
            
            if(debug):
                log.log(">>> Finished Processing")
                log.log("")
                log.log("")
            
            if(debug and command.split(' ')[0] == 'script'):
                for t in result.getRequest().parser.threads:
                    t.join()
                log.log(">> Dumping Current DataStore State:")
                log.log("    * I recommend this website for looking at the data: http://json.parser.online.fr/")
                log.log("")
                log.log("")
                log.log(json.dumps(result.getRequest().parser.data.dataStore, default=serialize))
                log.log("")
                log.log("")
            # print(result.getRequest().data.getData('5.3.role_assignments.0.links.assignment'))

            if(debug):
                log.log(">> Apitax finished processing in " + round2str(connector.executionTime) + "s")
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

                #subprocess.check_call('npm --prefix ' + path + ' run build', shell=True)
                log.log("")
                log.log(">> Done Building Website Assets")
            log.log(">> Booting Up WebServer:")
            log.log("")
            bSrv = bottleServer()
            bSrv.start(config.get("ip"), config.get("port"), config=config, debug=debug, sensitive=sensitive, reloader=reloader)
            #log.log("")
            #log.log(">> Done Booting Server")
            #log.log(">> Ready To Take Requests")
            #log.log("")

        elif(usage == 'grammar-test'):
            GrammarTest(script)

        elif(usage == 'build'):
            subprocess.check_call('npm --help')
        
        elif(usage == 'feature-test'):
            pass
            #from apitax.integrations.Github import Github
            #token = str(config.get('github-access-token'))
            #git = Github(token)
            #print(git.getRepo('ApitaxScripts'))

        else:
            log.log("### Error: Unknown mode")
            
        log.getLoggerDriver().outputLog()
            
        #print(">> Apitax finished processing in {0:.2f}s".format(t1 - t0))




