#!/usr/bin/env python3
"""
4. Parameterize and patch as decorators
5. Mocking a property
6. More patching
7. Parameterize
8. Integration test: fixtures
9. Integration tests
"""
import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient
from parameterized import parameterized_class


class TestGithubOrgClient(unittest.TestCase):
    """
    A class to test github org client
    """

    @parameterized.expand(
        [
            ("google"),
            ("abc"),
        ]
    )
    @patch("client.get_json", return_value={"payload": True})
    def test_org(self, org_name: str, mock_get_json: Mock) -> None:
        """
        Test for org
        """
        json_data = {'login': org_name, 'id': 12345}
        mock_get_json.return_value = json_data
        client = GithubOrgClient(org_name)
        response = client.org
        url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(url)
        self.assertEqual(response, json_data)
