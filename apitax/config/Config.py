import configparser
from apitax.utilities.Numbers import isNumber
from apitax.utilities.Booleans import isBoolean, str2bool

# Reads the config and allows us to retrieve values from it
class Config:
	
    configs = {}
    
    def __init__(self, path, sectionName):
        self.cp = configparser.RawConfigParser()
        self.cFilePath = path
        self.sectionName = sectionName
        self.cp.read(self.cFilePath)
        self.path = ''
        
	
    def read(path='config.txt', sectionName='Apitax'):
        if(path in Config.configs):
            return Config.configs[path]
        config = Config(path, sectionName)
        Config.configs[path] = config
        return config

    def get(self, param):
        prop: str = self.cp.get(self.sectionName, param)
        if(isBoolean(prop)):
            return str2bool(prop)
        elif(isNumber(prop)):
            return float(prop)
        return prop
        
    def getAsList(self, param):
        items = list(str(self.cp.get(self.sectionName, param)).split(","))
        return [x.strip(' ') for x in items]

    def has(self, param):
        return self.cp.has_option(self.sectionName, param)
        
    def serialize(self, serializable:list):
        returner = dict()
        for property in serializable:
            if(self.has(property)):
                returner.update({property: self.get(property)})
        return returner
