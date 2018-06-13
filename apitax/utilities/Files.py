import glob
import os
from pathlib import Path

def getAllFiles(path):
    dirList = glob.glob(path, recursive=True)
    # for d in dirList:
    #    print (d)
    return dirList
    
def readFile(path):
    with open(path, 'r') as myfile:
        return myfile.read()#.replace('\n', '').replace('\r', '')
        
def renameFile(originalFile, newFile):
    if(Path(newFile).exists()):
        return False
    Path(originalFile).rename(Path(newFile))
    return True
    # return os.rename(str(Path(originalFile).resolve()), str(Path(newFile).resolve()))
    
def saveFile(path, contents):
    with open(str(Path(path).resolve()), "w+") as text_file:
        print(contents, file=text_file)
    
def deleteFile(path):
    return Path(path).unlink()
    
def getPath(path):
    return str(Path(path).resolve())
    