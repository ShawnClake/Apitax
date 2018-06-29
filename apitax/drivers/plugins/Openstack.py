from apitax.drivers.Driver import Driver
from apitax.utilities.Files import getAllFiles
from apitax.ah.Options import Options
from pathlib import Path

class OpenstackDriver(Driver):
	
    def getToken(self, response):
        return response.getResponseHeaders().get('X-Subject-Token')

    def getTokenAuthHeader(self, token):
        return {'X-Auth-Token': token}
    
    def getPasswordAuthData(self, username, password):
        return {'auth': {'identity': {'methods': ['password'], 'password': {'user': {'domain': {'id': 'default'}, 'password': password, 'name': username}}} }}
    
    def isCredentialsPosted(self):
       	return True  	
  	   
    def getScriptsCatalog(self):
        files = getAllFiles(self.config.path + "/grammar/scripts/**/*.ah")
        returner = {"scripts": []}
        for file in files:
            returner['scripts'].append({"label": file.split('/')[-1].split('.')[0].title(),"relative-path":file,"path": str(Path(file).resolve())})
        # print(returner)
        return returner
        
    def getCatalog(self, auth):
        from apitax.ah.Connector import Connector
        import json
        connector = Connector(token=auth.token, command="custom --get --url " + self.getCatalogEndpoint(),
                              options=Options(debug=False,sensitive=True), parameters=None)
        
        commandHandler = connector.execute()

        services = json.loads(commandHandler.getRequest().getResponseBody())
        
        catalog = {}
        catalog['endpoints'] = {}
        
        for service in services['catalog']:
            endpoints = service['endpoints']
            if(len(endpoints) > 0):
                for endpoint in endpoints:
                    if(endpoint['interface'] == 'public'):
                        name = service['name']
                        catalog['endpoints'].update({name: {"label": name, "value": endpoint['url']}})
                        
					
        catalog['selected'] = "http://172.25.190.14:5000"
    
        return catalog