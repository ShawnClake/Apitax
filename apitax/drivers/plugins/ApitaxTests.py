from apitax.drivers.HttpPlug import HttpPlug


class ApitaxTestsDriver(HttpPlug):
    def isAuthenticated(self):
        return False
        
    def isTokenable(self):
        return False
        
    def getCatalog(self):
        catalog = super().getCatalog()
        catalog['endpoints'].update({"tests": {"label": "(Test) JSONPlaceHolder - https://jsonplaceholder.typicode.com", "value": "https://jsonplaceholder.typicode.com"}})
        catalog['endpoints'].update({"reqres": {"label": "(Test) Requests - https://reqres.in/", "value": "https://reqres.in/"}})
					
        catalog['selected'] = "https://reqres.in/"
    
        return catalog