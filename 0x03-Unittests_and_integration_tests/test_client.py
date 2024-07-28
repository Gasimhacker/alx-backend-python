#!/usr/bin/env python3
"""Execute a test multiple times with parameterized"""
import unittest
from unittest.mock import Mock, patch, PropertyMock
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD
from requests import HTTPError


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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected) -> None:
        """
        Test that GithubOrgClient.has_license returns the expected result
        """
        self.assertEqual(GithubOrgClient.has_license(repo, license_key),
                         expected)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
     }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Perform an integration test"""
    @classmethod
    def setUpClass(cls) -> None:
        """Set up the class fixure before running the tests"""
        route_payload = {
                "https://api.github.com/orgs/google": cls.org_payload,
                "https://api.github.com/orgs/google/repos": cls.repos_payload,
                }

        def get_paylod(url):
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = patch('requests.get', side_effect=get_paylod)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls) -> None:
        """Tear down the class fixure after running the tests"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """test that public_repos_url treats org method as a property"""
        self.assertEqual(GithubOrgClient("google").public_repos(),
                         self.expected_repos)

    def test_public_repos_with_license(self) -> None:
        """
        Test that GithubOrgClient.has_license returns the expected result
        """
        self.assertEqual(
                GithubOrgClient("google").public_repos(license="apache-2.0"),
                self.apache2_repos,
                )
