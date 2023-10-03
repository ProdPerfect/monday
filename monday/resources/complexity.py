from monday.resources.base import BaseResource
from monday.query_joins import get_complexity_query


class ComplexityResource(BaseResource):
    def __init__(self, token, headers):
        super().__init__(token, headers)

    def get_complexity(self):
        query = get_complexity_query()
        return self.client.execute(query)
