from monday.resources.base import BaseResource
from monday.query_joins import (get_workspaces_query, create_workspace_query,
                                add_users_to_workspace_query, delete_users_from_workspace_query,
                                add_teams_to_workspace_query, delete_teams_from_workspace_query)


class WorkspaceResource(BaseResource):
    def __init__(self, token, proxies):
        super().__init__(token, proxies)

    def get_workspaces(self):
        query = get_workspaces_query()
        return self.client.execute(query)
    
    def create_workspace(self, name, kind, description=""):
        query = create_workspace_query(name, kind, description)
        return self.client.execute(query)
    
    def add_users_to_workspace(self, workspace_id, user_ids, kind):
        query = add_users_to_workspace_query(workspace_id, user_ids, kind)
        return self.client.execute(query)
    
    def delete_users_from_workspace(self, workspace_id, user_ids):
        query = delete_users_from_workspace_query(workspace_id, user_ids)
        return self.client.execute(query)
    
    def add_teams_to_workspace(self, workspace_id, team_ids):
        query = add_teams_to_workspace_query(workspace_id, team_ids)
        return self.client.execute(query)
    
    def delete_teams_from_workspace(self, workspace_id, team_ids):
        query = delete_teams_from_workspace_query(workspace_id, team_ids)
        return self.client.execute(query)
    