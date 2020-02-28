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

monday.items.create_item(board='12345678', group='today',  item_name='Do a thing')

```

**Available methods:**
#### Items Resource (monday.items)
- `create_item(board, group, item_name, column_values=None)` - Create an item on a board in the given group with name item_name.

- `fetch_items_by_column_value(board_id, column, value)` - Fetch items on a board by column value.

- `fetch_items_by_id(board_id, [ids])` - Fetch items from any board by ids, passed in as an array of integers.

- `change_item_value(board_id, item_id, column, value)` - Change column values for item on a board. Check Monday's API for which columns are supported.


#### Updates Resource (monday.updates)
- `create_update(item_id, update_body)` - Create an update attached to a given item.

- `fetch_updates(limit, page=None)` - Fetch a certain number of updates, starting from the given page. Default is 1


#### Tags Resource (monday.tags)
- `fetch_tags(tag_ids=None)` - Fetch all tags associated with an account. Optionally takes a list containing tag ids (if you know them). Returns IDs, names, and colors.


#### Contributions
TBD

#### Bug Reports
TBD 
