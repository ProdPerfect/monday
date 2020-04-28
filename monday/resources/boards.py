import json

from monday.resources.base import BaseResource
from monday.query_joins import get_board_items_query


class BoardResource(BaseResource):
    def __init__(self, token):
        super().__init__(token)

    def fetch_items_by_board_id(self, board):
        query = get_board_items_query(board)
        return json.loads(self.client.execute(query))
