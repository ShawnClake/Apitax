from apitax.integrations.Git import Git
from apitax.drivers.Driver import Driver
from apitax.utilities.Files import getAllFiles
from apitax.utilities.Files import getPath
from apitax.utilities.Files import createDir
from pathlib import Path

class DefaultGitDriver(Driver):
    def isAuthenticated(self):
        return False
        
    def isTokenable(self):
        return False
        
    def getScriptsCatalog(self):
        path = self.getScriptsPath()
        createDir(path)
        git = Git()
        git.clone(self.driverConfig.get('git-repo-clone-url'), path)
        #print(self.driverConfig.get('git-repo-clone-url'))
        files = getAllFiles(path + "/**/*.ah")
        returner = {"scripts": []}
        for file in files:
            returner['scripts'].append({"label": file.split('/')[-1].split('.')[0].title(),"relative-path":file,"path": str(Path(file).resolve())})
        # print(returner)
        return returner
