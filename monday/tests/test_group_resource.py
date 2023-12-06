from monday.tests.test_case_resource import BaseTestCase
from monday.query_joins import get_groups_by_board_query, get_items_by_group_query, create_group_query, \
    duplicate_group_query, archive_group_query, delete_group_query


class GroupTestCase(BaseTestCase):
    def setUp(self):
        super(GroupTestCase, self).setUp()

    def test_add_group_query(self):
        query = create_group_query(board_id=self.board_id, group_name=self.group_name)
        self.assertIn(str(self.board_id), query)
        self.assertIn(str(self.group_name), query)

    def test_get_groups_by_board_query(self):
        query = get_groups_by_board_query(board_ids=[self.board_id])
        self.assertIn(str(self.board_id), query)

    def test_get_items_by_group_query(self):
        query = get_items_by_group_query(board_id=self.board_id, group_id=self.group_id)
        self.assertIn(str(self.board_id), query)
        self.assertIn(str(self.group_id), query)

    def test_get_items_by_group_query_with_limit_and_cursor(self):
        limit = 25
        cursor = 'MSw5NzI4MDA5MDAsaV9YcmxJb0p1VEdY...'
        query = get_items_by_group_query(board_id=self.board_id, group_id=self.group_id, limit=limit, cursor=cursor)
        items_page_line = f'items_page (limit: {limit}, cursor: "{cursor}")'
        self.assertIn(items_page_line, query)

    def test_duplicate_group_query(self):
        query = duplicate_group_query(board_id=self.board_id, group_id=self.group_id)
        self.assertIn(str(self.board_id), query)
        self.assertIn(str(self.group_id), query)

    def test_delete_group_query(self):
        query = delete_group_query(board_id=self.board_id, group_id=self.group_id)
        self.assertIn(str(self.board_id), query)
        self.assertIn(str(self.group_id), query)
        self.assertEqual('''
        mutation
        {
            delete_group(board_id: 12, group_id: "7")
            {
                id
                deleted
            }
        }'''.replace(" ", ""), query.replace(" ", ""))

    def test_archive_group_query(self):
        query = archive_group_query(board_id=self.board_id, group_id=self.group_id)
        self.assertIn(str(self.board_id), query)
        self.assertIn(str(self.group_id), query)

