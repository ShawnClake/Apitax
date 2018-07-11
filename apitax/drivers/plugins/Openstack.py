from apitax.drivers.Driver import Driver
from apitax.utilities.Files import getAllFiles
from apitax.ah.Options import Options
from pathlib import Path
from apitax.ah.Credentials import Credentials

class OpenstackDriver(Driver):
	
    def getToken(self, response):
        return response.getResponseHeaders().get('X-Subject-Token')

    def getTokenAuthHeader(self, credentials):
        return {'X-Auth-Token': credentials.token}
    
    def getPasswordAuthData(self, credentials):
        authObj = {'auth': {'identity': {'methods': ['password'], 'password': {'user': {'domain': {'id': 'default'}, 'password': credentials.password, 'name': credentials.username}}} }}
        if("project_id" in credentials.extra):
            authObj['auth'].update({"scope": {"project": {"id": credentials.extra['project_id']}}})
        return authObj
    
    def isCredentialsPosted(self):
       	return True  	

    def isConfigurable(self):
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

        connector = Connector(credentials=Credentials(token=auth.token), command="custom --get --driver OpenstackDriver --url " + self.getCatalogEndpoint(),
                         options=Options(debug=False,sensitive=True,driver='OpenstackDriver'), parameters=None)
        
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