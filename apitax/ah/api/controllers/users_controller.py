import json
import traceback

import connexion
import six

import flask

from apitax.ah.api.models.command import Command  # noqa: E501
from apitax.ah.api.models.error import Error  # noqa: E501
from apitax.ah.api.models.response import Response  # noqa: E501
from apitax.ah.api import util

from apitax.ah.State import State
from apitax.ah.LoadedDrivers import LoadedDrivers
from apitax.ah.Credentials import Credentials
from apitax.ah.Options import Options
from apitax.ah.Connector import Connector


def command(command=None):  # noqa: E501
    """Execute a Command

    Execute a command # noqa: E501

    :param command: The command object.
    :type command: dict | bytes

    :rtype: Response
    """
    if connexion.request.is_json:
        command = Command.from_dict(connexion.request.get_json())  # noqa: E501

    try:
        connector = None

        parameters = {}

        if (command.parameters):
            parameters = command.parameters

        credentials = Credentials()
        options = Options(debug=command.options['debug'], sensitive=command.options['sensitive'])

        # if ('token' in request.json):
        #    credentials.token = request.json['token']
        # else:
        #    credentials.username = request.json['user']
        #    credentials.password = request.json['pass']
        #    options.sensitive = True

        # if ('extra' in request.json):
        #    credentials.extra = request.json['extra']

        connector = Connector(options=options, credentials=credentials, command=command.command,
                              parameters=parameters)

        commandHandler = connector.execute()

        response = Response(status=commandHandler.getRequest().getResponseStatusCode(),
                            body=json.loads(commandHandler.getRequest().getResponseBody()))

        if (command.options['debug']):
            response.log = connector.logBuffer

        return response
    except:
        State.log.error(traceback.format_exc())
        if ('debug' in command.options and command.options['debug']):
            return Error(status=500,
                         message="Uncaught exception occured during processing. To get a larger stack trace, visit the logs.",
                         state=traceback.format_exc(3))
        else:
            return Error(status=500, message="")


def display_dashboard():  # noqa: E501
    """Displays the user dashboard page

    Displays the user dashboard page # noqa: E501


    :rtype: None
    """
    return flask.send_from_directory('dashboard/src/pages', 'dashboard.html')


def endpoint_catalog():  # noqa: E501
    """Retrieve the endpoint catalog

    Retrieve the endpoint catalog # noqa: E501


    :rtype: Response
    """
    driver = LoadedDrivers.getDefaultBaseDriver()
    auth = None
    # if(request.json):
    #    auth = request.json['token']
    return Response(status=200, body=driver.getCatalog(auth))


def get_script(name=None):  # noqa: E501
    """Retrieve the contents of a script

    Retrieve the contents of a script # noqa: E501

    :param name: The script name.
    :type name: str

    :rtype: Response
    """

    driver = LoadedDrivers.getDefaultBaseDriver()
    return Response(status=200, body=driver.readScript(name))


def script_catalog():  # noqa: E501
    """Retrieve the script catalog

    Retrieve the script catalog # noqa: E501


    :rtype: Response
    """
    driver = LoadedDrivers.getDefaultBaseDriver()
    return Response(status=200, body=driver.getScriptsCatalog())
