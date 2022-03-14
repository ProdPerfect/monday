from monday.resources.base import BaseResource
from monday.query_joins import create_notification_query


class NotificationResource(BaseResource):
    def __init__(self, token):
        super().__init__(token)

    def create_notification(self, user_id, target_id, text, target_type):
        """
        Refer to here for more information -> https://api.developer.monday.com/docs/notification-queries
        """
        query = create_notification_query(user_id, target_id, text, target_type)
        return self.client.execute(query)
