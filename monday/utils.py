import json
from enum import Enum
from typing import List


def monday_json_stringify(value):
    # This is necessary because Monday's API says that it requires a JSON encoded string for JSON values,
    # ala JSON.stringify, which doesn't quite work the same as json.dumps, unfortunately.
    # What it ACTUALLY requires (anything else returns an error) is a JSON encoded, JSON encoded string.
    # According to their API, a proper value for label should look like this:
    # "{\"label\":\"Done\"}"

    return json.dumps(json.dumps(value))


def gather_params(params, exclusion_list: List[str]) -> List[str]:
    valid_params: List[str] = []
    for param, value in params:
        if value is None or param in exclusion_list:
            continue
        if isinstance(value, Enum):
            valid_params.append(f"{param}: {value.value}")
            continue
        valid_params.append(f"{param}: {value}")
    return valid_params
