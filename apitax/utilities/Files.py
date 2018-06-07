import glob

def getAllFiles(path):
    dirList = glob.glob(path, recursive=True)
    # for d in dirList:
    #    print (d)
    return dirList
    
def readFile(path):
    with open(path, 'r') as myfile:
        return myfile.read()#.replace('\n', '').replace('\r', '')