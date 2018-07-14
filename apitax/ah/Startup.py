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
from apitax.config.Config import Config as ConfigConsumer
from apitax.grammar.grammartest import GrammarTest
from apitax.utilities.Numbers import round2str
from apitax.utilities.Npm import Npm
from apitax.ah.Options import Options
from apitax.ah.LoadedDrivers import LoadedDrivers
from apitax.utilities.Files import getRootPath
from apitax.ah.Credentials import Credentials

from apitax.logs.Log import Log
from apitax.logs.BufferedLog import BufferedLog
from apitax.logs.StandardLog import StandardLog

from apitax.ah.State import State

def serialize(obj):
    return obj.serialize()

class Startup:
    def __init__(self, passedArgs: list):
        self.t0 = time()

        if (len(passedArgs) == 0):
            self.args = sys.argv[1:]
        else:
            self.args = passedArgs

        self.usage = 'cli'

        self.debug = False
        self.sensitive = False

        self.reloader = False
        self.watcher = False

        self.username = ''
        self.password = ''

        self.command = ''
        self.script = ''

        self.build = True

        self.doLog = True
        self.logPath = '/logs/apitax.log'
        self.logColorize = True
        self.logPrefixes = True
        self.logHumanReadable = False

        # print(getRootPath('/config.txt'))
        configFile = getRootPath('/config.txt')
        self.config = ConfigConsumer.read()
        self.config.path = str(Path(os.path.dirname(os.path.abspath(inspect.stack()[0][1]))).resolve())
        # print(getRootPath())

        if (self.config.has('default-mode')):
            self.usage = self.config.get('default-mode')

        if (self.config.has('log')):
            self.doLog = self.config.get('log')

        if (self.config.has('log-file')):
            self.logPath = self.config.get('log-file')

        if (self.config.has('log-colorize')):
            self.logColorize = self.config.get('log-colorize')

        if (self.config.has('log-human-readable')):
            self.logHumanReadable = self.config.get('log-human-readable')

        if (self.config.has('log-prefixes')):
            self.logPrefixes = self.config.get('log-prefixes')

        if (self.logPath[:1] != '/'):
            self.logPath = '/' + self.logPath

        self.logPath = getRootPath(self.logPath)

        self.log = Log(StandardLog(), logFile=self.logPath, doLog=self.doLog, logColorize=self.logColorize, logPrefixes=self.logPrefixes,
                  logHumanReadable=self.logHumanReadable)

        self.log.log('')
        self.log.log('')
        self.log.log(">>>  Apitax - Combining the power of Commandtax and Scriptax")
        self.log.log('')
        self.log.log('')

        if ('--cli' in self.args):
            self.usage = 'cli'
        elif ('--web' in self.args):
            self.usage = 'web'
        elif ('--build-only' in self.args):
            self.usage = 'build'
        elif ('--grammar-test' in self.args):
            self.usage = 'grammar-test'
        elif ('--feature-test' in self.args):
            self.usage = 'feature-test'

        if ('--debug' in self.args):
            self.debug = True

        if ('--sensitive' in self.args):
            self.sensitive = True

        if ('--reloader' in self.args):
            self.reloader = True

        if ('--watcher' in self.args):
            self.watcher = True

        if ('--dev' in self.args):
            self.watcher = True
            self.reloader = True

        if ('--no-build' in self.args):
            self.build = False

        if ('-u' in self.args):
            self.username = self.args[self.args.index('-u') + 1]

        if ('-p' in self.args):
            self.password = click.prompt('Enter Your Password', hide_input=True)

        if ('-s' in self.args):
            self.script = self.args[self.args.index('-s') + 1]

        if ('-r' in self.args):
            self.command = self.args[self.args.index('-r') + 1]
        elif (self.script == '' and self.usage == 1):
            self.command = click.prompt('R')

        # This is to turn the '-s' flag into a command behind the scenes
        if (self.script != ''):
            self.command = 'script ' + self.script

        self.options = Options(debug=self.debug, sensitive=self.sensitive)

        self.loggingSettings = self.log.getLoggerSettings()

        self.log.log('>> Runtime Settings:')

        self.log.log('    * Using config: ' + configFile)

        self.log.log('    * Debug: ' + str(self.debug))

        self.log.log('    * Sensitive: ' + str(self.sensitive))

        self.log.log('    * Operating out of: ' + str(self.config.path))

        self.log.log('    * Logging: ' + str(self.loggingSettings.get('doLog')))

        if (self.loggingSettings.get('doLog')):
            self.log.log('      * Log Filepath: ' + str(self.loggingSettings.get('path')))
            self.log.log('      * Colorize CLI: ' + str(self.loggingSettings.get('colorize')))

        self.log.log('')
        self.log.log('')

        if (self.options.debug):
            self.log.log('>> Loading Drivers')
            self.log.log('')

        drivers = self.config.getAsList('drivers')
        for driver in drivers:
            LoadedDrivers.load(driver)

        if (self.options.debug):
            self.log.log('>> Finished Loading Drivers')

            self.log.log('')
            self.log.log('')

        if (self.username == '' and self.config.has('default-username')):
            self.username = LoadedDrivers.getDefaultBaseDriver().getDefaultUsername()  # config.get('default-username')

        if (self.password == '' and self.config.has('default-password')):
            self.password = LoadedDrivers.getDefaultBaseDriver().getDefaultPassword()  # config.get('default-password')

        # Setup App State
        State.config = self.config
        State.options = self.options
        State.log = self.log
        State.paths['node'] = getRootPath('/apitax/ah/api/dashboard')
        State.paths['logs'] = self.logPath
        State.paths['root'] = getRootPath()
        State.paths['config'] = configFile

    def execute(self):
        if (self.usage == 'cli'):
            # Authentication is incorporated into Connector

            if (self.options.debug):
                self.log.log(">>> Starting Processing")
                self.log.log("")
                self.log.log("")

            self.connector = Connector(options=self.options, command=self.command,
                              credentials=Credentials(username=self.username, password=self.password),
                              json=True)
            self.result = self.connector.execute()

            # print(str(connector.http.getCatalog()))

            if (self.options.debug):
                self.log.log(">>> Finished Processing")
                self.log.log("")
                self.log.log("")

            if (self.options.debug and self.command.split(' ')[0] == 'script'):
                for t in self.result.getRequest().parser.threads:
                    t.join()
                self.log.log(">> Dumping Current DataStore Status:")
                self.log.log("    * I recommend this website for looking at the data: http://json.parser.online.fr/")
                self.log.log("")
                self.log.log("")
                self.log.log(json.dumps(self.result.getRequest().parser.data.getStatus(), default=serialize))
                self.log.log("")
                self.log.log("")
            # print(result.getRequest().data.getData('5.3.role_assignments.0.links.assignment'))

            if (self.options.debug):
                self.log.log(">> Apitax finished processing in " + round2str(time() - self.t0) + "s")
                self.log.log("")
                self. log.log("")

        elif (self.usage == 'web'):
            from apitax.ah.api.Server import startDevServer
            if (self.build):
                self.log.log(">> Building Website Assets:")
                self.log.log("")
                path = State.paths['node']
                self.npm = Npm(path)
                self.npm.install()
                self.npm.build()
                if (self.watcher):
                    self.npm.buildWatch(True)
                self.log.log("")
                self.log.log(">> Done Building Website Assets")
            self.log.log(">> Booting Up WebServer:")
            self.log.log("")
            self.server = startDevServer(self.config.get("ip"), self.config.get("port"))
            #bSrv.start(config.get("ip"), config.get("port"), config=config, options=options, reloader=reloader)

        elif (self.usage == 'grammar-test'):
            GrammarTest(self.script)

        elif (self.usage == 'feature-test'):
            pass

        elif (self.usage == 'build'):
            self.log.log(">> Building:")
            self.log.log("> This can take several minutes")
            self.log.log("")
            path = State.paths['node']
            self.npm = Npm(path)
            self.npm.install()
            self.npm.build()
            self.log.log("")
            self.log.log(">> Building Complete")


        else:
            self.log.log("### Error: Unknown mode")

        self.log.getLoggerDriver().outputLog()

        # print(">> Apitax finished processing in {0:.2f}s".format(t1 - t0))
