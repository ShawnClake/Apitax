#!/usr/bin/env python

import connexion

from apitax.ah.api import encoder

app = connexion.App(__name__, specification_dir='./swagger/')
app.app.json_encoder = encoder.JSONEncoder
app.add_api('swagger.yaml', arguments={'title': 'Apitax'})

def startDevServer(ip, port):
    app.run(port=port, host=ip, debug=True)


