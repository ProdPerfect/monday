import json
import re

def python_json_stringify(value):
    # This is necessary because Monday's API requires a JSON encoded string,
    # ala JSON.stringify, which doesn't quite work the same as json.dumps, unfortunately.
    # According to their API, a proper value for label should look like this:
    # "{\"label\":\"Done\"}"

    # Don't do anything with regular ol' string values
    if type(value) != dict:
        return

    value = json.dumps(json.dumps(value))
    # Replace double slashes from above with single slash, or just remove them.
    return re.sub('\\\\\\\\', r'\\', value)
