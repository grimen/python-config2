
# =========================================
#       DEPS
# --------------------------------------

import sys
import os

from os import path, environ
from easypackage.syspath import syspath
from easypackage.root import root as get_root_path

syspath()

from attributedict.collections import AttributeDict


# =========================================
#       CONSTANTS
# --------------------------------------

DEFAULT_ENV = 'development'
DEFAULT_ENV_KEYS = ['PYTHON_ENV', 'ENV']

DEFAULT_CONFIG_ENV = DEFAULT_ENV
DEFAULT_CONFIG_ENV_KEYS = ['NODE_CONFIG_ENV']

DEFAULT_CONFIG_DIRECTORY_NAME = 'config'

DEFAULT_CONFIG_FORMATS = [
    'json',
    'yml',
]

DEFAULT_CONFIG_FORMAT_EXTENSIONS = {
    'json': 'json',
    'yaml': 'yaml',
    'yml': 'yaml',
}

DEFAULT_CONFIG_KEY = 'default'
DEFAULT_CONFIG_FILE_NAME = 'default.yml'
DEFAULT_CONFIG_FILE_TYPE = 'yaml'

DEFAULT_CONFIG_CUSTOM_ENV_FILE_NAME = 'custom-environment-variables.yml'

# REVIEW: https://github.com/lorenwest/node-config/wiki/Environment-Variables

# NODE_CONFIG
# NODE_APP_INSTANCE
# ALLOW_CONFIG_MUTATIONS
# NODE_CONFIG_STRICT_MODE
# DEFAULT_SUPPRESS_NO_CONFIG_WARNING


# =========================================
#       CLASSES
# --------------------------------------

# TODO: subclass `AttributeDict`

class Config(AttributeDict):

    def __init__(self,
        env = None,
        current_path = None,
        config_path = None,
        config_directory_name = None,
    ):
        current_path = current_path or os.getcwd()
        root_path = get_root_path(current_path)

        config_directory_name = config_directory_name or DEFAULT_CONFIG_DIRECTORY_NAME
        config_path = config_path or path.join(root_path, config_directory_name)

        self.__current_path = current_path
        self.__root_path = root_path

        self.__config_directory_name = config_directory_name
        self.__config_path = config_path

        # TODO: logger


# =========================================
#       INSTANCES
# --------------------------------------

config = Config()


# =========================================
#       MAIN
# --------------------------------------

if __name__ == '__main__':

    from easypackage.utils.banner import banner

    with banner('CONFIG'):
        pass
