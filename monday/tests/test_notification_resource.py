from monday.tests.test_case_resource import BaseTestCase
from monday.query_joins import create_notification_query


class NotificationsTestCase(BaseTestCase):
    def setUp(self):
        super(NotificationsTestCase, self).setUp()

    def test_create_notification_query(self):
        query = create_notification_query(self.user_ids[0], self.item_id, self.notification_text, self.notification_target_type)
        self.assertIn(str(self.user_ids[0]), query)
        self.assertIn(str(self.item_id), query)
        self.assertIn(str(self.notification_text), query)
        self.assertIn(str(self.notification_target_type), query)
        