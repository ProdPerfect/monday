import json

from monday.resources.base import BaseResource
from monday.query_joins import mutate_item_query, get_item_query, update_item_query, get_item_by_id_query


class ItemResource(BaseResource):
    def __init__(self, token):
        super().__init__(token)

    def create_item(self, board, group, item, column_values=None):
        query = mutate_item_query(board, group, item, column_values)
        return json.loads(self.client.execute(query))

    def fetch_items_by_column_value(self, board, column, value):
        query = get_item_query(board, column, value)
        return json.loads(self.client.execute(query))

    def fetch_items_by_id(self, ids):
        query = get_item_by_id_query(ids)
        return json.loads(self.client.execute(query))

    def change_item_value(self, board, item, column, value):
        query = update_item_query(board, item, column, value)
        return json.loads(self.client.execute(query))

