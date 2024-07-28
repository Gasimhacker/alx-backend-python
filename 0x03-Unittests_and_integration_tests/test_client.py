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

    @patch(
            'client.get_json',
            return_value=[{"name": 'simple_shell'}, {"name": 'sorting'}]
    )
    def test_public_repos(self, get_json_mock: Mock) -> None:
        """test that public_repos_url treats org method as a property"""
        repos_url = {"repos_url": "https://github.com/Mohamed/repos"}
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock,
                          return_value=repos_url) as public_repos_url_mock:
            client = GithubOrgClient("google")
            expected = ['simple_shell', 'sorting']
            self.assertEqual(client.public_repos(), expected)
            get_json_mock.assert_called_once()
            public_repos_url_mock.assert_called_once()
