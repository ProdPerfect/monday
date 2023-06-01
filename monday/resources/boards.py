import copy
from typing import List, Optional, Required
from monday.resources.base import BaseResource
from monday.query_joins import (
    get_boards_query,
    get_boards_by_id_query,
    get_board_items_query,
    get_columns_by_board_query,
    create_board_by_workspace_query,
)
from monday.resources.types import BoardKind, BoardState, BoardsOrderBy


class BoardResource(BaseResource):
    def __init__(self, token):
        super().__init__(token)

    def fetch_boards(
        self,
        limit: int = None,
        page: int = None,
        ids: List[int] = None,
        board_kind: BoardKind = None,
        state: BoardState = None,
        order_by: BoardsOrderBy = None,
    ):
        query = get_boards_query(limit, page, ids, board_kind, state, order_by)
        return self.client.execute(query)

    def fetch_boards_by_id(self, board_ids):
        query = get_boards_by_id_query(board_ids)
        return self.client.execute(query)

    def fetch_boards_by_workspace_id(
        self,
        limit: int = 1000,
        workspace_id: Required[int] = None,
        page: int = None,
        ids: List[int] = None,
        board_kind: BoardKind = None,
        state: BoardState = None,
        order_by: BoardsOrderBy = None,
    ):
        query = get_boards_query(limit, page, ids, board_kind, state, order_by)
        response = self.client.execute(query)
        filtered_boards = copy.deepcopy(response)
        filtered_boards["data"]["boards"].clear()
        for board in response["data"]["boards"]:
            try:
                if board["workspace"]["id"] == workspace_id:
                    filtered_boards["data"]["boards"].append(board)
            except TypeError:
                continue
        return filtered_boards

    def fetch_items_by_board_id(
        self, board_ids, limit: Optional[int] = None, page: Optional[int] = None
    ):
        query = get_board_items_query(board_ids, limit=limit, page=page)
        return self.client.execute(query)

    def fetch_columns_by_board_id(self, board_ids):
        query = get_columns_by_board_query(board_ids)
        return self.client.execute(query)

    def create_board(
        self, board_name: str, board_kind: BoardKind, workspace_id: int = None
    ):
        query = create_board_by_workspace_query(board_name, board_kind, workspace_id)
        return self.client.execute(query)
