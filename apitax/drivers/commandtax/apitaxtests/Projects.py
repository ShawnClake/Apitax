# Application import
from apitax.ah.commandtax.Request import Request

# Handles Openstack commands related to projects
class Projects(Request):
  def __init__(self, header, debug, sensitive):
    Request.__init__(self, '', header.get(), '', debug = debug, sensitive = sensitive)

  def handle(self, command):
    if(command[0] == 'list'):
      if(len(command) > 1 and command[1] == 'all'):
        self.getAll()
      else:
        self.getMy()

  def getAll(self):
      print('response: project list all \n')
    # self.setUrl('http://172.25.190.14:5000/v3/projects')
    # self.get()

  def getMy(self):
      print('response: project list \n')
    # self.setUrl('http://172.25.190.14:5000/v3/auth/projects')
    # self.get()