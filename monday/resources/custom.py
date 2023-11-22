from monday.resources.base import BaseResource


class CustomResource(BaseResource):
    def execute_custom_query(self, custom_query):
        return self.client.execute(custom_query)
