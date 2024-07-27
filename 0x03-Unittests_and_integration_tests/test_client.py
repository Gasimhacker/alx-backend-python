#!/usr/bin/env python3
"""Execute a test multiple times with parameterized"""
import unittest
from unittest.mock import Mock, patch
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """Test the GithubOrgClient.org method"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json', return_value={"payload": True})
    def test_org(self, org_name: str, mock_method: Mock) -> None:
        """test that org method returns the expected result"""
        expected = {"payload": True}
        url = f"https://api.github.com/orgs/{org_name}"

        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected)
        mock_method.assert_called_once_with(url)
