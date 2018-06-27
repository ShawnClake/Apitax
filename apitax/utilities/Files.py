import glob
import os
from pathlib import Path

def getAllFiles(path):
    return glob.glob(getPath(path), recursive=True)
    
def readFile(path):
    with open(getPath(path), 'r') as myfile:
        return myfile.read()#.replace('\n', '').replace('\r', '')
        
def renameFile(originalFile, newFile):
    if(getPath(path, asString=False).exists()):
        return False
    getPath(path, asString=False).rename(Path(newFile))
    return True
    
def saveFile(path, contents):
    with open(getPath(path), "w+") as text_file:
        print(contents, file=text_file)
    
def deleteFile(path):
    return getPath(path, asString=False).unlink()
    
def getPath(path, asString=True):
    pathStr = str(Path(path).resolve()).replace(os.sep, '/')
    if(asString):
        return pathStr
    else:
        return Path(pathStr)
    
def createDir(path):
    Path(path).mkdir(parents=True, exist_ok=True) 