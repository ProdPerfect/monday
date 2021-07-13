from monday.resources.base import BaseResource
from monday.graphql.gql_query_builder import GraphQLQueryBuilder


class CustomQueryResource(BaseResource, GraphQLQueryBuilder):
    def __init__(self, token):
        super(CustomQueryResource, self).__init__(token)

    def execute(self, query):
        return self.client.execute(query)
