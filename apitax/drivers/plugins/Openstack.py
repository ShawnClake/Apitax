from apitax.drivers.HttpPlug import HttpPlug
from apitax.utilities.Files import getAllFiles
from pathlib import Path

class OpenstackDriver(HttpPlug):

    def __init__(self):
        self.token = None
        super().__init__()
	
    def getToken(self, response):
        self.token = response.getResponseHeaders().get('X-Subject-Token')
        return self.token
    
    def getTokenAuthHeader(self, token):
        return {'X-Auth-Token': token}
    
    def getPasswordAuthData(self, username, password):
        return {'auth': {'identity': {'methods': ['password'], 'password': {'user': {'domain': {'id': 'default'}, 'password': password, 'name': username}}} }}
    
    def isCredentialsPosted(self):
       	return True  	
  	   
    def getScriptsCatalog(self, config):
        files = getAllFiles(config.path + "/grammar/scripts/**/*.ah")
        returner = {"scripts": []}
        for file in files:
            returner['scripts'].append({"label": file.split('/')[-1].split('.')[0].title(),"relative-path":file,"path": str(Path(file).resolve())})
        # print(returner)
        return returner
        
    def getCatalog(self):
        from apitax.ah.Connector import Connector
        import json
        connector = Connector(token=self.token, command="custom --get --url " + self.getCatalogEndpoint(),
                              debug=False, sensitive=True, parameters=None)
        
        commandHandler = connector.execute()

        services = json.loads(commandHandler.getRequest().getResponseBody())
        
        catalog = {}
        catalog['endpoints'] = {}
        
        for service in services['catalog']:
            endpoints = service['endpoints']
            if(len(endpoints) > 0):
                endpoint = endpoints[0]
                name = service['name']
                catalog['endpoints'].update({name: {"label": name, "value": endpoint['url']}})
        
        #catalog['endpoints'].update({"tests": {"label": "(Test) JSONPlaceHolder - https://jsonplaceholder.typicode.com", "value": "https://jsonplaceholder.typicode.com"}})
        #catalog['endpoints'].update({"reqres": {"label": "(Test) Requests - https://reqres.in/", "value": "https://reqres.in/"}})
					
        catalog['selected'] = "http://172.25.190.14:5000"
    
        return catalog