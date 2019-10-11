
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
        }''' % (board, column, value)

    return query
