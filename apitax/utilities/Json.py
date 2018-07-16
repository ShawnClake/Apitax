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


def read(file):
    with open(file) as jsonfile:
        # `json.loads` parses a string in json format
        return json.load(jsonfile)

