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


# Default imports
import click

# Application imports
from .ah.web.WebServer import *
from .config.Config import Config as ConfigConsumer
from .grammar.grammartest import GrammarTest


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
        username = ''
        password = ''
        command = ''
        script = ''

        print('')
        print('')
        print(">>>  Apitax - Combining the power of Commandtax and Scriptax")
        print('')
        print('')


        config = ConfigConsumer()

        if (config.has('default-username')):
            username = config.get('default-username')

        if (config.has('default-password')):
            password = config.get('default-password')

        if (config.has('default-mode')):
            usage = config.get('default-mode')

        if ('--cli' in args):
            usage = 'cli'
        elif ('--web' in args):
            usage = 'web'
        elif('--grammar-test' in args):
            usage = 'grammar-test'

        if ('--debug' in args):
            debug = True

        if ('--sensitive' in args):
            sensitive = True

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

        if (usage == 'cli'):
            # Authentication is incorporated into Connector
            connector = Connector(debug=debug, sensitive=sensitive, command=command, username=username, password=password,
                                  json=True)
            result = connector.execute()
            print(json.dumps(result.getRequest().data.dataStore))
            # print(result.getRequest().data.getData('5.3.role_assignments.0.links.assignment'))

        elif (usage == 'web'):
            bSrv = bottleServer()
            bSrv.start(config.get("ip"), config.get("port"))

        elif(usage == 'grammar-test'):
            GrammarTest(script)

