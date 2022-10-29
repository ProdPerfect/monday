from enum import Enum


class BoardKind(Enum):
    """Board kinds"""

    PUBLIC = "public"
    PRIVATE = "private"
    SHARE = "share"


class BoardState(Enum):
    """Board available states"""

    ALL = "all"
    ACTIVE = "active"
    ARCHIVED = "archived"
    DELETED = "deleted"


class BoardsOrderBy(Enum):
    """Order to retrieve boards"""

    CREATED_AT = "created_at"
    USED_AT = "used_at"


class DuplicateTypes(Enum):
    """Board duplication types"""

    WITH_STRUCTURE = "duplicate_board_with_structure"
    WITH_PULSES = "duplicate_board_with_pulses"
    WITH_PULSES_AND_UPDATES = "duplicate_board_with_pulses_and_updates"
