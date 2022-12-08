# monday
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-9-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
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

- `change_multiple_column_values(board_id, item_id, column_values, create_labels_if_missing=False)` - Change multiple column values for item on a board. Column values should be passed in as JSON. Check Monday's API for which columns are supported.

- `add_file_to_column(item_id, column_id, file)` - Upload a file to a file type column specified by column_id. Monday limits uploads to 500MB in size.

- `move_item_to_group(item_id, group_id)` - Move the item to a group within the same board.

- `archive_item_by_id(item_id)` - Archive the item by item_id.

- `delete_item_by_id(item_id)` - Delete the item by item_id.

#### Updates Resource (monday.updates)
- `create_update(item_id, update_body)` - Create an update attached to a given item.

- `fetch_updates(limit, page=None)` - Fetch a certain number of updates, starting from the given page. Default is 1

- `fetch_updates_for_item(board_id, item_id, limit)` - Fetch all updates for a certain item on a certain board up to a certain limit, set by you. Default is 100 updates


#### Tags Resource (monday.tags)
- `fetch_tags(tag_ids=None)` - Fetch all tags associated with an account. Optionally takes a list containing tag ids (if you know them). Returns IDs, names, and colors.


#### Boards Resource (monday.boards)
- `fetch_boards(**kwargs)` - Fetch boards associated with an account. Returns boards and their groups, tags, and columns. Accepts keyword arguments:
    - `limit` - The number of boards returned (*int*. Default is 25).
    - `page` - The page number returned, should you implement pagination(*int*. Starts at 1).
    - `ids` - A list of the unique board identifier(s) (*List[int]*).
    - `board_kind` - The board's kind (*BoardKind*. public / private / share).
    - `state` - The state of the board (*BoardState*. all / active / archived / deleted. Default is active).
    - `order_by` - The order in which to retrieve your boards (*BoardsOrderBy*. created_at / used_at).


- `fetch_boards_by_id([board_ids])` - Since Monday does not allow querying boards by name, you can use `fetch_boards` to get a list of boards, and then `fetch_boards_by_id` to get more detailed info about the groups and columns on that board. Accepts a comma separated list of board ids.

- `fetch_columns_by_board_id([board_ids])` - Get all columns, as well as their ids, types, and settings. Accepts a comma separated list of board ids.

- `fetch_items_by_board_id([board_ids], **kwargs)` - Get all items on a board(s). Accepts a comma separated list of board ids.
    - `limit` - The number of rows returned (*int*. no default).
    - `page` - The page number returned, should you implement pagination(*int*. no default).

- `create_board(board_name, board_kind, workspace_id)` - Create board with the given name and kind by (and optional) workspace id.


#### Users Resource (monday.users)
- `fetch_users(**kwargs)` - Fetch user information associated with an account. See Monday API docs for a list of accepted keyword arguments.

#### Workspaces Resource (monday.workspaces)
- `get_workspaces()` - Get all workspaces.

- `create_workspace(name, kind, description)` - Create workspace with the given name, kind and description.

- `add_users_to_workspace(workspace_id, [user_ids], kind)` - Add given users of the given kind to the given workspace.

- `delete_users_from_workspace(workspace_id, [user_ids])` - Delete given users from the given workspace.

- `add_teams_to_workspace(workspace_id, [team_ids])` - Add given teams to the given workspace.

- `delete_teams_from_workspace(workspace_id, [team_ids])` - Delete given teams from the given workspace.

#### Groups Resource (monday.groups)
- `get_groups_by_board([board_ids])` - Get all groups associated with a certain board or boards. Accepts a single id or a comma separated list of ids.

- `get_items_by_group(board_id, group_id)` - Get all items that are members of a given group.

- `create_group(board_id, group_name)` - Create a group on a given board.

- `duplicate_group(board_id, group_id)` - Duplicate a group and all its items on a given board.

- `archive_group(board_id, group_id)` - Archive a group on a given board.

- `delete_group(board_id, group_id)` - Delete a group on a given board.

#### Notifications Resource (monday.notifications)
- `create_notification(user_id, target_id, text, target_type)` - The create_notification mutation allows to trigger a notification within the platform (will also send out an email if the recipient's email preferences are set up accordingly).
### Additional Resources and Code Samples

- [Read and format all of the items on a board](https://github.com/ProdPerfect/monday/wiki/Code-Examples#whole-board-formatting-example)

## Contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center"><a href="https://github.com/rhymiz"><img src="https://avatars.githubusercontent.com/u/7029352?v=4?s=100" width="100px;" alt="Lemi Boyce"/><br /><sub><b>Lemi Boyce</b></sub></a><br /><a href="https://github.com/ProdPerfect/monday/commits?author=rhymiz" title="Code">💻</a> <a href="https://github.com/ProdPerfect/monday/issues?q=author%3Arhymiz" title="Bug reports">🐛</a> <a href="#maintenance-rhymiz" title="Maintenance">🚧</a></td>
      <td align="center"><a href="https://github.com/tonymorello"><img src="https://avatars.githubusercontent.com/u/7967400?v=4?s=100" width="100px;" alt="Tony Morello"/><br /><sub><b>Tony Morello</b></sub></a><br /><a href="https://github.com/ProdPerfect/monday/commits?author=tonymorello" title="Code">💻</a></td>
      <td align="center"><a href="https://github.com/chdastolfo"><img src="https://avatars.githubusercontent.com/u/9096407?v=4?s=100" width="100px;" alt="chdastolfo"/><br /><sub><b>chdastolfo</b></sub></a><br /><a href="https://github.com/ProdPerfect/monday/commits?author=chdastolfo" title="Code">💻</a> <a href="https://github.com/ProdPerfect/monday/issues?q=author%3Achdastolfo" title="Bug reports">🐛</a> <a href="https://github.com/ProdPerfect/monday/commits?author=chdastolfo" title="Documentation">📖</a> <a href="#maintenance-chdastolfo" title="Maintenance">🚧</a></td>
      <td align="center"><a href="https://github.com/lucioseki"><img src="https://avatars.githubusercontent.com/u/1480296?v=4?s=100" width="100px;" alt="Lucio Mitsuru Seki"/><br /><sub><b>Lucio Mitsuru Seki</b></sub></a><br /><a href="https://github.com/ProdPerfect/monday/commits?author=lucioseki" title="Code">💻</a></td>
      <td align="center"><a href="https://github.com/yogeshnile"><img src="https://avatars.githubusercontent.com/u/54445087?v=4?s=100" width="100px;" alt="YOGESH NILE"/><br /><sub><b>YOGESH NILE</b></sub></a><br /><a href="https://github.com/ProdPerfect/monday/commits?author=yogeshnile" title="Code">💻</a></td>
      <td align="center"><a href="https://github.com/spencersamuel7"><img src="https://avatars.githubusercontent.com/u/20449820?v=4?s=100" width="100px;" alt="spencersamuel7"/><br /><sub><b>spencersamuel7</b></sub></a><br /><a href="https://github.com/ProdPerfect/monday/commits?author=spencersamuel7" title="Code">💻</a></td>
      <td align="center"><a href="https://github.com/albcl"><img src="https://avatars.githubusercontent.com/u/17050266?v=4?s=100" width="100px;" alt="Alb. C"/><br /><sub><b>Alb. C</b></sub></a><br /><a href="https://github.com/ProdPerfect/monday/commits?author=albcl" title="Code">💻</a></td>
    </tr>
    <tr>
      <td align="center"><a href="https://github.com/pevner-p2"><img src="https://avatars.githubusercontent.com/u/45570949?v=4?s=100" width="100px;" alt="pevner-p2"/><br /><sub><b>pevner-p2</b></sub></a><br /><a href="https://github.com/ProdPerfect/monday/commits?author=pevner-p2" title="Code">💻</a></td>
      <td align="center"><a href="https://github.com/t-a-y-l-o-r"><img src="https://avatars.githubusercontent.com/u/32030464?v=4?s=100" width="100px;" alt="Taylor Cochran"/><br /><sub><b>Taylor Cochran</b></sub></a><br /><a href="https://github.com/ProdPerfect/monday/commits?author=t-a-y-l-o-r" title="Code">💻</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

### Bug Reports
TBD
