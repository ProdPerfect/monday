"""
monday.client
~~~~~~~~~~~~~~~~~~

:copyright: (c) 2019 by Christina D'Astolfo.
:license: Apache2, see LICENSE for more details.
"""

from .__version__ import __version__
from .resources import ItemResource, UpdateResource, TagResource, BoardResource, UserResource, GroupResource, ComplexityResource, WorkspaceResource, NotificationResource


class MondayClient:
    def __init__(self, token, proxies=None):
        """
        :param token: API Token for the new :class:`BaseResource` object.
        """
        self.items = ItemResource(token=token, proxies=proxies)
        self.updates = UpdateResource(token=token, proxies=proxies)
        self.tags = TagResource(token=token, proxies=proxies)
        self.boards = BoardResource(token=token, proxies=proxies)
        self.users = UserResource(token=token, proxies=proxies)
        self.groups = GroupResource(token=token, proxies=proxies)
        self.complexity = ComplexityResource(token=token, proxies=proxies)
        self.workspaces = WorkspaceResource(token=token, proxies=proxies)
        self.notifications = NotificationResource(token=token, proxies=proxies)

    def __str__(self):
        return f'MondayClient {__version__}'

    def __repr__(self):
        return f'MondayClient {__version__}'
