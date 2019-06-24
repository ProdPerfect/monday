"""
workstreams.resources.goals

:copyright: (c) 2019 by Lemuel Boyce.
:license: Apache2, see LICENSE for more details.

Resource for interacting with the Workstreams Goals API.
"""

from workstreams.resources.base import BaseResource
from workstreams.utils import url_join


class GoalResource(BaseResource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._base_url = '{base}/team'.format(base=self._base_url)

    def create(self, team_id, data, ws_user_id=None):
        url = url_join(self._base_url, team_id, 'goals')
        return self._request('POST', url, data=data, ws_user_id=ws_user_id)

    def updated(self, team_id, goal_id, data, ws_user_id=None):
        url = url_join(self._base_url, team_id, 'goals', goal_id)
        return self._request('PATCH', url, data=data, ws_user_id=ws_user_id)

    def archive(self, team_id, goal_id, ws_user_id=None):
        url = url_join(self._base_url, team_id, 'goals', goal_id)
        return self._request('PATCH', url, data={'archived': True}, ws_user_id=ws_user_id)

    def fetch_all(self, team_id, ws_user_id=None):
        url = url_join(self._base_url, team_id, 'goals')
        return self._request('GET', url, ws_user_id=ws_user_id)
