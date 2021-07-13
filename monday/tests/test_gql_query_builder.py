import unittest
from monday.graphql.gql_query_builder import GraphQLQueryBuilder


class GraphQLQueryBuilderTestCase(unittest.TestCase):
    def setUp(self):
        self.query_builder = GraphQLQueryBuilder()

    def test_query_fields(self):
        query_field_string = self.query_builder.query_fields(query_type='create_subitem', parent_item_id=15,
                                                             item_name='cheese').fields
        self.assertEqual(query_field_string, 'create_subitem(parent_item_id: 15, item_name: "cheese")')

    def test_return_values(self):
        return_value_string = self.query_builder.return_values(['permissions', 'group.id.title']).return_vals
        self.assertEqual(return_value_string, 'permissions, group{id,title}')

    def test_format_return_values(self):
        return_value = self.query_builder.format_return_value('permissions')
        nested_return_value = self.query_builder.format_return_value('group.id.title')
        self.assertEqual(return_value, 'permissions')
        self.assertEqual(nested_return_value, 'group{id,title}')

    def test_encode_values(self):
        should_be_quoted = self.query_builder.encode_values('group_id', 'topics')
        should_not_be_quoted = self.query_builder.encode_values('board_id', 1232425)
        should_be_escaped = self.query_builder.encode_values('column_values', {'status': 'Done'})
        self.assertEqual(should_be_quoted, '"topics"')
        self.assertEqual(should_not_be_quoted, 1232425)
        self.assertEqual(should_be_escaped, self.query_builder.monday_json_stringify({'status': 'Done'}))

    def test_make_query(self):
        self.query_builder.fields = 'complexity'
        self.query_builder.return_vals = 'after,reset_in_x_seconds'
        full_query = self.query_builder.make_query(operation='query')
        self.assertEqual(full_query, 'query{complexity{after,reset_in_x_seconds}}')

    def test_chained_query_build(self):
        query = self.query_builder.query_fields(query_type='boards', ids=1234567).query_fields(
            query_type='groups', ids="topics").return_values(['id', 'title', 'items.id.name']).make_query(
            operation='query')
        self.assertEqual(query, 'query{boards(ids: 1234567){groups(ids: topics) {id, title, items{id,name}}}}')