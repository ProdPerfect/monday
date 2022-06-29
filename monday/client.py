"""
monday.client
~~~~~~~~~~~~~~~~~~

:copyright: (c) 2019 by Christina D'Astolfo.
:license: Apache2, see LICENSE for more details.
"""

from .__version__ import __version__
from .resources import (
    CustomResource,
    ItemResource,
    ColumnsResource,
    UpdateResource,
    TagResource,
    BoardResource,
    UserResource,
    GroupResource,
    ComplexityResource,
    WorkspaceResource,
    NotificationResource,
    MeResource,
)


class MondayClient:
    def __init__(self, token):
        """
        :param token: API Token for the new :class:`BaseResource` object.
        """
        self.custom = CustomResource(token=token)
        self.items = ItemResource(token=token)
        self.columns = ColumnsResource(token=token)
        self.updates = UpdateResource(token=token)
        self.tags = TagResource(token=token)
        self.boards = BoardResource(token=token)
        self.users = UserResource(token=token)
        self.groups = GroupResource(token=token)
        self.complexity = ComplexityResource(token=token)
        self.workspaces = WorkspaceResource(token=token)
        self.notifications = NotificationResource(token=token)
        self.me = MeResource(token=token)

    def __str__(self):
        return f'MondayClient {__version__}'

    def __repr__(self):
        return f'MondayClient {__version__}'
