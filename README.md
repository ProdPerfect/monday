# monday
A Monday Python Client Library


For an overview of the Monday API, [click here](https://monday.com/developers/v2#introduction-section).


#### Requirements
- Python >= 3.6
- Requests >= 2.19.0
- GraphQLClient

#### Getting started
`pip install monday`

`monday` is very simple to use -- take a look at the below example:
```python
from monday import MondayClient


monday = MondayClient('your token')

monday.items.create_item(board='12345678', group='today',  item_name="what up nerds")

```

#### Tasks Resource (workstreams.tasks)

**Available methods:**
#### Items Resource (monday.items)
- `create_item(board, group, item_name)` - Create an item on a board in the given group with name item_name. 

- `fetch_item(board_id, column, value)` - Fetch a single item on a board by column value.


#### Contributions
TBD

#### Bug Reports
TBD 
