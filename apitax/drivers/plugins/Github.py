from apitax.integrations.Github import Github
from apitax.drivers.Driver import Driver
from apitax.utilities.Files import getAllFiles
from apitax.utilities.Files import getPath
from apitax.utilities.Files import createDir
from pathlib import Path

class GithubDriver(Driver):
	
    def __init__(self):
        super().__init__()
        self.git = Github(self.driverConfig.get('personal-access-token'), self.driverConfig.get('repo'))
	
    def isAuthenticated(self):
        return False
        
    def isTokenable(self):
        return False
        
    def getScriptsCatalog(self):
        files = self.git.getFiles()
        returner = {"scripts": []}
        for file in files:
            path = file.path
            if(path[-3:] == '.ah'):
                returner['scripts'].append({"label": path.split('/')[-1].split('.')[0].title(),"relative-path":path,"path": self.git.getPath(path)})
        return returner
        
    def readScript(self, path):
        return self.git.getFileContent(path)
        
    def renameScript(self, pathOriginal, pathNew):
        return self.git.renameFile(pathOriginal, pathNew)
        
    # Save does update and create
    def saveScript(self, path, content):
        return self.git.createOrUpdate(path, content)
    
    def deleteScript(self, path):
        return self.git.deleteFile(path=path)
