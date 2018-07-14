import git
from git import Repo


class BasicGit:

    def push(self):
        pass

    def pull(self, path):
        repo = git.Repo(path)
        o = repo.remotes.origin
        o.pull()

    def clone(self, url, path):
        if (self.isGitRepo(path)):
            self.pull(path)
        else:
            Repo.clone_from(url, path)

    def isGitRepo(self, path):
        try:
            _ = git.Repo(path).git_dir
            return True
        except git.exc.InvalidGitRepositoryError:
            return False

    def commit(self):
        pass

    def inPush(self):
        pass

    def getRepo(self, name):
        pass

    def getRepos(self):
        pass

    def getUser(self):
        pass
