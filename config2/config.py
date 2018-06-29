
# =========================================
#       DEPS
# --------------------------------------

import sys
import os
import logging

from os import path, listdir, environ
from pprint import pprint

from deepmerge import Merger

from easypackage.syspath import syspath
from easypackage.root import root as detect_root_path

syspath()

from attributedict.collections import AttributeDict

from config2.compat import string_types

from config2.serializers import json_ as json
from config2.serializers import yaml_ as yaml


# =========================================
#       CONSTANTS
# --------------------------------------

DEFAULT_ENV = None
DEFAULT_ENV_KEYS = ['PYTHON_ENV', 'ENV']

# NOTE: not supported for now
#
# DEFAULT_CONFIG_ENV = DEFAULT_ENV
# DEFAULT_CONFIG_ENV_KEYS = ['NODE_CONFIG_ENV']

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

DEFAULT_CONFIG_SERIALIZERS = {
    'json': json,
    'yaml': yaml,
}

# DEFAULT_CONFIG_FORMAT = 'yaml'

DEFAULT_CONFIG_DEFAULT_FILE_BASENAME = 'default'
DEFAULT_CONFIG_CUSTOM_ENV_FILE_BASENAME = 'custom-environment-variables'

DEFAULT_CONFIG_RESERVED_FILE_BASENAMES = [
    DEFAULT_CONFIG_DEFAULT_FILE_BASENAME,
    DEFAULT_CONFIG_CUSTOM_ENV_FILE_BASENAME,
]

DEFAULT_ROOT_DETECT_FILE_PATTERN = '.git|requirements.txt|setup.py'

# REVIEW: https://github.com/lorenwest/node-config/wiki/Environment-Variables

# NOTE: not supported for now
#
# NODE_CONFIG
# NODE_APP_INSTANCE
# ALLOW_CONFIG_MUTATIONS
# NODE_CONFIG_STRICT_MODE
# DEFAULT_SUPPRESS_NO_CONFIG_WARNING


# =========================================
#       Errors
# --------------------------------------

class ConfigError(Exception):
    pass


# =========================================
#       CLASSES
# --------------------------------------

class Config(AttributeDict):

    def __init__(self,
        env = None,
        path = None,
        config_path = None,
        config_directory_name = None,
        logger = False,
        detect = False,
        silent = True,
    ):
        if isinstance(env, string_types):
            if os.path.sep in env:
                path = env
                env = None

        env = env or DEFAULT_ENV
        path = path or os.getcwd()

        if detect:
            if not isinstance(detect, string_types):
                detect_root_pattern = DEFAULT_ROOT_DETECT_FILE_PATTERN
            else:
                detect_root_pattern = detect

            root_path = detect_root_path(path, detect_root_pattern) or os.getcwd()

        else:
            root_path = path

        config_directory_name = config_directory_name or DEFAULT_CONFIG_DIRECTORY_NAME # TODO: log warning if `config_path` used, means `config_directory_name` is ignored
        config_path = config_path or os.path.join(root_path, config_directory_name)

        if logger == False:
            logger = logger or self.__class__.logger('base')
            logging.disable(logging.INFO)
        else:
            logger = logger or self.__class__.logger('base')

        self.__config_data__ = None
        self.__config_directory_name__ = config_directory_name
        self.__config_files__ = []
        self.__config_path__ = config_path
        self.__default_config_file__ = None
        self.__env_config_file__ = None
        self.__env_config_files__ = []
        self.__env_variables_file__ = None
        self.__env__ = env
        self.__files__ = []
        self.__logger__ = logger
        self.__path__ = path
        self.__root_path__ = root_path
        self.__silent__ = silent

        self.reload()

        super(AttributeDict, self).__init__({})

    def get(self, key = None, default = None):
        if key is None:
            result = self.__dict__
        else:
            result = self.__dict__.get(key, default)

        result = AttributeDict.dict(result)

        return result

    def items(self):
        return list(map(lambda key: (key, self.__dict__.get(key, None)), self.__dict__.keys()))

    def keys(self):
        return list(self.__dict__.keys())

    def values(self):
        return list(map(lambda key: self.__dict__.get(key, None), self.__dict__.keys()))

    def has(self, key):
        return (key in self.keys())

    def reload(self):
        try:
            detected_files = self.__class__.detect_files(self.__config_path__)

            # detect: custom-environment-variables.yml
            env_variables_file = dict(enumerate(filter((lambda config_file:
                config_file.basename == DEFAULT_CONFIG_CUSTOM_ENV_FILE_BASENAME
            ), detected_files))).get(0, None)

            # detect: default.yml
            default_config_file = dict(enumerate(filter((lambda config_file:
                config_file.basename == DEFAULT_CONFIG_DEFAULT_FILE_BASENAME
            ), detected_files))).get(0, None)

            # detect: development.yml, production.yml, ...
            env_config_files = filter((lambda config_file:
                config_file.basename not in DEFAULT_CONFIG_RESERVED_FILE_BASENAMES
            ), detected_files)
            env_config_files = list(env_config_files)

            # current environment only
            env_config_file = dict(enumerate(filter((lambda config_file:
                config_file.basename == self.__env__
            ), detected_files))).get(0, None)

            config_files = [default_config_file] + env_config_files
            config_files = filter((lambda config_file:
                config_file is not None
            ), [default_config_file, env_config_file])
            config_files = list(config_files)

            files = [env_variables_file] + config_files
            files = filter((lambda config_file:
                config_file is not None
            ), files)
            files = list(files)

            # load: custom-environment-variables.yml
            try:
                self.__class__.load_file(env_variables_file)

            except Exception as error:
                if not self.__silent__:
                    raise error

            # load: default.yml
            try:
                self.__class__.load_file(default_config_file)

            except Exception as error:
                if not self.__silent__:
                    raise error

            # load: development.yml, production.yml, ...
            for environment_config_file in env_config_files:
                try:
                    self.__class__.load_file(environment_config_file)

                except Exception as error:
                    if not self.__silent__:
                        raise error

            config_datas = map((lambda _config_file:
                _config_file.data.copy()
            ), config_files)
            config_datas = list(config_datas)

            config_data = self.__class__.merge(*config_datas)

            self.__env_variables_file__ = env_variables_file
            self.__default_config_file__ = default_config_file
            self.__env_config_files__ = env_config_files
            self.__env_config_file__ = env_config_file
            self.__config_files__ = config_files
            self.__files__ = files
            self.__config_data__ = config_data

            self.update(config_data)

        except Exception as error:
            if not self.__silent__:
                raise error

    @staticmethod
    def detect_files(config_path):
        config_files = []

        for config_file_name in listdir(config_path):
            config_file_path = path.join(config_path, config_file_name)
            config_file_name_parts = dict(enumerate(config_file_name.split('.')))
            config_file_basename = config_file_name_parts.get(0, None)
            config_file_extension = config_file_name_parts.get(1, None)

            is_valid_config_file_extension = (config_file_extension in DEFAULT_CONFIG_FORMAT_EXTENSIONS.keys())

            if is_valid_config_file_extension:
                config_files.append(AttributeDict({
                    'basename': config_file_basename,
                    'path': config_file_path,
                    'name': config_file_name,
                    'extension': config_file_extension,
                    'format': DEFAULT_CONFIG_FORMAT_EXTENSIONS.get(config_file_extension, None)
                }))

        return config_files

    @staticmethod
    def load_file(config_file):
        config_file = config_file or {}

        try:
            with open(config_file.path) as file:
                try:
                    config_file.raw = file.read()

                except IOError as error:
                    raise ConfigError('Tried but failed to `read` detected config file `{path}`.'.format(**config_file))

                try:
                    serializer = DEFAULT_CONFIG_SERIALIZERS[config_file.format]

                    config_file.data = serializer.unpack(config_file.raw)

                except Exception as error:
                    raise ConfigError('Tried but failed to `unpack` (de-serialize) detected config file `{path}` using serializer `{format}`.'.format(**config_file))

        except AttributeError as error:
            raise ConfigError('Tried but failed to `load` detected config file.'.format(**config_file) + ' Reason: {}'.format(error))

        return config_file

    @staticmethod
    def logger(key, options = {}):
        logging.basicConfig(
            level = logging.INFO,
            stream = sys.stdout,
            format = "%(levelname)s %(name)s %(message)s"
        )

        logger = logging.getLogger('config2:%s' % (key))

        return logger

    @staticmethod
    def merge(*dicts):
        result_dict = {}

        merger = Merger(
            # merge strategies - for each type.
            [
                (dict, ['merge']),
                (list, ['override']),
            ],

            # fallback strategies - for all other types
            ['override'],

            # conflict strategies
            ['override'],
        )

        for next_dict in dicts:
            merger.merge(result_dict, next_dict)

        return result_dict

    @staticmethod
    def detect_env(keys, default = None):
        # print(type(environment))
        # for key in environment.keys():
        #     print('detect_env', key, environ.get(key, None))
        matching_keys = list(filter(lambda key: environ.get(key, None), keys))
        matching_keys = list(filter(lambda key: key is not None, matching_keys))

        matching_key = len(matching_keys) and matching_keys[0]
        matching_key = matching_key or default

        if matching_key:
            value = environ.get(matching_key, None)
        else:
            value = None

        return value

    @staticmethod
    def create(*args, **kvargs):
        env = dict(enumerate(args)).get(0, None)
        env = env or kvargs.get('env', None)
        env = env or Config.detect_env(DEFAULT_ENV_KEYS, DEFAULT_ENV)

        try:
            del args[0]
        except:
            pass

        try:
            del kvargs['env']
        except:
            pass

        config = Config(env, *args, **kvargs)

        return config


# =========================================
#       INSTANCES
# --------------------------------------

try:
    config = Config.create()

except Exception as error:
    pass


# =========================================
#       MAIN
# --------------------------------------

if __name__ == '__main__':

    from easypackage.utils.banner import banner

    with banner('CONFIG'):
        pass
