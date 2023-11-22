import unittest
from monday.graphqlclient.client import GraphQLClient


class GraphQlClientTestCase(unittest.TestCase):
    def setUp(self):
        self.token = "foo"
        self.url = "https://api.monday.com/v2'"
        self.client = GraphQLClient(self.url)

    def test_client_endpoint(self):
        self.assertEqual(self.client.endpoint, self.url)

    def test_inject_token(self):
        client = self.client
        client.inject_token(token=self.token)
        self.assertEqual(client.token, self.token)
