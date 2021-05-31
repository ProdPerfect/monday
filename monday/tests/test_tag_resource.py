from monday.tests.test_case_resource import BaseTestCase
from monday.query_joins import get_tags_query


class TagTestCase(BaseTestCase):
    def setUp(self):
        super(TagTestCase, self).setUp()

    def test_get_tags_query(self):
        query = get_tags_query(self.tags)
        self.assertIn(str(self.tags), query)
