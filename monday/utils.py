import json
from enum import Enum
from typing import List, Iterable, Tuple, Any, Optional


def monday_json_stringify(value):
    # This is necessary because Monday's API says that it requires a JSON encoded string for JSON values,
    # ala JSON.stringify, which doesn't quite work the same as json.dumps, unfortunately.
    # What it ACTUALLY requires (anything else returns an error) is a JSON encoded, JSON encoded string.
    # According to their API, a proper value for label should look like this:
    # "{\"label\":\"Done\"}"

    return json.dumps(json.dumps(value))


def gather_params(params: Iterable[Tuple[str, Any]], excluded_params: Optional[List[str]] = None,
                  exclude_none: bool = True) -> str:
    valid_params = [f"{param}: {format_param_value(value)}" for param, value in params
                    if not ((excluded_params and param in excluded_params) or (value is None and exclude_none))]
    return ', '.join(valid_params)


def format_param_value(value: Any) -> str:
    if value is None:
        return 'null'
    if isinstance(value, str):
        return f'"{value}"'
    if isinstance(value, Enum):
        return str(value.value)
    if isinstance(value, dict):
        return f"{{{gather_params(value.items(), exclude_none=False)}}}"
    if isinstance(value, list):
        return f"[{', '.join(format_param_value(val) for val in value)}]"
    return str(value)
