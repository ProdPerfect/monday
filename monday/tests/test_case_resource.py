import unittest

from monday.resources.types import BoardKind, BoardState, BoardsOrderBy, DuplicateType


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.group_name = "my_group"
        self.item_name = "Nerd"
        self.item_id = 24
        self.board_name = "my_board"
        self.board_id = 12
        self.board_kind = BoardKind.PUBLIC
        self.board_state = BoardState.ACTIVE
        self.boards_order_by = BoardsOrderBy.USED_AT
        self.duplicate_type = DuplicateType.WITH_PULSES
        self.group_id = 7
        self.column_id = "file_column"
        self.user_ids = [1287123, 1230919]
        self.update_value = "This is an update."
        self.tags = [123, 456, 789]
        self.subitem_name = "A subitem"
        self.column_values = {"foo": "bar", "bar": 12}
        self.workspace_name = "my_group_workspace"
        self.workspace_kind = "open"
        self.workspace_id = "123456"
        self.workspace_user_kind = "subscriber"
        self.team_ids = [105939, 105940, 105941]
        self.notification_text = "This is an awesome notification."
        self.notification_target_type = "Project"
    
