"""
monday.client
~~~~~~~~~~~~~~~~~~

:copyright: (c) 2019 by Christina D'Astolfo.
:license: Apache2, see LICENSE for more details.
"""

from .__version__ import __version__
from .resources import CustomResource, ItemResource, ColumnsResource, UpdateResource, TagResource, BoardResource, \
    UserResource, GroupResource, ComplexityResource, WorkspaceResource, NotificationResource, MeResource

_DEFAULT_HEADERS = {}


class MondayClient:
    def __init__(self, api_key, headers=None):
        """
        :param api_key: API key for the new :class:`BaseResource` object.
        :param headers: (optional) headers for the new :class:`BaseResource` object.
        """

        if not headers:
            headers = _DEFAULT_HEADERS.copy()

        self.custom = CustomResource(api_key=api_key, headers=headers)
        self.items = ItemResource(api_key=api_key, headers=headers)
        self.columns = ColumnsResource(api_key=api_key, headers=headers)
        self.updates = UpdateResource(api_key=api_key, headers=headers)
        self.tags = TagResource(api_key=api_key, headers=headers)
        self.boards = BoardResource(api_key=api_key, headers=headers)
        self.users = UserResource(api_key=api_key, headers=headers)
        self.groups = GroupResource(api_key=api_key, headers=headers)
        self.complexity = ComplexityResource(api_key=api_key, headers=headers)
        self.workspaces = WorkspaceResource(api_key=api_key, headers=headers)
        self.notifications = NotificationResource(api_key=api_key, headers=headers)
        self.me = MeResource(api_key=api_key, headers=headers)

    def __str__(self):
        return f'MondayClient {__version__}'

    def __repr__(self):
        return f'MondayClient {__version__}'
