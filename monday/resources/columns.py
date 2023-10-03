from monday.resources.base import BaseResource
from monday.query_joins import (
    get_columns_by_board_query,
    update_multiple_column_values_query,
)


class ColumnsResource(BaseResource):
    def __init__(self, token, headers):
        super().__init__(token, headers)

    def create_column(self, board_id):
        query = get_columns_by_board_query(board_id)
        return self.client.execute(query)

    def update_multiple_columns(self, item_id, board_id, column_values):
        query = update_multiple_column_values_query(item_id, board_id, column_values)
        return self.client.execute(query)
