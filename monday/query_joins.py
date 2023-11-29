import json
from enum import Enum
from typing import List, Union, Optional, Mapping

from monday.resources.types import BoardKind, BoardState, BoardsOrderBy, DuplicateType, ColumnType
from monday.utils import monday_json_stringify, gather_params


# Eventually I will organize this file better but you know what today is not that day.

# ITEM RESOURCE QUERIES
def mutate_item_query(board_id, group_id, item_name, column_values, create_labels_if_missing):
    # Monday does not allow passing through non-JSON null values here,
    # so if you choose not to specify column values, need to set column_values to empty object.
    column_values = column_values or {}

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
    column_values = column_values or {}

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
            items_page_by_column_values(
                board_id: %s,                
                columns: [{column_id: "%s", column_values: ["%s"]}]
            ) {
                cursor
                items {
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
            }
        }''' % (board_id, column_id, value)

    return query


def get_item_by_id_query(ids):
    query = '''query
        {
            items (ids: %s) {
                id,
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


def move_item_to_group_query(item_id, group_id):
    query = '''
    mutation
    {
        move_item_to_group (item_id: %s, group_id: %s)
        {
            id
        }
    }''' % (item_id, group_id)
    return query


def archive_item_query(item_id):
    query = '''
    mutation
    {
        archive_item (item_id: %s)
        {
            id
        }
    }''' % item_id
    return query


def delete_item_query(item_id):
    query = '''
    mutation
    {
        delete_item (item_id: %s)
        {
            id
        }
    }''' % item_id
    return query


# COLUMNS RESOURCE QUERIES
def create_column(
        board_id: int, column_title: str, column_type: Optional[ColumnType] = None, defaults: Mapping[str, any] = None,
        description: str = ""
):
    defaults = defaults or {}

    if not column_type:
        query = """mutation{
            create_column(board_id: %s, title: "%s") {
                id
                title
                description
            }
        }""" % (
            board_id,
            column_title,
        )
    else:
        query = """mutation{
            create_column(board_id: %s, title: "%s", description: "%s", column_type: %s, defaults: %s) {
                id
                title
                description
            }
        }""" % (
            board_id,
            column_title,
            description,
            column_type.value,
            monday_json_stringify(defaults),
        )

    return query


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


def update_multiple_column_values_query(board_id, item_id, column_values, create_labels_if_missing=False):
    query = '''mutation
        {
            change_multiple_column_values (
                board_id: %s,
                item_id: %s,
                column_values: %s,
                create_labels_if_missing: %s
            ) {
                id
                name
                column_values {
                  id
                  text
                }
            }
        }''' % (board_id, item_id, monday_json_stringify(column_values), str(create_labels_if_missing).lower())

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


def delete_update_query(item_id):
    query = """mutation {
        delete_update (id: %s) {
            id
        }
    }""" % item_id

    return query


def get_updates_for_item_query(item, limit):
    query = '''query{                
        items(ids: %s){
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
    }''' % (item, limit)

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
        }''' % (limit, page or 1)

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
def get_board_items_query(board_id: Union[str, int], limit: Optional[int] = None, page: Optional[int] = None) -> str:
    raw_params = locals().items()
    item_params = gather_params(raw_params, exclusion_list=["board_id", "item_ids"])
    joined_params = f"({', '.join(item_params)})" if item_params else ""

    query = '''query{
        boards(ids: %s){
            name
            items_page {
                items %s {
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
        }
    }''' % (board_id, joined_params)

    return query


def get_boards_query(limit: int = None, page: int = None, ids: List[int] = None, board_kind: BoardKind = None,
                     state: BoardState = None, order_by: BoardsOrderBy = None):
    parameters = locals().items()
    query_params = []
    for k, v in parameters:
        if v is not None:
            value = v
            if isinstance(v, Enum):
                value = v.value
            query_params.append("%s: %s" % (k, value))
    joined_params = f"({', '.join(query_params)})" if query_params else ""

    query = '''query
    {
        boards %s {
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
    }''' % joined_params

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


def duplicate_board_query(board_id: int, duplicate_type: DuplicateType, board_name: Optional[str] = None,
                          folder_id: Optional[int] = None, keep_subscribers: Optional[bool] = None,
                          workspace_id: Optional[int] = None):
    optional_params = ""
    if board_name is not None:
        optional_params += ", board_name: \"%s\"" % board_name
    if folder_id is not None:
        optional_params += ", folder_id: %s" % folder_id
    if keep_subscribers is not None:
        optional_params += ", keep_subscribers: %s" % keep_subscribers
    if workspace_id is not None:
        optional_params += ",  workspace_id: %s" % workspace_id

    query = """
    mutation {
        duplicate_board(board_id: %s, duplicate_type: %s%s) {
            board {
                id
            }
        }
    }
    """ % (board_id, duplicate_type.value, optional_params)

    return query


def create_board_by_workspace_query(board_name: str, board_kind: BoardKind, workspace_id=None) -> str:
    workspace_query = f'workspace_id: {workspace_id}' if workspace_id else ''
    query = '''
    mutation {
        create_board (board_name:"%s", board_kind: %s, %s) {
            id
        }
    }
    ''' % (board_name, board_kind.value, workspace_query)
    return query


# USER RESOURCE QUERIES
def get_users_query(**kwargs):
    joined_params = f"({', '.join(['%s: %s' % (arg, kwargs.get(arg)) for arg in kwargs])})" if kwargs else ""
    query = '''query
    {
        users %s {
            id
            name
            email
            enabled
            teams {
              id
              name
            }
        }
    }''' % joined_params
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


def get_workspaces_query():
    query = '''
    query {
        boards {
            workspace {
                id
                name
                kind
                description
            }
        }
    }
    '''
    return query


def create_workspace_query(name, kind, description=""):
    query = '''
    mutation {
        create_workspace (name:"%s", kind: %s, description: "%s") {
            id
            description
        }
    }
    ''' % (name, kind, description)
    return query


def add_users_to_workspace_query(workspace_id, user_ids, kind):
    query = '''
    mutation {
        add_users_to_workspace (workspace_id: %s, user_ids: %s, kind: %s) {
            id
        }
    }
    ''' % (workspace_id, user_ids, kind)
    return query


def delete_users_from_workspace_query(workspace_id, user_ids):
    query = '''
    mutation {
        add_users_to_workspace (workspace_id: %s, user_ids: %s) {
            id
        }
    }
    ''' % (workspace_id, user_ids)
    return query


def add_teams_to_workspace_query(workspace_id, team_ids):
    query = '''
    mutation {
        add_teams_to_workspace (workspace_id: %s, team_ids: %s) {
            id
        }
    }
    ''' % (workspace_id, team_ids)
    return query


def delete_teams_from_workspace_query(workspace_id, team_ids):
    query = '''
    mutation {
        delete_teams_from_workspace (workspace_id: %s, team_ids: %s) {
            id
        }
    }
    ''' % (workspace_id, team_ids)
    return query


def create_notification_query(user_id, target_id, text, target_type):
    query = '''
    mutation {
        create_notification (user_id: %s, target_id: %s, text: "%s", target_type: %s) {
            text
            user_id
            target_id
            target_type
        }
    }
    ''' % (user_id, target_id, text, target_type)
    # Target type may be: Project/Post
    return query


# ME RESOURCE QUERIES
def get_me_query():
    query = """{
    me {
        account {
            id
        },
        birthday,   
        country_code,   
        created_at, 
        join_date,  
        email,  
        enabled,
        id, 
        is_admin,   
        is_guest,   
        is_pending, 
        is_view_only,   
        location,   
        mobile_phone,   
        name,   
        phone,  
        photo_original, 
        photo_small,
        photo_thumb,
        photo_thumb_small,  
        photo_tiny, 
        teams {
            id,
            name
        },  
        time_zone_identifier,   
        title,  
        url,
        utc_hours_diff, 
        }
    }"""
    return query
