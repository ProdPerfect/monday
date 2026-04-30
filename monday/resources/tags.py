from monday.query_joins import create_or_get_tag_query, get_tags_query
from monday.resources.base import BaseResource


class TagResource(BaseResource):
    def fetch_tags(self, tag_ids=None):
        query = get_tags_query(tag_ids)
        return self.client.execute(query)

    def create_or_get_tag(self, tag_name):
        query = create_or_get_tag_query(tag_name)
        return self.client.execute(query)
