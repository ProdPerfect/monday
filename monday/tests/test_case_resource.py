import unittest


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.group_name = "my_group"
        self.item_name = "Nerd"
        self.item_id = 24
        self.board_name = "My_board"
        self.duplicate_type = "duplicate_board_with_pulses"
        self.board_id = 12
        self.board_kind = "public"
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
        self.keep_subscribers = False
    
