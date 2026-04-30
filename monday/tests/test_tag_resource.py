from monday.tests.test_case_resource import BaseTestCase
from monday.query_joins import create_or_get_tag_query, get_tags_query


class TagTestCase(BaseTestCase):
    def setUp(self):
        super(TagTestCase, self).setUp()
        self.tag_name = "My tag"

    def test_get_tags_query(self):
        query = get_tags_query(self.tags)
        self.assertIn(str(self.tags), query)
        self.assertEqual(
            """query
        {
            tags (ids: [123, 456, 789]) {
                name,
                color,
                id
            }
        }""".replace(" ", ""),
            query.replace(" ", ""),
        )

    def test_create_or_get_tag_query(self):
        query = create_or_get_tag_query(self.tag_name)
        self.assertIn(self.tag_name, query)
        self.assertEqual(
            """mutation {
        create_or_get_tag(
            tag_name: "My tag"
        ) {
            id
        }
    }""",
            query,
        )
