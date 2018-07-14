# Application import
from apitax.ah.commandtax.commands.Script import Script
from pathlib import Path


# Handles Openstack commands related to domains
class Tests(Script):
    def __init__(self, config, header, parameters, debug, sensitive):
        Script.__init__(self, config, header, parameters, debug, sensitive)

    def handle(self, command):
        command = str(
            Path('apitax/drivers/plugins/commandtax/apitaxtests/tests/' + '_'.join(command) + '.ah').resolve())
        super().handle([command])
