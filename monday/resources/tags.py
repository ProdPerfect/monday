from monday.resources.base import BaseResource
from monday.query_joins import get_tags_query


class TagResource(BaseResource):
    def __init__(self, token):
        super().__init__(token)

    def fetch_tags(self, tag_ids=None):
        query = get_tags_query(tag_ids)
        return self.client.execute(query)

