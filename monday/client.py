"""
monday.client
~~~~~~~~~~~~~~~~~~

:copyright: (c) 2019 by Christina D'Astolfo.
:license: Apache2, see LICENSE for more details.
"""

from .__version__ import __version__
from .resources import ItemResource, UpdateResource, TagResource, BoardResource, UserResource, GroupResource, ComplexityResource


class MondayClient:
    def __init__(self, token):
        """
        :param token: API Token for the new :class:`BaseResource` object.
        """
        self.items = ItemResource(token=token)
        self.updates = UpdateResource(token=token)
        self.tags = TagResource(token=token)
        self.boards = BoardResource(token=token)
        self.users = UserResource(token=token)
        self.groups = GroupResource(token=token)
        self.complexity = ComplexityResource(token=token)

    def __str__(self):
        return f'MondayClient {__version__}'

    def __repr__(self):
        return f'MondayClient {__version__}'
