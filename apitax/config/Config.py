import ConfigParser


# Reads the config and allows us to retrieve values from it
class Config:
    def __init__(self):
        self.cp = ConfigParser.RawConfigParser()
        cFilePath = 'config.txt'
        self.cp.read(cFilePath)

    def get(self, param):
        return self.cp.get('Config', param)

    def has(self, param):
        return self.cp.has_option('Config', param)
