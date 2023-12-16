from monday.query_joins import duplicate_board_query, create_board_by_workspace_query, get_boards_query, \
    get_boards_by_id_query, get_board_items_query, get_columns_by_board_query
from monday.resources.types import ItemsQueryRuleOperator
from monday.tests.test_case_resource import BaseTestCase


class BoardTestCase(BaseTestCase):
    def setUp(self):
        super(BoardTestCase, self).setUp()

    def test_get_boards_query(self):
        query_a = get_boards_query(limit=1, page=2, ids=[888, 999], board_kind=self.board_kind, state=self.board_state,
                                   order_by=self.boards_order_by)
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

        query_c = get_boards_query(limit=1, state=self.board_state)
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
        items_line = 'items'
        self.assertIn(items_line, query)

    def test_get_board_items_query_with_limit_and_cursor(self):
        limit = 100
        cursor = 'MSw0NTc5ODYzMTkyLFRWX2ljOWt2MVpnT...'
        query = get_board_items_query(board_id=self.board_id, limit=limit, cursor=cursor)
        items_page_line = f'items_page (limit: {limit}, cursor: "{cursor}")'
        self.assertIn(items_page_line, query)

    def test_get_board_items_query_with_query_params(self):
        query_params = {
            'rules': {
                'column_id': 'timeline',
                'compare_value': ['2023-06-30', '2023-07-01'],
                'compare_attribute': 'START_DATE',
                'operator': ItemsQueryRuleOperator.BETWEEN
            }}
        query = get_board_items_query(board_id=self.board_id, query_params=query_params)
        items_page_line = ('items_page (query_params: {rules: {'
                           'column_id: "timeline", '
                           'compare_value: ["2023-06-30", "2023-07-01"], '
                           'compare_attribute: "START_DATE", '
                           'operator: between}')
        self.assertIn(items_page_line, query)

    def test_get_columns_by_board_query(self):
        query = get_columns_by_board_query(board_ids=self.board_id)
        self.assertIn(str(self.board_id), query)

    def test_create_board_by_workspace_query(self):
        query_a = create_board_by_workspace_query(board_name=self.board_name, board_kind=self.board_kind,
                                                  workspace_id=self.workspace_id)
        self.assertIn(str(self.board_name), query_a)
        self.assertNotIn(str(self.board_kind), query_a)
        self.assertIn(str(self.board_kind.value), query_a)
        self.assertIn(str(self.workspace_id), query_a)
        query_b = create_board_by_workspace_query(board_name=self.board_name, board_kind=self.board_kind)
        self.assertIn(str(self.board_name), query_b)
        self.assertNotIn(str(self.board_kind), query_b)
        self.assertIn(str(self.board_kind.value), query_b)
        self.assertNotIn(str(self.workspace_id), query_b)

    def test_duplicate_board_query(self):
        query = duplicate_board_query(board_id=self.board_id, duplicate_type=self.duplicate_type)
        self.assertIn(str(self.board_id), query)
        self.assertNotIn(str(self.duplicate_type), query)
        self.assertIn(str(self.duplicate_type.value), query)
