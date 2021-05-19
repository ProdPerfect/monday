import requests
import json


class GraphQLClient:
    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.token = None
        self.headername = None

    def execute(self, query, variables=None):
        return self._send(query, variables)

    def inject_token(self, token, headername='Authorization'):
        self.token = token
        self.headername = headername

    def _send(self, query, variables):
        payload = {'query': query}
        headers = {}
        files = None

        if self.token is not None:
            headers[self.headername] = '{}'.format(self.token)

        if variables is None:
            headers['Content-Type'] = 'application/json'
            payload = json.dumps({'query': query}).encode('utf-8')
        elif variables.get('file', None) is not None:
            headers['content'] = 'multipart/form-data'
            files = [
                ('variables[file]', (variables['file'], open(variables['file'], 'rb')))
            ]

        try:
            response = requests.request("POST", self.endpoint, headers=headers, data=payload, files=files)
            response.raise_for_status()
            return response.json()
        except requests.HTTPError as e:
            print(e)
            raise e
