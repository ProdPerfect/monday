from monday.tests.test_case_resource import BaseTestCase
from monday.query_joins import mutate_item_query, get_item_query, update_item_query, get_item_by_id_query, \
    update_multiple_column_values_query, mutate_subitem_query, add_file_to_column_query, delete_item_query, \
    archive_item_query, move_item_to_group_query
from monday.utils import monday_json_stringify


class ItemTestCase(BaseTestCase):
    def setUp(self):
        super(ItemTestCase, self).setUp()

    def test_mutate_item_query(self):
        query = mutate_item_query(board_id=self.board_id, group_id=self.group_id, item_name=self.item_name,
                                  column_values=self.column_values, create_labels_if_missing=False)
        self.assertIn(str(self.board_id), query)
        self.assertIn(str(self.group_id), query)
        self.assertIn(self.item_name, query)
        self.assertIn(monday_json_stringify(self.column_values), query)
        self.assertNotIn("create_labels_if_missing: true", query)

    def test_get_item_query(self):
        query = get_item_query(board_id=self.board_id,
                               column_id=self.column_id, value="foo")
        self.assertIn(str(self.board_id), query)
        self.assertIn(self.column_id, query)
        self.assertIn("foo", query)

    def test_get_item_query_with_limit_and_cursor(self):
        limit = 10
        cursor = "MSw0NTc5ODYzMTkyLFRWX2ljOW..."
        query = get_item_query(board_id=self.board_id, column_id=None, value="foo", limit=limit, cursor=cursor)
        items_page_line = f'items_page_by_column_values (board_id: {self.board_id}, limit: {limit}, cursor: "{cursor}")'
        self.assertIn(items_page_line, query)
        self.assertNotIn(self.column_id, query)
        self.assertNotIn("foo", query)

    def test_update_item_query(self):
        query = update_item_query(
            board_id=self.board_id, item_id=self.item_id, column_id=self.column_id, value="foo")
        self.assertIn(str(self.board_id), query)
        self.assertIn(str(self.item_id), query)
        self.assertIn(self.column_id, query)
        self.assertIn("foo", query)

    def get_item_by_id_query(self):
        query = get_item_by_id_query(ids=self.item_id)
        self.assertIn(str(self.item_id), query)

    def test_update_multiple_column_values(self):
        query = update_multiple_column_values_query(board_id=self.board_id, item_id=self.item_id,
                                                    column_values=self.column_values, create_labels_if_missing=False)
        self.assertIn(str(self.board_id), query)
        self.assertIn(str(self.item_id), query)
        self.assertIn(monday_json_stringify(self.column_values), query)
        self.assertNotIn("create_labels_if_missing: true", query)

    def test_mutate_subitem_query(self):
        query = mutate_subitem_query(parent_item_id=self.item_id, subitem_name=self.subitem_name, column_values=None,
                                     create_labels_if_missing=False)
        self.assertIn(str(self.item_id), query)
        self.assertIn(self.subitem_name, query)
        self.assertNotIn("create_labels_if_missing: true", query)

    def test_add_file_to_column_query(self):
        query = add_file_to_column_query(
            item_id=self.item_id, column_id=self.column_id)
        self.assertIn(str(self.item_id), query)
        self.assertIn(str(self.column_id), query)

    def test_delete_item_by_id(self):
        query = delete_item_query(item_id=self.item_id)
        self.assertIn(str(self.item_id), query)
        self.assertEqual('''
        mutation
        {
            delete_item (item_id: 24)
            {
                id
            }
        }'''.replace(" ", ""), query.replace(" ", ""))
        
    def test_archive_item_by_id(self):
        query = archive_item_query(item_id=self.item_id)
        self.assertIn(str(self.item_id), query)
        self.assertEqual('''
        mutation
        {
            archive_item (item_id: 24)
            {
                id
            }
        }'''.replace(" ", ""), query.replace(" ", ""))

    def test_move_item_to_group_query(self):
        query = move_item_to_group_query(item_id=self.item_id, group_id=self.group_id)
        self.assertIn(str(self.item_id), query)
        self.assertIn(str(self.group_id), query)
