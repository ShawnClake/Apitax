


def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
        
def round2str(number):
    return "{0:.2f}".format(number)