import threading
import uuid


class GenericExecution(threading.Thread):
    def __init__(self, context, name, resolvedCommand, log=None, label=None):
        super().__init__()
        self.threadId = uuid.uuid4()
        self.name = name
        self.resolvedCommand = resolvedCommand
        self.callback = resolvedCommand['callback']
        self.result = {}
        self.log = log
        self.context = context
        self.label = label

    def run(self):
        if (self.log):
            self.log.log(">> Executing Async")
            self.log.log('')

        # Execute command
        self.result = self.context.executeCommand(self.resolvedCommand, '(In Thread: ' + str(self.threadId) + ')')

        if(self.label):
            self.context.data.storeVar(self.label, self.result['result'])
