import unittest
import api_endpoints as api

class TestingAPI(unittest.TestCase):

    def test_beer(self):
        result = api.search("", "beer")
