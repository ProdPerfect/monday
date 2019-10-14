from monday.resources.base import BaseResource
from monday.query_joins import mutate_query_join, get_query_join, update_query_join


class ItemResource(BaseResource):
    def __init__(self, token):
        super().__init__(token)

    def create_item(self, board, group, item, column_values=None):
        query = mutate_query_join(board, group, item, column_values)
        return self.client.execute(query)

    def fetch_items(self, board, column, value):
        query = get_query_join(board, column, value)
        return self.client.execute(query)

    def change_item_value(self, board, item, column, value):
        query = update_query_join(board, item, column, value)
        return self.client.execute(query)

