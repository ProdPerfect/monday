import json

import requests

from monday.exceptions import MondayQueryError


class GraphQLClient:
    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.token = None
        self.token_header_name = None
        self.headers = {}

    def execute(self, query, variables=None):
        return self._send(query, variables)

    def inject_token(self, token, token_header_name='Authorization'):
        self.token = token
        self.token_header_name = token_header_name

    def inject_headers(self, headers):
        self.headers = headers

    def _send(self, query, variables):
        payload = {'query': query}
        headers = self.headers.copy()
        files = None
        
        if self.token is not None:
            headers[self.token_header_name] = '{}'.format(self.token)

        if variables is None:
            headers.setdefault('Content-Type', 'application/json')

            payload = json.dumps({'query': query}).encode('utf-8')
        
        elif variables.get('file', None) is not None:
            headers.setdefault('content', 'multipart/form-data')
                
            files = [
                ('variables[file]', (variables['file'], open(variables['file'], 'rb')))
            ]

        try:
            response = requests.request("POST", self.endpoint, headers=headers, data=payload, files=files)
            response.raise_for_status()
            self._catch_error(response)
            return response.json()
        except (requests.HTTPError, MondayQueryError) as e:
            print(e)
            raise e

    def _catch_error(self, response):
        if 'errors' in response.json():
            raise MondayQueryError(response.json()['errors'][0]['message'])
