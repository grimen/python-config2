
# =========================================
#       DEPS
# --------------------------------------

import rootpath

rootpath.append()

import yaml
import re

from config2.compat import string_types


# =========================================
#       CONSTANTS
# --------------------------------------

DEFAULT_YAML_INDENT = 4
DEFAULT_YAML_TEST_PATTERN = r'[\n\t\s]*[^\[\]\{\}]+[\d\w\W]*\:[\n\t\s]*[\d\w\W]+' # NOTE: very greedy/naive for now


# =========================================
#       FUNCTIONS
# --------------------------------------

def pack(value, indent = DEFAULT_YAML_INDENT):
    try:
        NULL = ''

        if value is None:
            return NULL

        result = yaml.dump(value, default_flow_style = False, indent = indent).strip()

        return result

    except Exception as error:
        raise ValueError('{0}: {1}'.format(error, value))

def unpack(value):
    try:
        NULL = None

        value = value or NULL

        if value is None:
            return None

        result = yaml.load(value)

        return result

    except Exception as error:
        raise ValueError('{0}: {1}'.format(error, value))

def test(value):
    try:
        if value is None:
            return False

        if not isinstance(value, string_types):
            return False

        result = re.match(DEFAULT_YAML_TEST_PATTERN, value)

        return bool(result)

    except Exception as error:
        raise ValueError('{0}: {1}'.format(error, value))
