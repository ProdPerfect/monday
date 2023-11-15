from monday.tests.test_case_resource import BaseTestCase
from monday.query_joins import create_update_query, get_update_query, get_updates_for_item_query


class UpdateTestCase(BaseTestCase):
    def setUp(self):
        super(UpdateTestCase, self).setUp()

    def test_create_update_query(self):
        query = create_update_query(item_id=self.item_id, update_value=self.update_value)
        self.assertIn(str(self.item_id), query)
        self.assertIn(self.update_value, query)

    def test_get_update_query_without_page(self):
        query = get_update_query(limit=25, page=None)
        self.assertIn("25", query)
        self.assertIn("1", query)

    def test_get_update_query_with_page(self):
        query = get_update_query(limit=25, page=5)
        self.assertIn("25", query)
        self.assertIn("5", query)

    def test_get_updates_for_item_query(self):
        query = get_updates_for_item_query(item=self.item_id, limit=25)
        self.assertIn(str(self.item_id), query)
        self.assertIn("25", query)
        self.assertEqual('''query{ 
            items (ids: 24) {
                updates (limit: 25) {
                    id,
                    body,
                    created_at,
                    updated_at,
                    creator {
                      id,
                      name,
                      email
                    },
                    assets {
                      id,
                      name,
                      url,
                      file_extension,
                      file_size                  
                    },
                    replies {
                      id,
                      body,
                      creator{
                        id,
                        name,
                        email
                      },
                      created_at,
                      updated_at
                    }
                }
            }
        }'''.replace(" ", ""), query.replace(" ", ""))
