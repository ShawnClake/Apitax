# System import
import json
import re

# Library import
import requests

# Application import
from apitax.logs.Log import Log
from apitax.ah.Options import Options

# Request is the 'legs' of the application.
# It is responsible to act as a facade to the 'requests' library
# This provides additional output, logging, and logic capabilities
class Request:
    def __init__(self, url, headers='', postData='', paramData={}, pathData={}, options=Options(),
                 customResponse=False):
        self.url = url
        self.headers = headers
        self.postData = postData
        self.paramData = paramData
        self.pathData = pathData
        self.options = options
        self.request = None
        self.customResponse = customResponse
        self.log = Log()
        self.humanReadable = self.log.getLoggerSettings().get('human-readable')

    def setDebug(self, debug):
        self.options.debug = debug

    def setSensitive(self, sensitive):
        self.options.sensitive = sensitive

    def setHeaders(self, headers):
        self.headers = headers

    def setUrl(self, url):
        self.url = url

    def setPostData(self, postData):
        self.postData = postData

    def setParamData(self, paramData):
        self.paramData = paramData

    def setPathData(self, pathData):
        self.pathData = pathData

    def getRequestUrl(self):
        return self.request.url

    def getResponse(self):
        return self.request

    def getResponseHeaders(self):
        if (self.customResponse):
            return self.request['headers']
        else:
            return self.request.headers

    def getResponseBody(self):
        if (self.customResponse):
            if(isinstance(self.request['text'], dict)):
                return json.dumps(self.request['text'], separators=(',', ':'), indent=None).replace("\n", "")
            return self.request['text'].replace("\n", "")
        else:
            if(isinstance(self.request.text, dict) or isinstance(self.request.text, list)):
                return json.dumps(self.request.text, separators=(',', ':'), indent=None).replace("\n", "")
            return self.request.text.replace("\n", "")

    def getResponseBodyAsStructure(self):
        return json.loads(self.getResponseBody())

    def getResponseStatusCode(self):
        if (self.customResponse):
            return self.request['status_code']
        else:
            return self.request.status_code

    def getCLIResponse(self):
        return json.dumps(self.getResponseBodyAsStructure(), indent=2, separators=(',', ': '))

    def getDebugResponse(self):
        line = ''
        line += 'Status: ' + str(self.getResponseStatusCode()) + '\n'
        line += 'Headers:' + '\n'
        if (self.options.sensitive):
            line += 'Headers are not shown as it contains sensitive data. ie. token' + '\n'
        else:
            line += str(self.getResponseHeaders()) + '\n'
        line += 'Body:' + '\n'
        line += str(self.getResponseBody()) + '\n'
        return line

    def getDebugRequest(self):
        line = ''
        line += 'Endpoint:        ' + self.url + '\n'
        line += 'Formed Endpoint: ' + self.getRequestUrl() + '\n'
        line += 'Headers:' + '\n'
        if (self.options.sensitive):
            line += 'Headers are not shown as it contains sensitive data. ie. password' + '\n'
        else:
            line += str(self.headers) + '\n'
        line += 'Post Data:' + '\n'
        if (self.options.sensitive):
            line += 'Post Data is not shown as it contains sensitive data. ie. password' + '\n'
        elif (not self.postData):
            line += '{}' + '\n'
        else:
           line += str(self.postData) + '\n'
        return line

    def injectPathData(self):
        if (not self.pathData):
            return
        matches = re.findall('{[A-z0-9]{1,}}', self.url)
        for match in matches:
            matchStr = match[1:-1]
            if (matchStr in self.pathData):
                self.url = self.url.replace(match, self.pathData.get(matchStr))
            else:
                self.log.log('Path data did not contain key for `' + matchStr + '`')

    def logRequest(self):
        if (self.options.debug and not self.humanReadable):
            self.log.log('\n<==========' + '\n' + self.getDebugRequest() + '\n' + self.getDebugResponse() + '==========>' + '\n\n')

        elif(self.options.debug):
            self.log.log('\n<==========\n' + self.getCLIResponse() + '\n' + '==========>\n\n')

    def post(self):
        self.injectPathData()
        self.request = requests.post(self.url, data=json.dumps(self.postData), headers=self.headers,
                                     params=self.paramData)
        self.logRequest()

    def get(self):
        self.injectPathData()
        self.request = requests.get(self.url, data=json.dumps(self.postData), headers=self.headers,
                                    params=self.paramData)
        self.logRequest()

    def put(self):
        self.injectPathData()
        self.request = requests.put(self.url, data=json.dumps(self.postData), headers=self.headers,
                                    params=self.paramData)
        self.logRequest()

    def patch(self):
        self.injectPathData()
        self.request = requests.patch(self.url, data=json.dumps(self.postData), headers=self.headers,
                                      params=self.paramData)
        self.logRequest()

    def delete(self):
        self.injectPathData()
        self.request = requests.delete(self.url, data=json.dumps(self.postData), headers=self.headers,
                                       params=self.paramData)
        self.logRequest()
