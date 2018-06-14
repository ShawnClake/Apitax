import json

def isJson(x):
    try:
        json.loads(x)
        return True
    except:
        return False

def isJsonable(x):
    try:
        json.dumps(x)
        return True
    except:
        return False
