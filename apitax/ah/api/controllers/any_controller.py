import connexion
import six

import flask

from apitax.ah.api.models.error import Error  # noqa: E501
from apitax.ah.api.models.user_auth import UserAuth  # noqa: E501
from apitax.ah.api import util


def authenticate(user=None):  # noqa: E501
    """Authenticate

    Authenticate with the API # noqa: E501

    :param user: The user authentication object.
    :type user: dict | bytes

    :rtype: UserAuth
    """
    if connexion.request.is_json:
        user = UserAuth.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def display_login():  # noqa: E501
    """Displays the login page

    Displays the login page # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def get_asset(name):  # noqa: E501
    """Displays the user dashboard page

    Displays the user dashboard page # noqa: E501

    :param name: Get an asset such as a JavaScript file
    :type name: str

    :rtype: None
    """
    return flask.send_from_directory('dashboard/dist', name)
