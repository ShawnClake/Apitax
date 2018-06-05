import configparser


# Reads the config and allows us to retrieve values from it
class Config:
    def __init__(self):
        self.cp = configparser.RawConfigParser()
        cFilePath = 'config.txt'
        self.cp.read(cFilePath)

    def get(self, param):
        return self.cp.get('Config', param)

    def has(self, param):
        return self.cp.has_option('Config', param)
        
    def serialize(self, serializable:list):
        returner = dict()
        for property in serializable:
            if(self.has(property)):
                returner.update({property: self.get(property)})
        return returner
