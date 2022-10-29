from monday.tests.test_case_resource import BaseTestCase
from monday.query_joins import duplicate_board_query, create_board_by_workspace_query, get_boards_query, get_boards_by_id_query, get_board_items_query, get_columns_by_board_query


class BoardTestCase(BaseTestCase):
    def setUp(self):
        super(BoardTestCase, self).setUp()

    def test_get_boards_query(self):
        query_a = get_boards_query(limit=1, page=2, ids=[888,999], board_kind=self.board_kind, state=self.board_state, order_by=self.boards_order_by)
        self.assertIn('1', query_a)
        self.assertIn('2', query_a)
        self.assertIn('[888, 999]', query_a)
        self.assertNotIn(str(self.board_kind), query_a)
        self.assertIn(str(self.board_kind.value), query_a)
        self.assertNotIn(str(self.board_state), query_a)
        self.assertIn(str(self.board_state.value), query_a)
        self.assertNotIn(str(self.boards_order_by), query_a)
        self.assertIn(str(self.boards_order_by.value), query_a)

        query_b = get_boards_query(board_kind=self.board_kind)
        self.assertNotIn(str(self.board_kind), query_b)
        self.assertIn(str(self.board_kind.value), query_b)

        query_c = get_boards_query(limit=1,state=self.board_state)
        self.assertIn('1', query_c)
        self.assertNotIn(str(self.board_state), query_c)
        self.assertIn(str(self.board_state.value), query_c)
        self.assertNotIn(str(self.board_kind), query_c)
        self.assertNotIn(str(self.boards_order_by), query_c)



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
        query_a = duplicate_board_query(board_id=self.board_id, duplicate_type=self.duplicate_type)
        self.assertIn(str(self.board_id), query_a)
        self.assertNotIn(str(self.duplicate_type), query_a)
        self.assertIn(str(self.duplicate_type.value), query_a)
        query_b = duplicate_board_query(board_id=self.board_id, duplicate_type=self.duplicate_type, board_name='testing_name', workspace_id=1, folder_id=2)
        self.assertIn(str(self.board_id), query_b)
        self.assertNotIn(str(self.duplicate_type), query_b)
        self.assertIn(str(self.duplicate_type.value), query_b)
        self.assertIn(str('testing_name'), query_b)
        self.assertIn(str(1), query_b)
        self.assertIn(str(2), query_b)

    def test_create_board_by_workspace_query(self):
        query_a = create_board_by_workspace_query(board_name=self.board_name, board_kind=self.board_kind, workspace_id=self.workspace_id)
        self.assertIn(str(self.board_name), query_a)
        self.assertNotIn(str(self.board_kind), query_a)
        self.assertIn(str(self.board_kind.value), query_a)
        self.assertIn(str(self.workspace_id), query_a)
        query_b = create_board_by_workspace_query(board_name=self.board_name, board_kind=self.board_kind)
        self.assertIn(str(self.board_name), query_b)
        self.assertNotIn(str(self.board_kind), query_b)
        self.assertIn(str(self.board_kind.value), query_b)
        self.assertNotIn(str(self.workspace_id), query_b)
