import unittest
from unittest.mock import patch, MagicMock
import json
import urllib3

from monday.graphqlclient.client import GraphQLClient
from monday.exceptions import MondayQueryError


class GraphQlClientTestCase(unittest.TestCase):
    def setUp(self):
        self.token = "foo"
        self.url = "https://api.monday.com/v2"
        self.client = GraphQLClient(self.url)

    def test_client_endpoint(self):
        self.assertEqual(self.client.endpoint, self.url)

    def test_inject_token(self):
        client = self.client
        client.inject_token(token=self.token)
        self.assertEqual(client.token, self.token)

    def test_client_has_pool_manager(self):
        self.assertIsInstance(self.client._http, urllib3.PoolManager)

    @patch.object(urllib3.PoolManager, 'request')
    def test_execute_sends_post(self, mock_request):
        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.data = json.dumps({'data': {'boards': []}}).encode('utf-8')
        mock_request.return_value = mock_response

        self.client.inject_token(self.token)
        result = self.client.execute('{ boards { id } }')

        mock_request.assert_called_once()
        self.assertEqual(result, {'data': {'boards': []}})

    @patch.object(urllib3.PoolManager, 'request')
    def test_execute_raises_on_http_error(self, mock_request):
        mock_response = MagicMock()
        mock_response.status = 500
        mock_response.data = b'Internal Server Error'
        mock_request.return_value = mock_response

        with self.assertRaises(urllib3.exceptions.HTTPError):
            self.client.execute('{ boards { id } }')

    @patch.object(urllib3.PoolManager, 'request')
    def test_execute_raises_on_query_error(self, mock_request):
        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.data = json.dumps({'errors': [{'message': 'bad query'}]}).encode('utf-8')
        mock_request.return_value = mock_response

        with self.assertRaises(MondayQueryError):
            self.client.execute('{ bad }')
