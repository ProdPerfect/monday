# workstreams
A Workstreams Python Client Library


For an overview of the Workstream API Overview, [click here](https://s3-us-west-2.amazonaws.com/files.workstreams.ai/docs/api-v1.html).


#### Requirements
- Python >= 3.6
- Requests >= 2.19.0

#### Getting started
`pip install workstreams`

`workstreams` is very simple to use -- take a look at the below example:
```python
from workstreams import WorkstreamsClient


workstreams = WorkstreamsClient('your token')

workstreams.tasks.create(team_id='T3T7BFHGV', channel_id='C3T7D66J1', data={
    'title': 'test task',
    'labels': [
        'init-labelid123'
    ],
    'dueDate': '2018-03-07T11:46:17Z',
    'assignee': 'U3T716H3N'
    })

```

#### Tasks Resource
If there is a need to provide a user for given action, you can optionally 
provide a user id `ws_user_id=U123456` for all `create` and `update` operations.

**Available methods:**
- `create(team_id, channel_id, data, ws_user_id=None)` - Creates a task
- `update(task_id, data, ws_user_id=None)` - Updates a task
- `fetch(task_id)` - Fetch a single task
- `fetch_user_tasks(team_id, user_id)` - Fetch tasks for a single user
- `fetch_tasks_for_users(team_id, user_ids)` - Fetch tasks for multiple users
  * Example: `fetch_tasks_for_users(team_id='T3T7BFHGV', 'U123456', 'U123457', 'U123458')`
- `fetch_tasks_for_channels(team_id, channel_ids)` - Fetch all tasks for multiple channels
  * Example: `fetch_tasks_for_channels(team_id='T3T7BFHGV', 'C3T7D66J1', 'C3T7D66J2')`
- `fetch_changed_tasks_for_channels(team_id, channel_ids, timestamp)` - Fetch all tasks for multiple channels which changed since given timestamp
- `fetch_archived_tasks_for_channels(team_id, channel_ids)` - Fetch all archived tasks for multiple channels
- `archive_tasks(task_ids, ws_user_id=None)` - Archive multiple tasks
- `restore_tasks(task_ids, ws_user_id=None)` - Restore multiple tasks


#### Contributions
TBD

#### Bug Reports
TBD 