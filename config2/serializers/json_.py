
# =========================================
#       DEPS
# --------------------------------------

import rootpath

rootpath.append()

import json
import re

from config2.compat import string_types


# =========================================
#       CONSTANTS
# --------------------------------------

DEFAULT_JSON_INDENT = 4
DEFAULT_JSON_TEST_PATTERN = r'^\{.*\}|\[.*\]|null|\"[^\"\{\}\[\]]+\"$' # NOTE: very greedy/naive for now


# =========================================
#       FUNCTIONS
# --------------------------------------

def pack(value, indent = DEFAULT_JSON_INDENT):
    try:
        NULL = 'null'

        if value is None:
            return NULL

        result = json.dumps(value, default = lambda o: repr(o), sort_keys = False, indent = indent)

        return result

    except Exception as error:
        raise ValueError('{0}: {1}'.format(error, value))

def unpack(value):
    try:
        NULL = 'null'

        value = value or NULL

        if value is None:
            return None

        result = json.loads(value)

        return result

    except Exception as error:
        raise ValueError('{0}: {1}'.format(error, value))

def test(value):
    try:
        if value is None:
            return False

        if not isinstance(value, string_types):
            return False

        result = re.match(DEFAULT_JSON_TEST_PATTERN, value)

        return bool(result)

    except Exception as error:
        raise ValueError('{0}: {1}'.format(error, value))
