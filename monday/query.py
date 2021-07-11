# ideally we should know if something needs to be quoted...
# should be able to specify whether return args should be nested and what the nested properties should be
# column values should always been double encoded wherever encountered.


class Query:
    def __init__(self):
        self.query = {}
        self.args = ()
        self.arg_join_string = []
        self.quoted_args = ['group_id', 'item_name', 'column_value']

    def format_args(self, args):
        return ", ".join(["{key}: {value}".format(key=key, value=value) for key, value in args.items()])

    def format_return_values(self, return_values):
        return ", ".join([arg for arg in return_values])

    def make_query(self, query_type, resource_type, args, return_values):
        return "{query_type}{{ {resource_type}({args}){{ {kwargs} }}".format(query_type=query_type,
                                                                             resource_type=resource_type,
                                                                             args=self.format_args(
                                                                                 args),
                                                                             kwargs=self.format_return_values(
                                                                                 return_values))


'''query
    {
        boards (ids: %s) {
            id
            name
            permissions
            tags {
              id
              name
            }
            groups {
                id
                title
            }
            columns {
                id
                title
                type
                settings_str
            }
        }
    }'''

'''
    mutation
    {
        create_group(board_id: %s, group_name: "%s")
        {
            id
        }
    }'''

if __name__ == '__main__':
    print(Query().make_query('query', 'updates', {'page': 1, 'limit': 25}, ['id', 'body']))
    print(Query().make_query('mutation', 'create_group', {'board_id': 7, 'group_name': "cheese"}, ['id']))

