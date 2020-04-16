import json
from monday.utils import python_json_stringify


# ITEM RESOURCE QUERIES
def mutate_item_query(board, group, item, column_values):
    if column_values is None:
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


def get_item_query(board, column, value):
    query = '''query
        {
            items_by_column_values(
                board_id: %s,
                column_id: %s,
                column_value: "%s"
            ) {
                id
                name
                updates {
                    id
                    body
                }
                group {
                    id
                    title
                }
                column_values {
                    id
                    text
                    value
                }
            }
        }''' % (board, column, value)

    return query


def get_item_by_id_query(ids):
    query = '''query
        {
            items (ids: %s) {
                name,
                column_values {
                    id,
                    text,
                    value
                }
            }
        }''' % ids

    return query


def update_item_query(board, item, column, value):
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


# UPDATE RESOURCE QUERIES
def create_update_query(item_id, update_value):
    query = '''mutation
        {
            create_update(
                item_id: %s,
                body: %s
            ) {
                id
            }
        }''' % (item_id, json.dumps(update_value))

    return query


def get_update_query(limit, page):
    query = '''query
        {
            updates (
                limit: %s,
                page: %s
            ) {
                id,
                body
            }
        }''' % (limit, page if page else 1)

    return query


# TAG RESOURCE QUERIES
def get_tags_query(tags):
    if tags is None:
        tags = []

    query = '''query
        {
            tags (ids: %s) {
                name,
                color,
                id
            }
        }''' % tags

    return query
