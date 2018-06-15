# Application imports
from apitax.drivers.DriverCommands import DriverCommands
from apitax.drivers.plugins.commandtax.apitaxtests import *

# Openstack Command Driver for handling custom commands when the openstack driver is used
class ApitaxTestsCommands(DriverCommands):
    
  def handle(self, config, header, parameters, command, debug = False, sensitive = False):
    super().handle(config, header, parameters, command, debug, sensitive)
   # if(self.command[0] == 'project'):
   #   self.request = Projects(self.config, self.header, self.parameters, self.debug, self.sensitive)
   # elif(self.command[0] == 'domain'):
   #   self.request = Domains(self.config, self.header, self.parameters, self.debug, self.sensitive)
    
    if(self.command[0] == 'tests'):
      self.request = Tests(self.config, self.header, self.parameters, self.debug, self.sensitive)
    return self.request
