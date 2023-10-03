from monday.resources.base import BaseResource
from monday.query_joins import get_me_query


class MeResource(BaseResource):
    def __init__(self, token, headers):
        super().__init__(token, headers)

    def get_details(self):
        query = get_me_query()
        return self.client.execute(query)
