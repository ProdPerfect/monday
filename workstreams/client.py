"""
workstreams.client
~~~~~~~~~~~~~~~~~~

:copyright: (c) 2019 by Lemuel Boyce.
:license: Apache2, see LICENSE for more details.
"""

from .__version__ import __version__
from .resources import TaskResource


class WorkstreamsClient:
    def __init__(self, token, production=True):
        """
        :param token: API Token for the new :class:`BaseResource` object.
        :param production: flag used to switch between production and
            development URLs in :class:`BaseResource` object.
        """
        self.tasks = TaskResource(token=token, production=production)

    def __str__(self):
        return f'WorkstreamsClient {__version__}'

    def __repr__(self):
        return f'WorkstreamsClient {__version__}'
