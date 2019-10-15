# monday
A monday.com Python Client Library


For an overview of the Monday API, [click here](https://monday.com/developers/v2#introduction-section).


#### Requirements
- Python >= 3.6
- GraphQLClient >= 0.2.4

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

- `fetch_items(board_id, column, value)` - Fetch items on a board by column value.

- `change_item_value(board_id, item_id, column, value)` - Change column values for item on a board. Check Monday's API for which columns are supported.


#### Contributions
TBD

#### Bug Reports
TBD 
