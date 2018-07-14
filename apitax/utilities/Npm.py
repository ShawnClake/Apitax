import subprocess
from multiprocessing import Process
import atexit

from apitax.logs.Log import Log


class Npm:
    processes = []

    def __init__(self, pathToNode=''):
        atexit.register(npmCleanup)
        self.path = pathToNode
        self.log = Log()

    def install(self):
        prefix = ''
        if (self.path != ''):
            prefix = '--prefix ' + self.path + ' '
        subprocess.check_call('npm ' + prefix + 'install', shell=True)

    def build(self):
        prefix = ''
        if (self.path != ''):
            prefix = '--prefix ' + self.path + ' '
        subprocess.check_call('npm ' + prefix + 'run build', shell=True)

    def test(self):
        prefix = ''
        if (self.path != ''):
            prefix = '--prefix ' + self.path + ' '
        subprocess.check_call('npm ' + prefix + 'run test', shell=True)

    def buildWatch(self, newProcess=False):
        if (newProcess):
            self.spawnWatcher
        else:
            prefix = ''
            if (self.path != ''):
                prefix = '--prefix ' + self.path + ' '
            subprocess.check_call('npm ' + prefix + 'run build-watch', shell=True)

    @property
    def spawnWatcher(self):
        if (len(Npm.processes) < 1):
            self.log.log("")
            self.log.log(">>> Spawning new process to watch for website changes and build them")
            self.log.log("")
            process = Process(target=self.buildWatch)
            process.start()
            Npm.processes.append(process)


def npmCleanup():
    log = Log()
    for p in Npm.processes:
        log.log("")
        log.log(">>> Terminating NPM watch processes")
        log.log("")
        p.terminate()
