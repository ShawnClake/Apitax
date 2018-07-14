from apitax.integrations.Git import Git

import gitlab


class Gitlab(Git):
    def __init__(self, config):
        if (config.has('gitlab-access-token')):
            super().__init__(gitlab.Gitlab('https://142.164.8.254', private_token=config.get('gitlab-access-token')))

    def getRepos(self):
        projects = self.git.projects.list()
        for project in projects:
            print(project)
