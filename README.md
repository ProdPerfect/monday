# monday
A monday.com Python Client Library


For an overview of the Monday API, [click here](https://monday.com/developers/v2#introduction-section).


#### Requirements
- Python >= 3.6

#### Getting started
`pip install monday`

`monday` is very simple to use -- take a look at the below example:
```python
from monday import MondayClient


monday = MondayClient('your token')

monday.items.create_item(board_id='12345678', group_id='today',  item_name='Do a thing')

```

**Available methods:**
#### Items Resource (monday.items)
- `create_item(board_id, group_id, item_name, column_values=None, create_labels_if_missing=False)` - Create an item on a board in the given group with name item_name.

- `create_subitem(parent_item_id, subitem_name, column_values=None, create_labels_if_missing=False)` - Create a subitem underneath a given parent item. Monday API will return an error if the board you're trying to add to does not have a subitems column/at least one subitem created.

- `fetch_items_by_column_value(board_id, column_id, value)` - Fetch items on a board by column value.

- `fetch_items_by_id(board_id, [ids])` - Fetch items from any board by ids, passed in as an array of integers.

- `change_item_value(board_id, item_id, column_id, value)` - Change column values for item on a board. Check Monday's API for which columns are supported.

- `change_multiple_column_values(board_id, item_id, column_values)` - Change multiple column values for item on a board. Column values should be passed in as JSON. Check Monday's API for which columns are supported.

- `add_file_to_column(item_id, column_id, file)` - Upload a file to a file type column specified by column_id. Monday limits uploads to 500MB in size.

- `delete_item_by_id(item_id)` - Delete the item by item_id.

#### Updates Resource (monday.updates)
- `create_update(item_id, update_body)` - Create an update attached to a given item.

- `fetch_updates(limit, page=None)` - Fetch a certain number of updates, starting from the given page. Default is 1

- `fetch_updates_for_item(board_id, item_id, limit)` - Fetch all updates for a certain item on a certain board up to a certain limit, set by you. Default is 100 updates


#### Tags Resource (monday.tags)
- `fetch_tags(tag_ids=None)` - Fetch all tags associated with an account. Optionally takes a list containing tag ids (if you know them). Returns IDs, names, and colors.


#### Boards Resource (monday.boards)
- `fetch_boards(**kwargs)` - Fetch boards associated with an account. Returns boards and their groups, tags, and columns. Accepts keyword arguments. See Monday API docs for a list of accepted keyword arguments.

- `fetch_boards_by_id([board_ids])` - Since Monday does not allow querying boards by name, you can use `fetch_boards` to get a list of boards, and then `fetch_boards_by_id` to get more detailed info about the groups and columns on that board. Accepts a comma separated list of board ids.

- `fetch_columns_by_board_id([board_ids])` - Get all columns, as well as their ids, types, and settings. Accepts a comma separated list of board ids.

- `fetch_items_by_board_id([board_ids])` - Get all items on a board(s). Accepts a comma separated list of board ids.


#### Users Resource (monday.users)
- `fetch_users(**kwargs)` - Fetch user information associated with an account. See Monday API docs for a list of accepted keyword arguments.


### Groups Resource (monday.groups)
- `get_groups_by_board([board_ids])` - Get all groups associated with a certain board or boards. Accepts a single id or a comma separated list of ids.

- `get_items_by_group(board_id, group_id)` - Get all items that are members of a given group.

- `create_group(board_id, group_name)` - Create a group on a given board.

- `duplicate_group(board_id, group_id)` - Duplicate a group and all its items on a given board.

- `archive_group(board_id, group_id)` - Archive a group on a given board.

- `delete_group(board_id, group_id)` - Delete a group on a given board.

### Build your own query
You can use the graphql query builder to build your own query to send to Monday.
Here is an example of a query to get boards by id.
```python
from monday import MondayClient

monday = MondayClient('your token')

custom_query = monday.custom_query.query_fields(
    query_type="boards",
    ids=[1234567]
).return_values(
    ['id', 'name', 'permissions', 'groups.id.title',
     'columns.id.title.type.settings_str']
).make_query(operation='query')

monday.custom_query.execute(custom_query)

```
Note the formatting of the list passed as return values. This is equivalent to 
adding nested return values to your GraphQL query, like so:

```
id
name
permissions
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
```

If you want to create a query with nested fields, chain query_fields method calls, with
the parent objects being passed in before the child objects. This method call:
```python
client.custom_query.query_fields(
    query_type='boards', ids=1234567
).query_fields(
    query_type='groups', ids='topics'
).return_values(
    ['id', 'title', 'items.id.name']
).make_query(
    operation='query'
)
```
generates the following query:

```
query
{
    boards(ids: 1234567) {
        groups(ids: "topics") {
            id
            title
            items {
                id
                name
            }
        }
    }
}
```


#### Contributions
TBD

#### Bug Reports
TBD 
