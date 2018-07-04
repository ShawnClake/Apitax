from apitax.drivers.Driver import Driver
from apitax.utilities.Files import getAllFiles
from pathlib import Path

class ApitaxTestsDriver(Driver):
    def isAuthenticated(self):
        return False
        
    def isTokenable(self):
        return False
        
    def getScriptsCatalog(self):
        files = getAllFiles(self.config.path + "/grammar/scripts/**/*.ah")
        returner = {"scripts": []}
        for file in files:
            returner['scripts'].append({"label": file.split('/')[-1].split('.')[0].title(),"relative-path":file,"path": str(Path(file).resolve())})
        # print(returner)
        return returner
        
    def getCatalog(self, auth):
        catalog = super().getCatalog(auth)
        catalog['endpoints'].update({"tests": {"label": "(Test) JSONPlaceHolder - https://jsonplaceholder.typicode.com", "value": "https://jsonplaceholder.typicode.com"}})
        catalog['endpoints'].update({"reqres": {"label": "(Test) Requests - https://reqres.in/", "value": "https://reqres.in/"}})
					
        catalog['selected'] = "https://reqres.in/"
    
        return catalog