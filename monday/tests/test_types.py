import unittest
from unittest.mock import patch
from monday.resources.types import ColumnType


class TypesTestCase(unittest.TestCase):

    def setUp(self):
        self.defaults_mirror_missing = {}
        self.defaults_mirror_correct = {
            "relation_column": "some_id",
            "displayed_linked_columns": ["name"]
        }
        self.defaults_board_relation_missing = {}
        self.defaults_board_relation_correct = {
            "boardId": 123
        }

    @patch('monday.resources.types.warn')
    def test_is_defaults_have_recommended_keys_mirror_missing(self, mock_warn):
        ColumnType.MIRROR.is_defaults_have_recommended_keys(
            self.defaults_mirror_missing)
        mock_warn.assert_called_once()
        self.assertIn("missing recommended keys", mock_warn.call_args[0][0])

    @patch('monday.resources.types.warn')
    def test_is_defaults_have_recommended_keys_mirror_correct(self, mock_warn):
        ColumnType.MIRROR.is_defaults_have_recommended_keys(
            self.defaults_mirror_correct)
        mock_warn.assert_not_called()

    @patch('monday.resources.types.warn')
    def test_is_defaults_have_recommended_keys_board_relation_missing(
            self, mock_warn):
        ColumnType.BOARD_RELATION.is_defaults_have_recommended_keys(
            self.defaults_board_relation_missing)
        mock_warn.assert_called_once()
        self.assertIn("missing recommended keys", mock_warn.call_args[0][0])

    @patch('monday.resources.types.warn')
    def test_is_defaults_have_recommended_keys_board_relation_correct(
            self, mock_warn):
        ColumnType.BOARD_RELATION.is_defaults_have_recommended_keys(
            self.defaults_board_relation_correct)
        mock_warn.assert_not_called()

    @patch('monday.resources.types.warn')
    def test_is_defaults_have_recommended_keys_other_type(self, mock_warn):
        ColumnType.TEXT.is_defaults_have_recommended_keys({})
        mock_warn.assert_not_called()
