
# =========================================
#       DEPS
# --------------------------------------

import rootpath

rootpath.append()

# @see https://github.com/benjaminp/six/blob/master/six.py

import sys
import types


# =========================================
#       CONSTANTS
# --------------------------------------

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3
PY34 = sys.version_info[0:2] >= (3, 4)


# =========================================
#       VARIABLES
# --------------------------------------

if PY3:
    string_types = str,
    integer_types = int,
    class_types = type,
    text_type = str
    binary_type = bytes

else:
    string_types = basestring,
    integer_types = (int, long)
    class_types = (type, types.ClassType)
    text_type = unicode
    binary_type = str
