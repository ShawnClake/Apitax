import connexion
import six

import flask

from apitax.ah.api.models.auth_response import AuthResponse  # noqa: E501
from apitax.ah.api.models.error_response import ErrorResponse  # noqa: E501
from apitax.ah.api.models.user_auth import UserAuth  # noqa: E501
from apitax.ah.api import util

from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)

def authenticate(user=None):  # noqa: E501
    """Authenticate

    Authenticate with the API # noqa: E501

    :param user: The user authentication object.
    :type user: dict | bytes

    :rtype: UserAuth
    """
    if connexion.request.is_json:
        user = UserAuth.from_dict(connexion.request.get_json())  # noqa: E501

    access_token = create_access_token(identity={'username': user.username, 'role': 'user'})
    refresh_token = create_refresh_token(identity={'username': user.username, 'role': 'user'})

    return AuthResponse(status=201, message='User ' + user.username + ' was created', access_token=access_token, refresh_token=refresh_token, auth=UserAuth())


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


@jwt_refresh_token_required
def refresh_token():  # noqa: E501
    """Refreshes login token using refresh token

    Refreshes login token using refresh token # noqa: E501


    :rtype: UserAuth
    """
    current_user = get_jwt_identity()
    access_token = create_access_token(identity=current_user)
    return AuthResponse(status=201, message='Refreshed Access Token', access_token=access_token, auth=UserAuth())
