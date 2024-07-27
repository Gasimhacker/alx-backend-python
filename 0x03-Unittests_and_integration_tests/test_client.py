#!/usr/bin/env python3
"""Execute a test multiple times with parameterized"""
import unittest
import requests
from unittest.mock import patch, Mock
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """Test the GithubOrgClient.org method"""

    @parameterized.expand([
        ("google", {'a': 1}),
        ("abc", {'a': 1}),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, expected, mock_method):
        """test that org method returns the expected result"""
        mock_method.return_value = {'a': 1}
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected)
        url = f"https://api.github.com/orgs/{org_name}"
        mock_method.assert_called_once_with(url)


if __name__ == '__main__':
    unittest.main()
