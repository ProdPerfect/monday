from enum import Enum
from typing import Mapping
from warnings import warn


class DuplicateType(Enum):
    """Board duplication types"""

    WITH_STRUCTURE = "duplicate_board_with_structure"
    WITH_PULSES = "duplicate_board_with_pulses"
    WITH_PULSES_AND_UPDATES = "duplicate_board_with_pulses_and_updates"


class ColumnType(Enum):
    AUTO_NUMBER = (
        "auto_number"  # Number items according to their order in the group/board
    )
    CHECKBOX = "checkbox"  # Check off items and see what's done at a glance
    COUNTRY = "country"  # Choose a country
    COLOR_PICKER = "color_picker"  # Manage a design system using a color palette
    CREATION_LOG = (
        "creation_log"  # Add the item's creator and creation date automatically
    )
    DATE = "date"  # Add dates like deadlines to ensure you never drop the ball
    DEPENDENCY = "dependency"  # Set up dependencies between items in the board
    DROPDOWN = "dropdown"  # Create a dropdown list of options
    EMAIL = "email"  # Email team members and clients directly from your board
    FILE = "file"  # Add files & docs to your item
    HOUR = "hour"  # Add times to manage and schedule tasks, shifts and more
    ITEM_ID = "item_id"  # Show a unique ID for each item
    LAST_UPDATED = (
        "last_updated"  # Add the person that last updated the item and the date
    )
    LINK = "link"  # Simply hyperlink to any website
    BOARD_RELATION = "board_relation"  # Relationship with another board
    LOCATION = "location"  # Place multiple locations on a geographic map
    LONG_TEXT = "long_text"  # Add large amounts of text without changing column width
    MIRROR = "mirror"  # Display a value from another board through a linked item. If linked item is in another board, BOARD_RELATION also needs to be set up in the board
    NUMBERS = "numbers"  # Add revenue, costs, time estimations and more
    PEOPLE = "people"  # Assign people to improve team work
    PHONE = "phone"  # Call your contacts directly from monday.com
    PROGRESS = "progress"  # Show progress by combining status columns in a battery
    RATING = "rating"  # Rate or rank anything visually
    STATUS = "status"  # Get an instant overview of where things stand
    TEAM = "team"  # Assign a full team to an item
    TAGS = "tags"  # Add tags to categorize items across multiple boards
    TEXT = "text"  # Add textual information e.g. addresses, names or keywords
    TIMELINE = "timeline"  # Visually see a breakdown of your team's workload by time
    TIME_TRACKING = (
        "time_tracking"  # Easily track time spent on each item, group, and board
    )
    VOTE = "vote"  # Vote on an item e.g. pick a new feature or a favorite lunch place
    WEEK = "week"  # Select the week on which each item should be completed
    WORLD_CLOCK = "world_clock"  # Keep track of the time anywhere in the world

    def is_defaults_have_recommended_keys(self, defaults: Mapping[str, any] = None):
        defaults = defaults or {}
        if self == ColumnType.MIRROR:
            mirror_keys = ("relation_column", "displayed_linked_columns")
            missing_keys = [key for key in mirror_keys if key not in defaults]
            if missing_keys:
                warn(
                    "Defaults for mirror column type missing recommended "
                    f"keys: {missing_keys}. Column will appear blank.",
                    UserWarning,
                )
        elif self == ColumnType.BOARD_RELATION:
            relation_keys = ("boardId", "boardIds")
            if not any(key in defaults for key in relation_keys):
                warn(
                    "Defaults for board_relation column type missing "
                    "recommended keys: 'boardId' or 'boardIds'. "
                    "Items from the related board(s) will not be linkable.",
                    UserWarning,
                )


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


class ItemsQueryOperator(Enum):
    """Conditions between query rules"""

    AND = "and"
    OR = "or"


class ItemsOrderByDirection(Enum):
    """Direction to sort items in"""

    ASC = "asc"
    DESC = "desc"


class ItemsQueryRuleOperator(Enum):
    """Condition for value comparison"""

    ANY_OF = "any_of"
    NOT_ANY_OF = "not_any_of"
    IS_EMPTY = "is_empty"
    IS_NOT_EMPTY = "is_not_empty"
    GREATER_THAN = "greater_than"
    GREATER_THAN_OR_EQUALS = "greater_than_or_equals"
    LOWER_THAN = "lower_than"
    LOWER_THAN_OR_EQUAL = "lower_than_or_equal"
    BETWEEN = "between"
    NOT_CONTAINS_TEXT = "not_contains_text"
    CONTAINS_TEXT = "contains_text"
    CONTAINS_TERMS = "contains_terms"
    STARTS_WITH = "starts_with"
    ENDS_WITH = "ends_with"
    WITHIN_THE_NEXT = "within_the_next"
    WITHIN_THE_LAST = "within_the_last"
