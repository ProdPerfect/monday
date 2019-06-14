from workstreams.exceptions import WorkstreamError
from workstreams.resources.base import BaseResource
from workstreams.utils import url_join


def _validate_iterable(it, it_name):
    if not isinstance(it, (list, tuple)):
        raise WorkstreamError(f'{it_name} must be a list or tuple')


class TaskResource(BaseResource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._base_url = '{base}/tasks'.format(base=self._base_url)

    def create(self, team_id, channel_id, data, ws_user_id=None):
        url = url_join(self._base_url, 'team', team_id, 'channel', channel_id)
        return self._request('POST', url, data=data, ws_user_id=ws_user_id).json()

    def update(self, task_id, data, ws_user_id=None):
        url = url_join(self._base_url, task_id)
        return self._request('PATCH', url, data=data, ws_user_id=ws_user_id).json()

    def fetch(self, task_id, ws_user_id=None):
        url = url_join(self._base_url, task_id)
        return self._request('GET', url, ws_user_id=ws_user_id).json()

    def fetch_user_tasks(self, team_id, user_id, ws_user_id=None):
        url = url_join(self._base_url, 'team', team_id, 'user', user_id)
        return self._request('GET', url, ws_user_id=ws_user_id).json()

    def fetch_tasks_for_users(self, team_id, user_ids, ws_user_id=None):
        _validate_iterable(user_ids, 'user_ids')
        url = url_join(self._base_url, 'team', team_id, 'users', ','.join(user_ids))
        return self._request('GET', url, ws_user_id=ws_user_id).json()

    def fetch_tasks_for_channels(self, team_id, channel_ids, ws_user_id=None):
        _validate_iterable(channel_ids, 'channel_ids')
        url = url_join(self._base_url, 'team', team_id, 'channels', ','.join(channel_ids))
        return self._request('GET', url, ws_user_id=ws_user_id).json()

    def fetch_changed_tasks_for_channels(self, team_id, channel_ids, timestamp, ws_user_id=None):
        _validate_iterable(channel_ids, 'channel_ids')
        url = url_join(self._base_url, 'team', team_id, 'channels', ','.join(channel_ids), 'after', timestamp)
        return self._request('GET', url, ws_user_id=ws_user_id).json()

    def fetch_archived_tasks_for_channels(self, team_id, channel_ids, ws_user_id=None):
        _validate_iterable(channel_ids, 'channel_ids')
        url = url_join(self._base_url, 'team', team_id, 'channels', ','.join(channel_ids), 'archived')
        return self._request('GET', url, ws_user_id=ws_user_id).json()

    def archive_tasks(self, task_ids, ws_user_id=None):
        _validate_iterable(task_ids, 'task_ids')
        url = url_join(self._base_url_batch, 'tasks', 'archive')
        return self._request('PATCH', url, data={'taskIds': task_ids}, ws_user_id=ws_user_id).json()

    def restore_tasks(self, task_ids, ws_user_id=None):
        url = url_join(self._base_url_batch, 'tasks', 'restore')
        return self._request('PATCH', url, data={'taskIds': task_ids}, ws_user_id=ws_user_id).json()

    def __str__(self):
        return 'TaskResource'

    def __repr__(self):
        return 'TaskResource'
