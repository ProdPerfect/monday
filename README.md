# workstreams
A Workstreams Python Client Library


For an overview of the Workstream API, [click here](https://s3-us-west-2.amazonaws.com/files.workstreams.ai/docs/api-v1.html).


#### Requirements
- Python >= 3.6
- Requests >= 2.19.0

#### Getting started
`pip install workstreams`

`workstreams` is very simple to use -- take a look at the below example:
```python
from workstreams import WorkstreamsClient


workstreams = WorkstreamsClient('your token')

workstreams.tasks.create(team_id='T3T7BFHGV', channel_id='C3T7D66J1', ws_user_id='U3T716H3N', data={
    'title': 'test task',
    'labels': [
        'init-labelid123'
    ],
    'checklist': [{
        'text': 'never gonna give you up',
        'checked': False
    }],
    'dueDate': '2018-03-07T11:46:17Z',
    'assignee': 'U3T716H3N'
    })

```

Note: `ws_user_id` must always be provided for app tokens. 

#### Tasks Resource (workstreams.tasks)

**Available methods:**
- `create(team_id, channel_id, data, ws_user_id=None)` - Creates a task

- `update(task_id, data, ws_user_id=None)` - Updates a task

- `fetch(task_id, ws_user_id=None)` - Fetch a single task

- `fetch_user_tasks(team_id, user_id, ws_user_id=None)` - Fetch tasks for a single user

- `fetch_tasks_for_users(team_id, user_ids, ws_user_id=None)` - Fetch tasks for multiple users
  * Example: `fetch_tasks_for_users(team_id='T3T7BFHGV', user_ids=['U123456', 'U123457', 'U123458'], ws_user_id=None)`
  
- `fetch_tasks_for_channels(team_id, channel_ids)` - Fetch all tasks for multiple channels
  * Example: `fetch_tasks_for_channels(team_id='T3T7BFHGV', channel_ids=['C3T7D66J1', 'C3T7D66J2'], ws_user_id=None)`
  
- `fetch_changed_tasks_for_channels(team_id, channel_ids, timestamp, ws_user_id=None)` - Fetch all tasks for multiple channels which changed since given timestamp

- `fetch_archived_tasks_for_channels(team_id, channel_ids, ws_user_id=None)` - Fetch all archived tasks for multiple channels

- `archive_tasks(task_ids, ws_user_id=None)` - Archive multiple tasks

- `restore_tasks(task_ids, ws_user_id=None)` - Restore multiple tasks


#### Tasks Resource (workstreams.labels)
**Available methods:**
- `create(team_id, data, ws_user_id=None)` - Creates a new label

- `update(label_id, data, ws_user_id=None)` - Update a label

- `delete(label_id, ws_user_id=None)` - Delete a label

- `fetch(label_id, ws_user_id=None)` - Fetch a single label

- `fetch_team_labels(team_id, ws_user_id=None)` - Fetch all labels for a given team

#### Contributions
TBD

#### Bug Reports
TBD 
