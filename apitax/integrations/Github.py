from apitax.integrations.Git import Git

from github import Github as GithubIntegration


class Github(Git):
    def __init__(self, token, repo=None):
        self.git = GithubIntegration(token)
        self.repo = None
        if (repo):
            self.setRepo(repo)
        self.user = self.git.get_user()

    # This requires a full name: "ShawnClake/Apitax"
    def setRepo(self, name):
        self.repo = self.git.get_repo(name)
        return self.repo

    def getRepos(self):
        return self.git.get_user().get_repos()

    def printRepos(self):
        for repo in self.getRepos():
            print(repo.name)

    def isFileExists(self, path):
        try:
            files = self.getFiles(path, recursive=False)
            if (len(files) > 1):
                return False
            if (len(files) < 1):
                return False
            if (files[0].type == 'dir'):
                return False
            return files[0]
        except:
            return False

    def createFile(self, path, content, commitMessage="Updated via Apitax"):
        path = self.getPath(path)
        return self.repo.create_file(path, commitMessage, content)

    def updateFile(self, originalFile, newContent, commitMessage="Updated via Apitax"):
        path = self.getPath(originalFile.path)
        return self.repo.update_file(path, commitMessage, newContent, originalFile.sha)

    def deleteFile(self, path=None, file=None, commitMessage="Updated via Apitax"):
        if (not file):
            file = self.isFileExists(path)
        if (not file):
            return False
        path = self.getPath(file.path)
        return self.repo.delete_file(path, commitMessage, file.sha)

    def getFile(self, path):
        return self.isFileExists(path)

    def getFiles(self, path="", recursive=True):
        path = self.getPath(path)
        foundFiles = self.repo.get_contents(path)
        if (recursive):
            files = []
            for file in foundFiles:
                files += self.getFilesHelper(file)
            return files
        else:
            if (isinstance(foundFiles, list)):
                return foundFiles
            return [foundFiles]

    def getFilesHelper(self, file):
        if (file.type == 'file'):
            return [file]
        files = []
        for nextFile in self.repo.get_contents(file.path):
            files += self.getFilesHelper(nextFile)
        return files

    def getFileContent(self, path=None, file=None):
        if (not file):
            file = self.isFileExists(path)
        if (not file):
            return False
        if (self.isEncoded(file)):
            return self.decode(file.content)
        return file.content
