# System import
import json

# Library import
from bottle import route, run, template, request, static_file, post, Bottle

# Application import
from connector import Connector


# from command import Command
# from ahRequests.authentication import *


# BottleServer is used to provide a web interface which routes through Connector
# It is also used to serve css, html, and javascript

@route('/')
def index():
    return static_file('index.html', 'webSrv/pages/')


# Hosts html file which will be invoked from browser.
@route('/pages/<staticFile>')
def serve_static_file(staticFile):
    filePath = 'webSrv/pages/'
    return static_file(staticFile, filePath)


# host css files which will be invoked implicitly by your html files.
@route('/pages/css/<cssFile>')
def serve_css_files(cssFile):
    filePath = 'webSrv/pages/css/'
    return static_file(cssFile, filePath)


# host js files which will be invoked implicitly by your html files.
@route('/pages/js/<jsFile>')
def serve_js_files(jsFile):
    filePath = 'webSrv/pages/js/'
    return static_file(jsFile, filePath)


# Authentication endpoint is used to facilitate simpler authentication
@route('/api/auth/', method='POST')
def execute_api_auth():
    connector = Connector(sensitive=True, username=request.json['user'], password=request.json['pass'])

    if (connector.http.isTokenable()):
        return json.dumps({"status": 201, "auth": "presumed success", "token": connector.token,
                           "body": json.loads(connector.auth.getResponseBody())})
    else:
        return json.dumps({"status": 400,
                           "auth": "authentication does not support tokens, please pass username and password with each API request"})


# Command endpoint is used to facilitate simpler requests
@route('/api/command/', method='POST')
def execute_api_command():
    connector = None

    if ('token' in request.json):
        connector = Connector(token=request.json['token'], command=request.json['command'],
                              debug=request.json['debug'], sensitive=request.json['sensitive'])
    else:
        connector = Connector(username=request.json['user'], password=request.json['pass'],
                              command=request.json['command'], debug=request.json['debug'], sensitive=True)

    commandHandler = connector.execute()

    return json.dumps({"status": commandHandler.getRequest().getResponseStatusCode(),
                       "body": json.loads(commandHandler.getRequest().getResponseBody())})


@route('/dummy/<filename:path>')
def serve_dummy(filename):
    return static_file(filename, root='/directory/to/files')


class bottleServer():

    def start(self, ip, port):
        # self.app = Bottle()
        run(host=ip, port=port, reloader=True, debug=True)

