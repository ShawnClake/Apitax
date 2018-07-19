#!/usr/bin/env python

from apitax.ah.State import State
from apitax.ah.Setup import Setup

# Put Driver imports here

# End Driver imports

State.paths['root'] = '/app'
State.paths['config'] = '/app/config.txt'
State.paths['node'] = '/app/apitax/ah/api/dashboard'

# Set drivers

# End set drivers


# Put your custom logic here

# End custom logic


# These should probably be the last lines of your file
# Setup must run before importing the 'app' object from the API Server
setup = Setup()
from apitax.ah.api.Server import *
# Uncomment to debug without uwsgi or nginx
#app.run(port=5082, host='0.0.0.0')