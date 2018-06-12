# System import
import json

# Library import
from bottle import route, run, template, request, static_file, post, Bottle

# Application import
from apitax.ah.Connector import Connector
from apitax.drivers.HttpPlugFactory import HttpPlugFactory
from apitax.logs.Log import Log
from apitax.utilities.Files import readFile



# from command import Command
# from ahRequests.authentication import *


# BottleServer is used to provide a web interface which routes through Connector
# It is also used to serve css, html, and javascript

@route('/')
def index():
    return static_file('index.html', bottleServer.directory)

# Hosts html file which will be invoked from browser.
@route('/node/<staticFile>')
def serve_node(staticFile):
    return static_file(staticFile, bottleServer.directory+'node/dist/')

# Hosts html file which will be invoked from browser.
@route('/pages/<staticFile>')
def serve_static_file(staticFile):
    return static_file(staticFile, bottleServer.directory)


# host css files which will be invoked implicitly by your html files.
@route('/pages/css/<cssFile>')
def serve_css_files(cssFile):
    filePath = bottleServer.directory+'css/'
    return static_file(cssFile, filePath)


# host js files which will be invoked implicitly by your html files.
@route('/pages/js/<jsFile>')
def serve_js_files(jsFile):
    filePath = bottleServer.directory +'js/'
    return static_file(jsFile, filePath)


# Authentication endpoint is used to facilitate simpler authentication
@route('/apitax/auth/', method='POST')
def execute_api_auth():
    connector = Connector(sensitive=True, username=request.json['user'], password=request.json['pass'])

    if (connector.http.isTokenable()):
        return json.dumps({"status": 201, "auth": "presumed success", "token": connector.token,
                           "body": json.loads(connector.auth.getResponseBody())})
    else:
        return json.dumps({"status": 400,
                           "auth": "authentication does not support tokens, please pass username and password with each API request"})

@route('/dummy/<filename:path>')
def serve_dummy(filename):
    return static_file(filename, root='/directory/to/files')


# Command endpoint is used to facilitate simpler requests
@route('/apitax/command/', method='POST')
def execute_api_command():
    connector = None

    parameters = []
    
    if(request.json['parameters']):
        parameters = request.json['parameters']

    if ('token' in request.json):
        connector = Connector(token=request.json['token'], command=request.json['command'],
                              debug=request.json['debug'], sensitive=request.json['sensitive'], parameters=parameters)
    else:
        connector = Connector(username=request.json['user'], password=request.json['pass'],
                              command=request.json['command'], debug=request.json['debug'], sensitive=True, parameters=parameters)

    commandHandler = connector.execute()

    return json.dumps({"status": commandHandler.getRequest().getResponseStatusCode(),
                       "body": json.loads(commandHandler.getRequest().getResponseBody())})


# Command endpoint is used to facilitate simpler requests
@route('/apitax/system/status', method='GET')
def execute_system_status():

    configDict = bottleServer.config.serialize(["driver", "log", "log-file", "log-colorize"])
    configDict.update({'debug':bottleServer.debug, 'sensitive':bottleServer.sensitive})
    return json.dumps(configDict)
    
# Command endpoint is used to facilitate simpler requests
@route('/apitax/system/driver/status', method='GET')
def execute_system_driver_status():
    http = HttpPlugFactory.make(bottleServer.config.get('driver') + 'Driver')
    driverDict = {"driver": {"name":bottleServer.config.get('driver')}}
    driverDict['driver'].update(http.serialize(bottleServer.config))
    return json.dumps(driverDict)
    
# Command endpoint is used to facilitate simpler requests
@route('/apitax/system/scripts/catalog', method='GET')
def execute_system_scripts_catalog():
    http = HttpPlugFactory.make(bottleServer.config.get('driver') + 'Driver')
    return json.dumps(http.getScriptsCatalog())
    
# Command endpoint is used to facilitate simpler requests
@route('/apitax/system/catalog', method='GET')
def execute_system_catalog():
    http = HttpPlugFactory.make(bottleServer.config.get('driver') + 'Driver')
    return json.dumps(http.getCatalog())
    
# Command endpoint is used to facilitate simpler requests
@route('/apitax/system/scripts', method='POST')
def execute_system_scripts():
    # http = HttpPlugFactory.make(bottleServer.config.get('driver') + 'Driver')
    return json.dumps({"contents": readFile(request.json['file'])})
    	
    	
# Command endpoint is used to facilitate simpler requests
@route('/apitax/system/scripts/save', method='POST')
def execute_system_scripts_create():
    # http = HttpPlugFactory.make(bottleServer.config.get('driver') + 'Driver')
    with open(request.json['file-name'], "w") as text_file:
        print(request.json['file'], file=text_file)
    # print(request.json['file'])
    return json.dumps({'status':200})

class bottleServer():

    directory = 'apitax/ah/web/node/'
    log = Log()
    config = None
    debug = False
    sensitive = False
    
    def start(self, ip, port, config=None, debug=False, sensitive=False):
        # self.app = Bottle()
        bottleServer.config = config
        bottleServer.debug = debug
        bottleServer.sensitive = sensitive
        run(host=ip, port=port, reloader=True, debug=debug)

