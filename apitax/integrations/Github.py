from apitax.integrations.Git import Git

from github import Github as GithubDriver

class Github(Git):
    def __init__(self, token):
        self.git = GithubDriver(token)

    def getUser(self):
        return self.git.get_user()
            
    def getRepo(self, name):
        user = self.getUser()
        return user.get_repo(name)