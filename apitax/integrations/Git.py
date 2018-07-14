import base64


class Git:
    def __init__(self, token):
        self.git = None
        self.repo = None
        self.user = None

    # This requires a full name: "ShawnClake/Apitax"
    def setRepo(self, name):
        pass

    def getRepos(self):
        pass

    def printRepos(self):
        pass

    def createOrUpdate(self, path, content, commitMessage="Updated via Apitax"):
        file = self.isFileExists(path)
        if (not file):
            return self.createFile(path, content, commitMessage)
        return self.updateFile(file, content, commitMessage)

    def createIfNotExists(self, path, content, commitMessage="Updated via Apitax"):
        if (not self.isFileExists(path)):
            return self.createFile(path, content, commitMessage)
        return False

    def renameFile(self, originalPath, newPath):
        content = self.getFileContent(path=originalPath)
        self.deleteFile(path=originalPath, commitMessage="Updated via Apitax for renaming")
        self.createFile(newPath, content, commitMessage="Updated via Apitax for renaming")
        return True

    def isFileExists(self, path):
        pass

    def createFile(self, path, content, commitMessage="Updated via Apitax"):
        pass

    def updateFile(self, originalFile, newContent, commitMessage="Updated via Apitax"):
        pass

    def deleteFile(self, path=None, file=None, commitMessage="Updated via Apitax"):
        pass

    def getFile(self, path):
        return self.isFileExists(path)

    def getFiles(self, path="", recursive=True):
        pass

    def getFilesHelper(self, file):
        pass

    def getFileContent(self, path=None, file=None):
        pass

    def getPath(self, path):
        if (path[0:1] == '/'):
            return path
        return "/" + path

    def isEncoded(self, file):
        return bool(file.encoding)

    def encode(self, message):
        return base64.b64encode(message.encode())

    def decode(self, message):
        return base64.b64decode(message).decode()  # The last decode turns \n's etc. into actual new lines
