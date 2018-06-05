# Application import
from apitax.ah.commandtax.Request import Request

# Handles Openstack commands related to domains
class Domains(Request):
  def __init__(self, header, debug, sensitive):
    Request.__init__(self, '', header.get(), '', debug = debug, sensitive = sensitive)

  def handle(self, command):
    if(command[0] == 'list'):
      if(len(command) > 1 and command[1] == 'all'):
        self.getAll()
      else:
        self.getMy()
    elif(command[0] == 'create'):
      self.create(command[1])

  def getAll(self):
      print('response: domain list all \n')
    # self.setUrl('http://172.25.190.14:5000/v3/projects')
    # self.setParamData({'is_domain': True})
    # self.get()

  def getMy(self):
      print('response: domain list \n')
    # self.setUrl('http://172.25.190.14:5000/v3/auth/domains')
    # self.get()

  def create(self, name, description = "", enabled = True):
      print('response: domain create \n')
    # self.setUrl('http://172.25.190.14:5000/v3/domains')
    # self.setPostData({'domain': { 'name': name, 'description': description, 'enabled':enabled}})
    # self.post()    

