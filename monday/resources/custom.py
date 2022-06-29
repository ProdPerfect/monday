from monday.resources.base import BaseResource


class CustomResource(BaseResource):
    def __init__(self, token):
        super().__init__(token)

    def execute_custom_query(self, custom_query):
        return self.client.execute(custom_query)
