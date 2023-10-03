from monday.resources.base import BaseResource


class CustomResource(BaseResource):
    def __init__(self, token, headers):
        super().__init__(token, headers)

    def execute_custom_query(self, custom_query):
        return self.client.execute(custom_query)
