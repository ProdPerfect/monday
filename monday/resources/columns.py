from monday.query_joins import update_multiple_column_values_query, create_column

from monday.resources.base import BaseResource


class ColumnsResource(BaseResource):
    def create_column(self, board_id, column_title, column_type=None, defaults=None):
        query = create_column(board_id, column_title, column_type, defaults)
        return self.client.execute(query)

    def update_multiple_columns(self, item_id, board_id, column_values, create_labels_if_missing=False):
        query = update_multiple_column_values_query(item_id, board_id, column_values, create_labels_if_missing)
        return self.client.execute(query)
