
def isBoolean(v):
    return v.lower() in ("true", "false")

def str2bool(v):
    if(v.lower() in ("true")):
        return True
    elif(v.lower() in ("false")):
        return False
    else:
        return None