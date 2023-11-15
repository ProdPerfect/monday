from monday.query_joins import get_me_query
from monday.resources.base import BaseResource


class MeResource(BaseResource):
    def get_details(self):
        query = get_me_query()
        return self.client.execute(query)
