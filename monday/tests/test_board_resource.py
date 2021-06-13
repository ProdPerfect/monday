from monday.tests.test_case_resource import BaseTestCase
from monday.query_joins import get_boards_query, get_boards_by_id_query, get_board_items_query, \
    get_columns_by_board_query


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
