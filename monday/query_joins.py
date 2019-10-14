from monday.utils import python_json_stringify


def mutate_query_join(board, group, item):
    query = '''mutation
    {
        create_item (
            board_id: %s,
            group_id: %s,
            item_name: "%s",
        ) {
            id
        }
    }''' % (board, group, item)

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
        }''' % (board, column, python_json_stringify(value))

    return query


def update_query_join(board, item, column, value):
    query = '''mutation
        {
            change_column_value(
                board_id: %s,
                item_id: %s,
                column_id: %s,
                value: "%s"
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