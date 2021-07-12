# ideally we should know if something needs to be quoted...
# should be able to specify whether return args should be nested and what the nested properties should be
# column values should always been double encoded wherever encountered.


class GraphQLQueryBuilder:
    def __init__(self):
        self.query_type = ''
        self.query_args = ()
        self.query_return_vals = []
        self.quoted_args = ['group_id', 'item_name', 'column_value']

    def format_return_value(self, return_value):
        values = return_value.split('.')
        if len(values) == 1:
            return values[0]
        else:
            return "{column} {{ {values} }}".format(column=values.pop(0), values=",".join(values))

    def fields(self, **kwargs):
        return ", ".join(["{key}: {value}".format(key=key, value=value) for key, value in kwargs.items()])

    def return_values(self, return_values):
        return ", ".join([self.format_return_value(value) for value in return_values])

    def query_type(self, query_type, category):
        return "{query_type} {{ {category} }}".format(query_type=query_type, category=category)

    def make_query(self, operation, query_type):
        return "{operation}{{ {query_type}({args}){{ {kwargs} }}".format(operation=operation, query_type=query_type)


if __name__ == '__main__':
    builder = GraphQLQueryBuilder()
    print(builder.return_values(return_values=['name', 'permissions', 'groups.id.title', 'columns.id.title.type.settings_str']))
    builder.fields(board_id=7, group_name='cheese')
    # print(builder.make_query(operation='query', query_type='boards').fields(board_id=7, group_name='cheese').return_values('name', 'permissions', 'groups.id.title', 'columns.id.title.type.settings_str'))
    # print(builder.make_query('query', 'updates', {'page': 1, 'limit': 25}, ['id', 'body']))
    # print(builder.make_query('mutation', 'create_group', {'board_id': 7, 'group_name': "cheese"}, ['id']))


