"""
monday.client
~~~~~~~~~~~~~~~~~~

:copyright: (c) 2019 by Christina D'Astolfo.
:license: Apache2, see LICENSE for more details.
"""

from .__version__ import __version__
from .resources import CustomResource, ItemResource, ColumnsResource, UpdateResource, TagResource, BoardResource, \
    UserResource, GroupResource, ComplexityResource, WorkspaceResource, NotificationResource, MeResource

_DEFAULT_HEADERS = {
    "API-Version": "2023-10"
}

DEFAULT_TIMEOUT = 60

class MondayClient:
    def __init__(self, token, headers=None, timeout=DEFAULT_TIMEOUT):
        """
        :param token: API token for the new :class:`BaseResource` object.
        :param headers: (optional) headers for the new :class:`BaseResource` object.
        """

        if not headers:
            headers = _DEFAULT_HEADERS.copy()

        self.custom = CustomResource(token=token, headers=headers, timeout=timeout)
        self.items = ItemResource(token=token, headers=headers, timeout=timeout)
        self.columns = ColumnsResource(token=token, headers=headers, timeout=timeout)
        self.updates = UpdateResource(token=token, headers=headers, timeout=timeout)
        self.tags = TagResource(token=token, headers=headers, timeout=timeout)
        self.boards = BoardResource(token=token, headers=headers, timeout=timeout)
        self.users = UserResource(token=token, headers=headers, timeout=timeout)
        self.groups = GroupResource(token=token, headers=headers, timeout=timeout)
        self.complexity = ComplexityResource(token=token, headers=headers, timeout=timeout)
        self.workspaces = WorkspaceResource(token=token, headers=headers, timeout=timeout)
        self.notifications = NotificationResource(token=token, headers=headers, timeout=timeout)
        self.me = MeResource(token=token, headers=headers, timeout=timeout)

    def __str__(self):
        return f'MondayClient {__version__}'

    def __repr__(self):
        return f'MondayClient {__version__}'
