import json

from monday.utils import monday_json_stringify


# Eventually I will organize this file better but you know what today is not that day.

# ITEM RESOURCE QUERIES
def mutate_item_query(board_id, group_id, item_name, column_values,
                      create_labels_if_missing):
    # Monday does not allow passing through non-JSON null values here,
    # so if you choose not to specify column values, need to set column_values to empty object.
    column_values = column_values if column_values else {}

    query = '''mutation
    {
        create_item (
            board_id: %s,
            group_id: "%s",
            item_name: "%s",
            column_values: %s,
            create_labels_if_missing: %s
        ) {
            id
        }
    }''' % (board_id, group_id, item_name, monday_json_stringify(column_values),
            str(create_labels_if_missing).lower())

    return query


def mutate_subitem_query(parent_item_id, subitem_name, column_values,
                         create_labels_if_missing):
    column_values = column_values if column_values else {}

    return '''mutation
    {
        create_subitem (
            parent_item_id: %s,
            item_name: "%s",
            column_values: %s,
            create_labels_if_missing: %s
        ) {
            id,
            name,
            column_values {
                id,
                text
            },
            board {
                id,
                name
            }
        }
    }''' % (parent_item_id, subitem_name, monday_json_stringify(column_values),
            str(create_labels_if_missing).lower())


def get_item_query(board_id, column_id, value):
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
        }''' % (board_id, column_id, value)

    return query


def get_item_by_id_query(ids):
    query = '''query
        {
            items (ids: %s) {
                name,
                group {
                    id
                    title
                }
                column_values {
                    id,
                    text,
                    value
                }
            }
        }''' % ids

    return query


def update_item_query(board_id, item_id, column_id, value):
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
        }''' % (board_id, item_id, column_id, monday_json_stringify(value))

    return query


def delete_item_query(item_id):
    query = '''
    mutation
    {
        delete_item (item_id: %s)
        {
            id
        }
    }''' % (item_id)
    return query


def update_multiple_column_values_query(board_id, item_id, column_values):
    query = '''mutation
        {
            change_multiple_column_values (
                board_id: %s,
                item_id: %s,
                column_values: %s
            ) {
                id
                name
                column_values {
                  id
                  text
                }
            }
        }''' % (board_id, item_id, monday_json_stringify(column_values))

    return query


def add_file_to_column_query(item_id, column_id):
    query = '''mutation ($file: File!) {
        add_file_to_column (
            file: $file,
            item_id: %s,
            column_id: %s
        ) {
            id
        }
    }''' % (item_id, column_id)
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


def get_updates_for_item_query(board, item, limit):
    query = '''query 
    {boards (ids: %s) 
        {items (ids: %s) {
            updates (limit: %s) {
                id,
                body,
                created_at,
                updated_at,
                creator {
                  id,
                  name,
                  email
                },
                assets {
                  id,
                  name,
                  url,
                  file_extension,
                  file_size                  
                },
                replies {
                  id,
                  body,
                  creator{
                    id,
                    name,
                    email
                  },
                  created_at,
                  updated_at
                }
                }
            }
        }
    }''' % (board, item, limit)

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


# BOARD RESOURCE QUERIES
def get_board_items_query(board_id):
    query = '''query
    {
        boards(ids: %s) {
            name
            items {
                group {
                    id
                    title
                }
                id
                name
                column_values {
                  id
                  text
                  type
                  value
                }
            }
        }
    }''' % board_id

    return query


def get_boards_query(**kwargs):
    query = '''query
    {
        boards (%s) {
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
            }
        }
    }''' % ', '.join(["%s: %s" % (arg, kwargs.get(arg)) for arg in kwargs])
    return query


def get_boards_by_id_query(board_ids):
    return '''query
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
    }''' % board_ids


def get_columns_by_board_query(board_ids):
    return '''query
        {
            boards(ids: %s) {
                id
                name
                groups {
                    id
                    title
                }
                columns {
                    title
                    id
                    type
                    settings_str
                 }
            }
        }''' % board_ids


# USER RESOURCE QUERIES
def get_users_query(**kwargs):
    query = '''query
    {
        users (%s) {
            id
            name
            email
            enabled
            teams {
              id
              name
            }
        }
    }''' % ', '.join(["%s: %s" % (arg, kwargs.get(arg)) for arg in kwargs])
    return query


# GROUP RESOURCE QUERIES
def get_groups_by_board_query(board_ids):
    query = '''query
    {
        boards(ids: %s) {
            groups {
                id
                title
                archived
                deleted
                color
            }
        }
    }''' % board_ids
    return query


def get_items_by_group_query(board_id, group_id):
    query = '''query
    {
        boards(ids: %s) {
            groups(ids: "%s") {
                id
                title
                items {
                    id
                    name
                }
            }
        }
    }''' % (board_id, group_id)
    return query


def create_group_query(board_id, group_name):
    query = '''
    mutation
    {
        create_group(board_id: %s, group_name: "%s")
        {
            id
        }
    }''' % (board_id, group_name)
    return query


def duplicate_group_query(board_id, group_id):
    query = '''
    mutation
    {
        duplicate_group(board_id: %s, group_id: "%s")
        {
            id
        }
    }''' % (board_id, group_id)
    return query


def archive_group_query(board_id, group_id):
    query = '''
    mutation
    {
        archive_group(board_id: %s, group_id: "%s")
        {
            id
            archived
        }
    }''' % (board_id, group_id)
    return query


def delete_group_query(board_id, group_id):
    query = '''
    mutation
    {
        delete_group(board_id: %s, group_id: "%s")
        {
            id
            deleted
        }
    }''' % (board_id, group_id)
    return query


def get_complexity_query():
    query = '''
    query
    {
        complexity {
            after,
            reset_in_x_seconds
        }
    }'''

    return query
