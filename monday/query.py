# ideally we should know if something needs to be quoted...
# should be able to specify whether return args should be nested and what the nested properties should be
# column values should always been double encoded wherever encountered.


class GraphQLQueryBuilder:
    def __init__(self):
        self.quoted_args = ['group_id', 'item_name', 'column_value']

    def format_return_value(self, return_value):
        values = return_value.split('.')
        return "{column} {{ {values} }}".format(column=values.pop(0), values=",".join(values)) if len(values) > 1 \
            else values[0]

    def fields(self, **kwargs):
        self.query_fields = ", ".join(["{key}: {value}".format(key=key, value=value) for key, value in kwargs.items()])
        return self

    def return_values(self, return_values):
        self.return_values = ", ".join([self.format_return_value(value) for value in return_values])
        return self

    def query_type(self, operation, query_method):
        self.operation = operation
        self.query_type = query_method
        return self

    def make_query(self):
        self.query = "{operation}{{ {query_type}({query_fields}) {{ {return_vals} }} }} ".format(operation=self.operation,
                                                                                         query_type=self.query_type,
                                                                                         query_fields=self.query_fields,
                                                                                         return_vals=self.return_values)
        return self.query


if __name__ == '__main__':
    builder = GraphQLQueryBuilder()
    print(builder.query_type(operation='query', query_method='boards').fields(board_id=7, group_name='cheese'
                                    ).return_values(
        ['name', 'permissions', 'groups.id.title', 'columns.id.title.type.settings_str']).make_query())
    # print(builder.make_query('query', 'updates', {'page': 1, 'limit': 25}, ['id', 'body']))
    # print(builder.make_query('mutation', 'create_group', {'board_id': 7, 'group_name': "cheese"}, ['id']))
