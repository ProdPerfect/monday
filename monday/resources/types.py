from enum import Enum


class DuplicateTypes(Enum):
    """Board duplication types"""

    WITH_STRUCTURE = "duplicate_board_with_structure"
    WITH_PULSES = "duplicate_board_with_pulses"
    WITH_PULSES_AND_UPDATES = "duplicate_board_with_pulses_and_updates"
