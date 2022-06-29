from monday.tests.test_case_resource import BaseTestCase
from monday.query_joins import duplicate_board_query, create_board_by_workspace_query, get_boards_query, get_boards_by_id_query, get_board_items_query, get_columns_by_board_query


class BoardTestCase(BaseTestCase):
    def setUp(self):
        super(BoardTestCase, self).setUp()

    def test_get_boards_query(self):
        query = get_boards_query(board_kind=self.board_kind)
        self.assertIn(self.board_kind, query)

    def test_get_boards_by_id_query(self):
        query = get_boards_by_id_query(board_ids=self.board_id)
        self.assertIn(str(self.board_id), query)

    def test_get_board_items_query(self):
        query = get_board_items_query(board_id=self.board_id)
        self.assertIn(str(self.board_id), query)

    def test_get_columns_by_board_query(self):
        query = get_columns_by_board_query(board_ids=self.board_id)
        self.assertIn(str(self.board_id), query)

    def test_duplicate_board_query(self):
        query = duplicate_board_query(board_id=self.board_id, duplicate_type=self.duplicate_type)
        self.assertIn(str(self.board_id), query)
        self.assertNotIn(str(self.duplicate_type), query)
        self.assertIn(str(self.duplicate_type.value), query)

    def test_create_board_by_workspace_query(self):
        query_a = create_board_by_workspace_query(board_name=self.board_name, board_kind=self.board_kind, workspace_id=self.workspace_id)
        self.assertIn(str(self.board_name), query_a)
        self.assertIn(str(self.board_kind), query_a)
        self.assertIn(str(self.workspace_id), query_a)
        query_b = create_board_by_workspace_query(board_name=self.board_name, board_kind=self.board_kind)
        self.assertIn(str(self.board_name), query_b)
        self.assertIn(str(self.board_kind), query_b)
        self.assertNotIn(str(self.workspace_id), query_b)
