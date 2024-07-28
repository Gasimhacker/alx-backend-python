#!/usr/bin/env python3
"""Execute a test multiple times with parameterized"""
import unittest
from unittest.mock import Mock, patch, PropertyMock
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
        result = client.org
        mock_method.assert_called_once_with(url)
        self.assertEqual(result, expected)

    def test_public_repos_url(self) -> None:
        """test that public_repos_url treats org method as a property"""
        expected = {"repos_url": "https://github.com/Mohamed/alx-backend"}
        with patch.object(GithubOrgClient, 'org',
                          new_callable=PropertyMock) as mock_property:
            mock_property.return_value = expected
            client = GithubOrgClient("google")
            self.assertEqual(client._public_repos_url, expected["repos_url"])
