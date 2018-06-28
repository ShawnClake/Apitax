# Application imports
from apitax.drivers.DriverCommands import DriverCommands
#from apitax.drivers.plugins.commandtax.apitaxtests import *

# Openstack Command Driver for handling custom commands when the openstack driver is used
class ApitaxTestsCommands(DriverCommands):
    
  def getDriverName(self):
      return 'apitaxtests'
      

