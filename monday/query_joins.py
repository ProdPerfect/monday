import json

def mutate_query_join(board, group, item):
    query = '''mutation 
    {
        create_item (
            board_id: %s,
            group_id: %s,
            item_name: %s,
            column_values: json.dumps("status0": {"index": 4})
        ) {
            id
        }
    }''' % (board, group, item)

    return json.dumps(query)

def get_query_join(board, column, value):
    query = '''query 
        {
            items_by_column_values(
                board_id: %s,
                column_id: %s,
                column_value: %s
            ) {
                id
                name
                status
            }
        }''' % (board, column, value)

    return json.dumps(query)
