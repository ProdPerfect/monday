"""
monday.client
~~~~~~~~~~~~~~~~~~

:copyright: (c) 2019 by Christina D'Astolfo.
:license: Apache2, see LICENSE for more details.
"""

from .__version__ import __version__
from .resources import ItemResource, UpdateResource, TagsResource


class MondayClient:
    def __init__(self, token):
        """
        :param token: API Token for the new :class:`BaseResource` object.
        """
        self.items = ItemResource(token=token)
        self.updates = UpdateResource(token=token)
        self.tags = TagsResource(token=token)

    def __str__(self):
        return f'MondayClient {__version__}'

    def __repr__(self):
        return f'MondayClient {__version__}'
