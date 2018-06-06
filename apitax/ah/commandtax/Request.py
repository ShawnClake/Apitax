# System import
import json
import re

# Library import
import requests

# Application import
from apitax.logs.Log import Log

# Request is the 'legs' of the application.
# It is responsible to act as a facade to the 'requests' library
# This provides additional output, logging, and logic capabilities
class Request:
    def __init__(self, url, headers='', postData='', paramData={}, pathData={}, debug=False, sensitive=False,
                 customResponse=False):
        self.url = url
        self.headers = headers
        self.postData = postData
        self.paramData = paramData
        self.pathData = pathData
        self.debug = debug
        self.sensitive = sensitive
        self.request = None
        self.customResponse = customResponse
        self.log = Log()

    def setDebug(self, debug):
        self.debug = debug

    def setSensitive(self, sensitive):
        self.sensitive = sensitive

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

    def printCLIResponse(self):
        self.log.log(json.dumps(self.getResponseBodyAsStructure(), indent=2, separators=(',', ': ')))

    def printDebugResponse(self):
        self.log.log('Status: ' + str(self.getResponseStatusCode()))
        self.log.log('Headers:')
        if (self.sensitive):
            self.log.log('Headers are not shown as it contains sensitive data. ie. token')
        else:
            self.log.log(self.getResponseHeaders())
        self.log.log('Body:')
        self.log.log(self.getResponseBody())

    def printDebugRequest(self):
        self.log.log('Endpoint:        ' + self.url)
        self.log.log('Formed Endpoint: ' + self.getRequestUrl())
        self.log.log('Headers:')
        if (self.sensitive):
            self.log.log('Headers are not shown as it contains sensitive data. ie. password')
        else:
            self.log.log(self.headers)
        self.log.log('Post Data:')
        if (self.sensitive):
            self.log.log('Post Data is not shown as it contains sensitive data. ie. password')
        elif (not self.postData):
            self.log.log('{}')
        else:
            self.log.log(self.postData)

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
        if (self.debug):
            self.log.log('')
            self.log.log('<==========')
            self.printDebugRequest()

            self.log.log('')
            self.printDebugResponse()
            self.log.log('==========>')
            self.log.log('')
            self.log.log('')
        else:
            self.log.log('')
            self.log.log('<==========')
            self.printCLIResponse()
            self.log.log('==========>')
            self.log.log('')
            self.log.log('')

    def post(self):
        self.injectPathData()
        self.request = requests.post(self.url, data=json.dumps(self.postData), headers=self.headers,
                                     params=self.paramData)
        self.logRequest()
        # if(self.debug):
        #  self.log.log('')
        #  self.log.log('<==========')
        #  self.printDebugRequest()

        #  self.log.log('')
        #  self.printDebugResponse()
        #  self.log.log('==========>')
        #  self.log.log('')
        #  self.log.log('')
        # else:
        #  self.log.log('')
        #  self.log.log('<==========')
        #  self.printCLIResponse()
        #  self.log.log('==========>')
        #  self.log.log('')
        #  self.log.log('')

    def get(self):
        self.injectPathData()
        self.request = requests.get(self.url, data=json.dumps(self.postData), headers=self.headers,
                                    params=self.paramData)
        self.logRequest()
        # if(self.debug):
        #  self.log.log('')
        #  self.log.log('<==========')
        #  self.printDebugRequest()

        #  self.log.log('')
        #  self.printDebugResponse()
        #  self.log.log('==========>')
        #  self.log.log('')
        #  self.log.log('')
        # else:
        #  self.log.log('')
        #  self.log.log('<==========')
        #  self.printCLIResponse()
        #  self.log.log('==========>')
        #  self.log.log('')
        #  self.log.log('')

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
