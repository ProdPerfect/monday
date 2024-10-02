from typing import List, Optional, Union, Any, Mapping

from monday.query_joins import get_boards_query, get_boards_by_id_query, get_board_items_query, \
    get_columns_by_board_query, create_board_by_workspace_query, duplicate_board_query
from monday.resources.base import BaseResource
from monday.resources.types import BoardKind, BoardState, BoardsOrderBy, DuplicateType


class BoardResource(BaseResource):
    def fetch_boards(self, limit: Optional[int] = None, page: Optional[int] = None, ids: Optional[List[int]] = None,
                     board_kind: Optional[BoardKind] = None, state: Optional[BoardState] = None,
                     order_by: Optional[BoardsOrderBy] = None, workspace_ids: Optional[List[int]] = None):
        query = get_boards_query(limit, page, ids, board_kind, state, order_by, workspace_ids)
        return self.client.execute(query)

    def fetch_boards_by_id(self, board_ids: Union[int, str]):
        query = get_boards_by_id_query(board_ids)
        return self.client.execute(query)

    def fetch_items_by_board_id(self, board_ids: Union[int, str], query_params: Optional[Mapping[str, Any]] = None,
                                limit: Optional[int] = None, cursor: Optional[str] = None):
        query = get_board_items_query(board_ids, query_params=query_params, limit=limit, cursor=cursor)
        return self.client.execute(query)

    def fetch_columns_by_board_id(self, board_ids: Union[int, str]):
        query = get_columns_by_board_query(board_ids)
        return self.client.execute(query)

    def create_board(self, board_name: str, board_kind: BoardKind, workspace_id: Optional[int] = None):
        query = create_board_by_workspace_query(board_name, board_kind, workspace_id)
        return self.client.execute(query)

    def duplicate_board(self, board_id: int, duplicate_type: DuplicateType, board_name: Optional[str] = None,
                        folder_id: Optional[int] = None, keep_subscribers: Optional[bool] = None,
                        workspace_id: Optional[int] = None):
        query = duplicate_board_query(board_id, duplicate_type, board_name, folder_id, keep_subscribers, workspace_id)
        return self.client.execute(query)
