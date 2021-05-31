from monday.tests.test_case_resource import BaseTestCase
from monday.query_joins import get_users_query


class UserTestCase(BaseTestCase):
    def setUp(self):
        super(UserTestCase, self).setUp()
        pass

    def test_get_users_query(self):
        query = get_users_query(ids=self.user_ids)
        self.assertIn(str(self.user_ids), query)
