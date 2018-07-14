# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from apitax.ah.api.models.command import Command  # noqa: E501
from apitax.ah.api.models.error import Error  # noqa: E501
from apitax.ah.api.models.response import Response  # noqa: E501
from apitax.ah.api.test import BaseTestCase


class TestUsersController(BaseTestCase):
    """UsersController integration test stubs"""

    def test_command(self):
        """Test case for command

        Execute a Command
        """
        command = Command()
        response = self.client.open(
            '/apitax/2/command',
            method='POST',
            data=json.dumps(command),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_display_dashboard(self):
        """Test case for display_dashboard

        Displays the user dashboard page
        """
        response = self.client.open(
            '/apitax/2/dashboard',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_endpoint_catalog(self):
        """Test case for endpoint_catalog

        Retrieve the endpoint catalog
        """
        response = self.client.open(
            '/apitax/2/system/endpoint/catalog',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_script(self):
        """Test case for get_script

        Retrieve the contents of a script
        """
        query_string = [('name', 'name_example')]
        response = self.client.open(
            '/apitax/2/system/script',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_script_catalog(self):
        """Test case for script_catalog

        Retrieve the script catalog
        """
        response = self.client.open(
            '/apitax/2/system/script/catalog',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
