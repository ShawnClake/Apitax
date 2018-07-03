# System import
import json

# Library import
from bottle import route, run, template, request, static_file, post, Bottle

# Application import
from apitax.ah.Connector import Connector
from apitax.ah.LoadedDrivers import LoadedDrivers
from apitax.logs.Log import Log
from apitax.utilities.Files import readFile
from apitax.utilities.Files import saveFile
from apitax.utilities.Files import deleteFile
from apitax.utilities.Files import renameFile
from apitax.utilities.Files import getPath
from apitax.ah.Options import Options


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
                              options=Options(debug=request.json['debug'], sensitive=request.json['sensitive']), parameters=parameters)
    else:
        connector = Connector(username=request.json['user'], password=request.json['pass'],
                              command=request.json['command'], options=Options(debug=request.json['debug'], sensitive=True), parameters=parameters)

    commandHandler = connector.execute()

    returner = {"status": commandHandler.getRequest().getResponseStatusCode(),
                       "body": json.loads(commandHandler.getRequest().getResponseBody())}
                       	
    if(request.json['debug']):
         returner.update({"log": connector.logBuffer})

    return json.dumps(returner)


# Command endpoint is used to facilitate simpler requests
@route('/apitax/system/status', method='GET')
def execute_system_status():

    configDict = bottleServer.config.serialize(["driver", "log", "log-file", "log-colorize"])
    configDict.update({'debug':bottleServer.options.debug, 'sensitive':bottleServer.options.sensitive})
    return json.dumps(configDict)
    
# Command endpoint is used to facilitate simpler requests
@route('/apitax/system/driver/status', method='GET')
def execute_system_driver_status():
    driver = LoadedDrivers.getDefaultBaseDriver()
    driverDict = {"driver": {"name":str(driver.__class__.__name__)}}
    driverDict['driver'].update(driver.serialize())
    return json.dumps(driverDict)
    
# Command endpoint is used to facilitate simpler requests
@route('/apitax/system/scripts/catalog', method='GET')
def execute_system_scripts_catalog():
    driver = LoadedDrivers.getDefaultBaseDriver()
    return json.dumps(driver.getScriptsCatalog())
    
# Command endpoint is used to facilitate simpler requests
@route('/apitax/system/catalog', method='GET')
def execute_system_catalog():
    driver = LoadedDrivers.getDefaultBaseDriver()
    return json.dumps(driver.getCatalog(request.json['token']))
    
# Command endpoint is used to facilitate simpler requests
@route('/apitax/system/scripts', method='POST')
def execute_system_scripts():
    # http = HttpPlugFactory.make(bottleServer.config.get('driver') + 'Driver')
    return json.dumps({'status':200, "contents": readFile(request.json['file-name'])})
    	
    	
# Command endpoint is used to facilitate simpler requests
@route('/apitax/system/scripts/save', method='POST')
def execute_system_scripts_save():
    saveFile(request.json['file-name'], request.json['file'])
    return json.dumps({'status':200, 'file-name': getPath(request.json['file-name'])})
    	
# Command endpoint is used to facilitate simpler requests
@route('/apitax/system/scripts/rename', method='POST')
def execute_system_scripts_rename():
    if(not renameFile(request.json['file-name-original'], request.json['file-name-new'])):
        return json.dumps({'status':500,'message':'Cannot rename to an existing file.'})
    return json.dumps({'status':200, 'file-name': getPath(request.json['file-name-new'])})
    	
# Command endpoint is used to facilitate simpler requests
@route('/apitax/system/scripts/delete', method='POST')
def execute_system_scripts_delete():
    deleteFile(request.json['file-name'])
    return json.dumps({'status':200})

class bottleServer():

    directory = 'apitax/ah/web/node/'
    log = Log()
    config = None
    options = None
    
    def start(self, ip, port, config=None, options=Options(), reloader=False):
        # self.app = Bottle()
        bottleServer.config = config
        bottleServer.options = options
        bottleServer.directory = config.path + '/ah/web/node/'
        run(host=ip, port=port, reloader=reloader, debug=options.debug)

