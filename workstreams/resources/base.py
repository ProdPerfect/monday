import requests

from workstreams import __version__

_URLS = {
    'dev': 'https://api-dev.workstreams.ai/api',
    'prod': 'https://rest.workstreams.ai/api'
}


class BaseResource:
    def __init__(self, token, production=True):
        self._token = token
        self._headers = {
            'Authorization': f'Bearer {self._token}',
            'User-Agent': f'Workstreams Python {__version__}'
        }
        self._base_url = _URLS['prod'] if production else _URLS['dev']
        self._base_url_batch = f'{self._base_url}/batch'

    def _request(self, method, url, ws_user_id=None, data=None, params=None):
        headers = self._headers
        if ws_user_id:
            headers['ws-user-id'] = ws_user_id
        return requests.request(method=method, url=url, data=data,
                                params=params, headers=headers)
