monday
======

.. raw:: html

   <!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

|All Contributors| A monday.com Python Client Library

For an overview of the Monday API, `click
here <https://developer.monday.com/api-reference/docs>`__.

Requirements
^^^^^^^^^^^^

-  Python >= 3.6

Getting started
^^^^^^^^^^^^^^^

``pip install monday``

``monday`` is very simple to use – take a look at the below example:

.. code:: python

   from monday import MondayClient


   monday = MondayClient('your token')

   monday.items.create_item(board_id='12345678', group_id='today',  item_name='Do a thing')

**Available methods:** #### Items Resource (monday.items) -
``create_item(board_id, group_id, item_name, column_values=None, create_labels_if_missing=False)``
- Create an item on a board in the given group with name item_name.

-  ``create_subitem(parent_item_id, subitem_name, column_values=None, create_labels_if_missing=False)``
   - Create a subitem underneath a given parent item. Monday API will
   return an error if the board you’re trying to add to does not have a
   subitems column/at least one subitem created.

-  ``fetch_items_by_column_value(board_id, column_id, value)`` - Fetch
   items on a board by column value.

-  ``fetch_items_by_id(board_id, [ids])`` - Fetch items from any board
   by ids, passed in as an array of integers.

-  ``change_item_value(board_id, item_id, column_id, value)`` - Change
   column values for item on a board. Check Monday’s API for which
   columns are supported.

-  ``change_multiple_column_values(board_id, item_id, column_values, create_labels_if_missing=False)``
   - Change multiple column values for item on a board. Column values
   should be passed in as JSON. Check Monday’s API for which columns are
   supported.

-  ``add_file_to_column(item_id, column_id, file)`` - Upload a file to a
   file type column specified by column_id. Monday limits uploads to
   500MB in size.

-  ``move_item_to_group(item_id, group_id)`` - Move the item to a group
   within the same board.

-  ``archive_item_by_id(item_id)`` - Archive the item by item_id.

-  ``delete_item_by_id(item_id)`` - Delete the item by item_id.

Updates Resource (monday.updates)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  ``create_update(item_id, update_body)`` - Create an update attached
   to a given item.

-  ``fetch_updates(limit, page=None)`` - Fetch a certain number of
   updates, starting from the given page. Default is 1

-  ``fetch_updates_for_item(board_id, item_id, limit)`` - Fetch all
   updates for a certain item on a certain board up to a certain limit,
   set by you. Default is 100 updates

Tags Resource (monday.tags)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  ``fetch_tags(tag_ids=None)`` - Fetch all tags associated with an
   account. Optionally takes a list containing tag ids (if you know
   them). Returns IDs, names, and colors.

Boards Resource (monday.boards)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  ``fetch_boards(**kwargs)`` - Fetch boards associated with an account.
   Returns boards and their groups, tags, and columns. Accepts keyword
   arguments:

   -  ``limit`` - The number of boards returned (*int*. Default is 25).
   -  ``page`` - The page number returned, should you implement
      pagination(*int*. Starts at 1).
   -  ``ids`` - A list of the unique board identifier(s) (*List[int]*).
   -  ``board_kind`` - The board’s kind (*BoardKind*. public / private /
      share).
   -  ``state`` - The state of the board (*BoardState*. all / active /
      archived / deleted. Default is active).
   -  ``order_by`` - The order in which to retrieve your boards
      (*BoardsOrderBy*. created_at / used_at).

-  ``fetch_boards_by_id([board_ids])`` - Since Monday does not allow
   querying boards by name, you can use ``fetch_boards`` to get a list
   of boards, and then ``fetch_boards_by_id`` to get more detailed info
   about the groups and columns on that board. Accepts a comma separated
   list of board ids.

-  ``fetch_columns_by_board_id([board_ids])`` - Get all columns, as well
   as their ids, types, and settings. Accepts a comma separated list of
   board ids.

-  ``fetch_items_by_board_id([board_ids], **kwargs)`` - Get all items on
   a board(s). Accepts a comma separated list of board ids.

   -  ``limit`` - The number of rows returned (*int*. no default).
   -  ``page`` - The page number returned, should you implement
      pagination(*int*. no default).

-  ``create_board(board_name, board_kind, workspace_id)`` - Create board
   with the given name and kind by (and optional) workspace id.

Users Resource (monday.users)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  ``fetch_users(**kwargs)`` - Fetch user information associated with an
   account. See Monday API docs for a list of accepted keyword
   arguments.

Workspaces Resource (monday.workspaces)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  ``get_workspaces()`` - Get all workspaces.

-  ``create_workspace(name, kind, description)`` - Create workspace with
   the given name, kind and description.

-  ``add_users_to_workspace(workspace_id, [user_ids], kind)`` - Add
   given users of the given kind to the given workspace.

-  ``delete_users_from_workspace(workspace_id, [user_ids])`` - Delete
   given users from the given workspace.

-  ``add_teams_to_workspace(workspace_id, [team_ids])`` - Add given
   teams to the given workspace.

-  ``delete_teams_from_workspace(workspace_id, [team_ids])`` - Delete
   given teams from the given workspace.

Groups Resource (monday.groups)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  ``get_groups_by_board([board_ids])`` - Get all groups associated with
   a certain board or boards. Accepts a single id or a comma separated
   list of ids.

-  ``get_items_by_group(board_id, group_id)`` - Get all items that are
   members of a given group.

-  ``create_group(board_id, group_name)`` - Create a group on a given
   board.

-  ``duplicate_group(board_id, group_id)`` - Duplicate a group and all
   its items on a given board.

-  ``archive_group(board_id, group_id)`` - Archive a group on a given
   board.

-  ``delete_group(board_id, group_id)`` - Delete a group on a given
   board.

Notifications Resource (monday.notifications)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  ``create_notification(user_id, target_id, text, target_type)`` - The
   create_notification mutation allows to trigger a notification within
   the platform (will also send out an email if the recipient’s email
   preferences are set up accordingly). ### Additional Resources and
   Code Samples

-  `Read and format all of the items on a
   board <https://github.com/ProdPerfect/monday/wiki/Code-Examples#whole-board-formatting-example>`__

Contributors
------------

.. raw:: html

   <!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->

.. raw:: html

   <!-- prettier-ignore-start -->

.. raw:: html

   <!-- markdownlint-disable -->

.. raw:: html

   <table>

.. raw:: html

   <tbody>

.. raw:: html

   <tr>

.. raw:: html

   <td align="center">

Lemi Boyce💻 🐛 🚧

.. raw:: html

   </td>

.. raw:: html

   <td align="center">

Tony Morello💻

.. raw:: html

   </td>

.. raw:: html

   <td align="center">

chdastolfo💻 🐛 📖 🚧

.. raw:: html

   </td>

.. raw:: html

   <td align="center">

Lucio Mitsuru Seki💻

.. raw:: html

   </td>

.. raw:: html

   <td align="center">

YOGESH NILE💻

.. raw:: html

   </td>

.. raw:: html

   <td align="center">

spencersamuel7💻

.. raw:: html

   </td>

.. raw:: html

   <td align="center">

Alb. C💻

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td align="center">

pevner-p2💻

.. raw:: html

   </td>

.. raw:: html

   <td align="center">

Taylor Cochran💻

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </tbody>

.. raw:: html

   </table>

.. raw:: html

   <!-- markdownlint-restore -->

.. raw:: html

   <!-- prettier-ignore-end -->

.. raw:: html

   <!-- ALL-CONTRIBUTORS-LIST:END -->

.. raw:: html

   <!-- prettier-ignore-start -->

.. raw:: html

   <!-- markdownlint-disable -->

.. raw:: html

   <!-- markdownlint-restore -->

.. raw:: html

   <!-- prettier-ignore-end -->

.. raw:: html

   <!-- ALL-CONTRIBUTORS-LIST:END -->

Bug Reports
~~~~~~~~~~~

TBD

.. |All Contributors| image:: https://img.shields.io/badge/all_contributors-9-orange.svg?style=flat-square
   :target: #contributors-

