from apitax.integrations.Git import Git
from apitax.drivers.HttpPlug import HttpPlug
from apitax.utilities.Files import getAllFiles
from apitax.utilities.Files import getPath
from apitax.utilities.Files import createDir
from pathlib import Path

class DefaultGitDriver(HttpPlug):
    def isAuthenticated(self):
        return False
        
    def isTokenable(self):
        return False
        
    def getScriptsCatalog(self, config):
        path = getPath(config.path + '/drivers/plugins/scriptax/default-git/')
        createDir(path)
        git = Git()
        git.clone(config.get('git-repo-clone-url'), path)
        files = getAllFiles(path + "/**/*.ah")
        returner = {"scripts": []}
        for file in files:
            returner['scripts'].append({"label": file.split('/')[-1].split('.')[0].title(),"relative-path":file,"path": str(Path(file).resolve())})
        # print(returner)
        return returner
