from monday.utils import python_json_stringify


def mutate_query_join(board, group, item, column_values):
    if column_values == None:
        column_values = {}

    query = '''mutation
    {
        create_item (
            board_id: %s,
            group_id: %s,
            item_name: "%s",
            column_values: %s
        ) {
            id
        }
    }''' % (board, group, item, python_json_stringify(column_values))

    return query


def get_query_join(board, column, value):
    query = '''query
        {
            items_by_column_values(
                board_id: %s,
                column_id: %s,
                column_value: "%s"
            ) {
                id
                name
                column_values {
                    id
                    text
                    value
                }
            }
        }''' % (board, column, value)

    return query


def update_query_join(board, item, column, value):
    query = '''mutation
        {
            change_column_value(
                board_id: %s,
                item_id: %s,
                column_id: %s,
                value: %s
            ) {
                id
                name
                column_values {
                    id
                    text
                    value
                }
            }
        }''' % (board, item, column, python_json_stringify(value))

    return query