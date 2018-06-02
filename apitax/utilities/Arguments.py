import sys


class SystemCommands:

    def __init__(self):
        self.args = sys.argv[1:]

    def isEmpty(self):
        if(len(self.args) < 1):
            return True
        return False

    def isArg(self, arg):
        if (arg in self.args):
            return True
        return False

    def getArg(self, arg, default=""):
        if (not self.isArg(arg)):
            if default != "":
                return default
            else:
                return False
        return self.args[self.args.index(arg) + 1]
