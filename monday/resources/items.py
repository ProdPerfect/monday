from monday.exceptions import MondayError
from monday.resources.base import BaseResource
from monday.query_joins import mutate_query_join, get_query_join


def _validate_iterable(it, it_name):
    if not isinstance(it, (list, tuple)):
        raise MondayError(f'{it_name} must be a list or tuple')


class ItemResource(BaseResource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def create_item(self, board, group, item):
        query = mutate_query_join(board, group, item)
        return self.client.execute(query)

    def fetch_item(self, board, column, value):
        query = get_query_join(board, column, value)
        return self.client.execute(query)

