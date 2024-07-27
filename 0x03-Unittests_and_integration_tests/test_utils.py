#!/usr/bin/env python3
"""Execute a test multiple times with parameterized"""
import unittest
import requests
from unittest.mock import patch, Mock
from utils import get_json, access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Test the access_nested_map method"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test get_json method"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, expected):
        mock = Mock()
        mock.json.return_value = expected
        with patch('requests.get', return_value=mock):
            self.assertEqual(get_json(test_url), expected)


if __name__ == '__main__':
    unittest.main()
