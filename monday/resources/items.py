from monday.resources.base import BaseResource
from monday.query_joins import mutate_item_query, get_item_query, update_item_query, get_item_by_id_query, \
    update_multiple_column_values_query, mutate_subitem_query, add_file_to_column_query, delete_item_query, \
    archive_item_query, move_item_to_group_query


class ItemResource(BaseResource):
    def __init__(self, token):
        super().__init__(token)

    def create_item(self, board_id, group_id, item_name, column_values=None,
                    create_labels_if_missing=False):
        query = mutate_item_query(board_id, group_id, item_name, column_values,
                                  create_labels_if_missing)
        return self.client.execute(query)

    def create_subitem(self, parent_item_id, subitem_name, column_values=None,
                       create_labels_if_missing=False):
        query = mutate_subitem_query(parent_item_id, subitem_name, column_values,
                                     create_labels_if_missing)
        return self.client.execute(query)

    def fetch_items_by_column_value(self, board_id, column_id, value):
        query = get_item_query(board_id, column_id, value)
        return self.client.execute(query)

    def fetch_items_by_id(self, ids):
        query = get_item_by_id_query(ids)
        return self.client.execute(query)

    def change_item_value(self, board_id, item_id, column_id, value):
        query = update_item_query(board_id, item_id, column_id, value)
        return self.client.execute(query)

    def change_multiple_column_values(self, board_id, item_id, column_values, create_labels_if_missing=False):
        query = update_multiple_column_values_query(
            board_id, item_id, column_values, create_labels_if_missing)
        return self.client.execute(query)

    def add_file_to_column(self, item_id, column_id, file):
        query = add_file_to_column_query(item_id, column_id)
        return self.file_upload_client.execute(query, variables={'file': file})

    def move_item_to_group(self, item_id, group_id):
        query = move_item_to_group_query(item_id, group_id)
        return self.client.execute(query)

    def archive_item_by_id(self, item_id):
        query = archive_item_query(item_id)
        return self.client.execute(query)
    
    def delete_item_by_id(self, item_id):
        query = delete_item_query(item_id)
        return self.client.execute(query)
