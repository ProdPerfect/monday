from monday.resources.base import BaseResource
from monday.query_joins import create_update_query, get_update_query


class UpdateResource(BaseResource):
    def __init__(self, token):
        super().__init__(token)

    def create_update(self, item_id, update_value):
        query = create_update_query(item_id, update_value)
        return self.client.execute(query)

    def fetch_updates(self, limit, page=None):
        query = get_update_query(limit, page)
        return self.client.execute(query)

