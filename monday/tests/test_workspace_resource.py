from monday.tests.test_case_resource import BaseTestCase
from monday.query_joins import (get_workspaces_query, create_workspace_query,
                                add_users_to_workspace_query, delete_users_from_workspace_query,
                                add_teams_to_workspace_query, delete_teams_from_workspace_query)


class WorkspaceTestCase(BaseTestCase):
    def setUp(self):
        super(WorkspaceTestCase, self).setUp()

    def test_get_workspaces_query(self):
        query = get_workspaces_query()
        self.assertEqual('''
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
        '''.replace(" ", ""), query.replace(" ", ""))

    def test_create_workspace_query(self):
        query = create_workspace_query(self.workspace_name, self.workspace_kind)
        self.assertIn(str(self.workspace_name), query)
        self.assertIn(str(self.workspace_kind), query)

    def test_add_users_to_workspace_query(self):
        query = add_users_to_workspace_query(self.workspace_id, self.user_ids, self.workspace_user_kind)
        self.assertIn(str(self.workspace_id), query)
        self.assertIn(str(self.user_ids), query)
        self.assertIn(str(self.workspace_user_kind), query)
    
    def test_delete_users_from_workspace_query(self):
        query = delete_users_from_workspace_query(self.workspace_id, self.user_ids)
        self.assertIn(str(self.workspace_id), query)
        self.assertIn(str(self.user_ids), query)

    def test_add_teams_to_workspace_query(self):
        query = add_teams_to_workspace_query(self.workspace_id, self.team_ids)
        self.assertIn(str(self.workspace_id), query)
        self.assertIn(str(self.team_ids), query)
    
    def test_delete_teams_from_workspace_query(self):
        query = delete_teams_from_workspace_query(self.workspace_id, self.team_ids)
        self.assertIn(str(self.workspace_id), query)
        self.assertIn(str(self.team_ids), query)
    

        