from monday.graphqlclient.client import GraphQLClient

_URLS = {
    'prod': 'https://api.monday.com/v2',
    'file': 'https://api.monday.com/v2/file'
}


class BaseResource:
    def __init__(self, token, headers):
        self._token = token
        self.client = GraphQLClient(_URLS['prod'])
        self.file_upload_client = GraphQLClient(_URLS['file'])
        self.client.inject_token(token)
        self.client.inject_headers(headers)
        self.file_upload_client.inject_token(token)

    def _query(self, query):
        result = self.client.execute(query)

        if result:
            return result

    def __str__(self):
        return self.__class__.__name__

    def __repr__(self):
        return self.__class__.__name__
