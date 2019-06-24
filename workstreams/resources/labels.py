"""
workstreams.resources.labels

:copyright: (c) 2019 by Lemuel Boyce.
:license: Apache2, see LICENSE for more details.

Resource for interacting with the Workstreams Label API.
"""

from workstreams.resources.base import BaseResource
from workstreams.utils import url_join


class LabelResource(BaseResource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._base_url = '{base}/labels'.format(base=self._base_url)

    def create(self, team_id, data, ws_user_id=None):
        url = url_join(self._base_url, 'team', team_id)
        return self._request('POST', url, ws_user_id=ws_user_id, data=data)

    def update(self, label_id, data, ws_user_id=None):
        url = url_join(self._base_url, label_id)
        return self._request('PATCH', url, ws_user_id=ws_user_id, data=data)

    def delete(self, label_id, ws_user_id=None):
        url = url_join(self._base_url, label_id)
        return self._request('DELETE', url, ws_user_id=ws_user_id)

    def fetch(self, label_id, ws_user_id=None):
        url = url_join(self._base_url, label_id)
        return self._request('GET', url, ws_user_id=ws_user_id)

    def fetch_team_labels(self, team_id, ws_user_id=None):
        url = url_join(self._base_url, 'team', team_id)
        return self._request('GET', url, ws_user_id=ws_user_id)
