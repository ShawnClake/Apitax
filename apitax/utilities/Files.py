import glob

def getAllFiles(path):
    dirList = glob.glob(path, recursive=True)
    # for d in dirList:
    #    print (d)
    return dirList