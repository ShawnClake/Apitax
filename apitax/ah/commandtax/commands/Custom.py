# System import
import json
import shlex

# Library import
import click

# Application import
from apitax.ah.commandtax.Request import Request
from apitax.ah.HeaderBuilder import HeaderBuilder
from apitax.ah.Options import Options


# Handles custom commands
# This allows a user to access an arbitrary endpoint
class Custom(Request):
    def __init__(self, config=None, header=None, auth=None, parameters={}, options=Options()):
        Request.__init__(self, '', header.get(), '', options=options)

    # Executes the passed command
    def handle(self, command):
        if (type(command) is not list):
            command = shlex.split(command.strip())
        if (len(command) < 1):
            return

        cType = None

        if ('--get' in command):
            cType = 'get'
        elif ('--post' in command):
            cType = 'post'
        elif ('--put' in command):
            cType = 'put'
        elif ('--patch' in command):
            cType = 'patch'
        elif ('--delete' in command):
            cType = 'delete'
        else:
            print('Custom requests require a type e.g. --get or --post')
            return

        if ('--url' not in command):
            print('Custom requests require a --url')
            return

        url = command[command.index('--url') + 1]

        postData = ''  # Post Data
        paramData = ''  # Data container in the URL, but only the part after the ?: someurl.com/user/7?thisIsAParamData=true
        pathData = ''  # Data contained in the URL
        headerData = ''  # Data contained in the headers

        if ('--data-post' in command):
            postData = command[command.index('--data-post') + 1]
        elif(self.postData != {}):
            postData = json.dumps(self.postData)
        else:
            postData = {}

        if ('--data-query' in command):
            paramData = command[command.index('--data-query') + 1]

        if ('--data-path' in command):
            pathData = command[command.index('--data-path') + 1]

        if ('--data-header' in command):
            headerData = command[command.index('--data-header') + 1]

        self.setUrl(url)
        # print(command)
        if (postData != ''):
            self.setPostData(json.loads(str(postData)))
        if (paramData != ''):
            self.setParamData(json.loads(str(paramData)))
        if (pathData != ''):
            self.setPathData(json.loads(str(pathData)))
        if (headerData != ''):
            header = HeaderBuilder()
            header.build(self.headers)
            header.build(json.loads(str(headerData)))
            self.setHeaders(header.get())

        if (cType == 'get'):
            self.get()
        elif (cType == 'post'):
            self.post()
        elif (cType == 'put'):
            self.put()
        elif (cType == 'patch'):
            self.patch()
        elif (cType == 'delete'):
            self.delete()
        else:
            print('Invalid custom request type')
