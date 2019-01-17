
# =========================================
#       DEPS
# --------------------------------------

import json

from os import path
from os import environ as env

import rootpath

rootpath.append()

from attributedict.collections import AttributeDict

from config2.tests import helper
from config2.serializers import yaml_ as yaml

import config2
import config2.config as module

Config = module.Config

deepdict = AttributeDict.dict


# =========================================
#       FIXTURES
# --------------------------------------

fixture_foo_root_path = helper.fixture_path('foo')
fixture_foo_src_nested_path = helper.fixture_path('foo', 'src', 'nested')

fixture_bar_root_path = helper.fixture_path('bar')

fixture_baz_root_path = helper.fixture_path('baz')

package_root_path = helper.root_path()

CUSTOM_ENV = {
    'A1': 'override',
    'A2': 'should have no effect',
    'C2': '42',
}

env_variables_file_basename = 'custom-environment-variables'
env_variables_file_content = helper.fixture('foo/config/{0}.yml'.format(env_variables_file_basename)).read()
env_variables_file_content_mapped = '{0}'.format(env_variables_file_content)
for key in CUSTOM_ENV.keys():
    env_variables_file_content_mapped = env_variables_file_content_mapped.replace(key, json.dumps(CUSTOM_ENV[key]))
env_variables_file_data = yaml.unpack(env_variables_file_content_mapped)
env_variables_file = {
    'name': '{0}.yml'.format(env_variables_file_basename),
    'extension': 'yml',
    'format': 'yaml',
    'basename': env_variables_file_basename,
    'raw': env_variables_file_content,
    'path': '{0}/config/{1}.yml'.format(fixture_foo_root_path, env_variables_file_basename),
    'data': env_variables_file_data,
}

default_config_file_basename = 'default'
default_config_file_content = helper.fixture('foo/config/{0}.yml'.format(default_config_file_basename)).read()
default_config_file_data = yaml.unpack(default_config_file_content)
default_config_file = {
    'name': '{0}.yml'.format(default_config_file_basename),
    'extension': 'yml',
    'format': 'yaml',
    'basename': default_config_file_basename,
    'raw': default_config_file_content,
    'path': '{0}/config/{1}.yml'.format(fixture_foo_root_path, default_config_file_basename),
    'data': default_config_file_data,
}

development_config_file_basename = 'development'
development_config_file_content = helper.fixture('foo/config/{0}.yml'.format(development_config_file_basename)).read()
development_config_file_data = yaml.unpack(development_config_file_content)
development_config_file = {
    'name': '{0}.yml'.format(development_config_file_basename),
    'extension': 'yml',
    'format': 'yaml',
    'basename': development_config_file_basename,
    'raw': development_config_file_content,
    'path': '{0}/config/{1}.yml'.format(fixture_foo_root_path, development_config_file_basename),
    'data': development_config_file_data,
}

foo_config_file_basename = 'foo'
foo_config_file_content = helper.fixture('foo/config/{0}.yml'.format(foo_config_file_basename)).read()
foo_config_file_data = yaml.unpack(foo_config_file_content)
foo_config_file = {
    'name': '{0}.yml'.format(foo_config_file_basename),
    'extension': 'yml',
    'format': 'yaml',
    'basename': foo_config_file_basename,
    'raw': foo_config_file_content,
    'path': '{0}/config/{1}.yml'.format(fixture_foo_root_path, foo_config_file_basename),
    'data': foo_config_file_data,
}

production_config_file_basename = 'production'
production_config_file_content = helper.fixture('foo/config/{0}.yml'.format(production_config_file_basename)).read()
production_config_file_data = yaml.unpack(production_config_file_content)
production_config_file = {
    'name': '{0}.yml'.format(production_config_file_basename),
    'extension': 'yml',
    'format': 'yaml',
    'basename': production_config_file_basename,
    'raw': production_config_file_content,
    'path': '{0}/config/{1}.yml'.format(fixture_foo_root_path, production_config_file_basename),
    'data': production_config_file_data,
}

env_config_files = [
    development_config_file,    # development.yml
    foo_config_file,            # foo.yml
    production_config_file,     # production.yml
]

config_files = [
    default_config_file,        # default.yml

    development_config_file,    # development.yml
    foo_config_file,            # foo.yml
    production_config_file,     # production.yml
]

files = [
    env_variables_file,         # custom-environment-variables.yml

    default_config_file,        # default.yml

    development_config_file,    # development.yml
    foo_config_file,            # foo.yml
    production_config_file,     # production.yml
]

default_config_data = default_config_file.get('data')

default_and_development_config_basename = 'default+development'
default_and_development_config_content = helper.fixture('config/{0}.yml'.format(default_and_development_config_basename)).read()
default_and_development_config_data = yaml.unpack(default_and_development_config_content)

default_and_foo_config_basename = 'default+foo'
default_and_foo_config_content = helper.fixture('config/{0}.yml'.format(default_and_foo_config_basename)).read()
default_and_foo_config_data = yaml.unpack(default_and_foo_config_content)

default_and_production_config_basename = 'default+production'
default_and_production_config_content = helper.fixture('config/{0}.yml'.format(default_and_production_config_basename)).read()
default_and_production_config_data = yaml.unpack(default_and_production_config_content)


# =========================================
#       TEST
# --------------------------------------

class TestCase(helper.TestCase):

    def test__import(self):
        self.assertModule(module)

    def test__instance(self):
        self.assertTrue(isinstance(module.Config(), Config))

    def test_env(self):
        self.assertTrue(hasattr(module.Config(), '__env__'))

        try:
            del env['A1']
        except:
            pass

        try:
            del env['A2']
        except:
            pass

        try:
            del env['C2']
        except:
            pass

        config = module.Config()

        self.assertEqual(config.__env__, None)

        config = module.Config('development')

        self.assertEqual(config.__env__, 'development')

        config = module.Config('foo')

        self.assertEqual(config.__env__, 'foo')

        config = module.Config('production')

        self.assertEqual(config.__env__, 'production')

        config = module.Config('xxx')

        self.assertEqual(config.__env__, 'xxx')

    def test_path(self):
        self.assertTrue(hasattr(module.Config(), '__path__'))

        try:
            del env['A1']
        except:
            pass

        try:
            del env['A2']
        except:
            pass

        try:
            del env['C2']
        except:
            pass

        config = module.Config()

        self.assertEqual(config.__path__, path.join(package_root_path, 'config2', 'tests'))

        config = module.Config(path = package_root_path)

        self.assertEqual(config.__path__, package_root_path)

        config = module.Config(path = fixture_foo_root_path)

        self.assertEqual(config.__path__, fixture_foo_root_path)

        config = module.Config(path = fixture_foo_src_nested_path)

        self.assertEqual(config.__path__, fixture_foo_src_nested_path)

    def test_root_path(self):
        self.assertTrue(hasattr(module.Config(), '__root_path__'))

        try:
            del env['A1']
        except:
            pass

        try:
            del env['A2']
        except:
            pass

        try:
            del env['C2']
        except:
            pass

        config = module.Config()

        self.assertEqual(config.__root_path__, package_root_path)

        config = module.Config()

        self.assertEqual(config.__root_path__, package_root_path)

        config = module.Config(path = fixture_foo_root_path)

        self.assertEqual(config.__root_path__, fixture_foo_root_path)

        config = module.Config(path = fixture_foo_root_path, detect = True)

        self.assertEqual(config.__root_path__, fixture_foo_root_path)

        config = module.Config(path = fixture_foo_src_nested_path)

        self.assertEqual(config.__root_path__, fixture_foo_root_path)

        config = module.Config(path = fixture_foo_src_nested_path, detect = True)

        self.assertEqual(config.__root_path__, fixture_foo_root_path)

    def test_config_path(self):
        self.assertTrue(hasattr(module.Config(), '__config_path__'))

        try:
            del env['A1']
        except:
            pass

        try:
            del env['A2']
        except:
            pass

        try:
            del env['C2']
        except:
            pass

        config = module.Config()

        self.assertEqual(config.__config_path__, path.join(package_root_path, 'config'))

        config = module.Config(path = fixture_foo_root_path)

        self.assertEqual(config.__config_path__, path.join(fixture_foo_root_path, 'config'))

        config = module.Config(path = fixture_foo_src_nested_path)

        self.assertEqual(config.__config_path__, path.join(fixture_foo_root_path, 'config'))

        config = module.Config(path = fixture_foo_root_path, detect = True)

        self.assertEqual(config.__config_path__, path.join(fixture_foo_root_path, 'config'))

        config = module.Config(path = fixture_foo_src_nested_path, detect = True)

        self.assertEqual(config.__config_path__, path.join(fixture_foo_root_path, 'config'))

        config = module.Config(path = fixture_foo_root_path, detect = 'not_a_root_file')

        self.assertEqual(config.__config_path__, path.join(package_root_path, 'config'))

        config = module.Config(path = fixture_foo_src_nested_path, detect = 'not_a_root_file')

        self.assertEqual(config.__config_path__, path.join(package_root_path, 'config'))

    def test_config_directory_name(self):
        self.assertTrue(hasattr(module.Config(), '__config_directory_name__'))

        try:
            del env['A1']
        except:
            pass

        try:
            del env['A2']
        except:
            pass

        try:
            del env['C2']
        except:
            pass

        config = module.Config()

        self.assertEqual(config.__config_directory_name__, 'config')

        config = module.Config()

        self.assertEqual(config.__config_directory_name__, 'config')

        config = module.Config(config_directory_name = 'foo')

        self.assertEqual(config.__config_directory_name__, 'foo')
        self.assertEqual(config.__config_path__, path.join(package_root_path, 'foo'))

    def test_config_data(self):
        self.assertTrue(hasattr(module.Config(), '__config_data__'))

        try:
            del env['A1']
        except:
            pass

        try:
            del env['A2']
        except:
            pass

        try:
            del env['C2']
        except:
            pass

        config = module.Config()

        self.assertDeepEqual(deepdict(config.__config_data__), {})

        config = module.Config(detect = True)

        self.assertDeepEqual(deepdict(config.__config_data__), {})

        config = module.Config(path = package_root_path)

        self.assertDeepEqual(deepdict(config.__config_data__), {})

        config = module.Config(path = package_root_path, detect = True)

        self.assertDeepEqual(deepdict(config.__config_data__), {})

        config = module.Config(path = fixture_foo_root_path)

        self.assertDeepEqual(deepdict(config.__config_data__), default_config_data)

        config = module.Config(path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(deepdict(config.__config_data__), default_config_data)

        config = module.Config(path = fixture_foo_src_nested_path)

        self.assertDeepEqual(deepdict(config.__config_data__), default_config_data)

        config = module.Config(path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(deepdict(config.__config_data__), default_config_data)

        config = module.Config('development')

        self.assertDeepEqual(deepdict(config.__config_data__), {})

        config = module.Config('development', path = package_root_path)

        self.assertDeepEqual(deepdict(config.__config_data__), {})

        config = module.Config('development', path = package_root_path, detect = True)

        self.assertDeepEqual(deepdict(config.__config_data__), {})

        config = module.Config('development', path = fixture_foo_root_path)

        self.assertDeepEqual(deepdict(config.__config_data__), default_and_development_config_data)

        config = module.Config('development', path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(deepdict(config.__config_data__), default_and_development_config_data)

        config = module.Config('development', path = fixture_foo_src_nested_path)

        self.assertDeepEqual(deepdict(config.__config_data__), default_and_development_config_data)

        config = module.Config('development', path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(deepdict(config.__config_data__), default_and_development_config_data)

        config = module.Config('foo')

        self.assertDeepEqual(deepdict(config.__config_data__), {})

        config = module.Config('foo', path = package_root_path)

        self.assertDeepEqual(deepdict(config.__config_data__), {})

        config = module.Config('foo', path = package_root_path, detect = True)

        self.assertDeepEqual(deepdict(config.__config_data__), {})

        config = module.Config('foo', path = fixture_foo_root_path)

        self.assertDeepEqual(deepdict(config.__config_data__), default_and_foo_config_data)

        config = module.Config('foo', path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(deepdict(config.__config_data__), default_and_foo_config_data)

        config = module.Config('foo', path = fixture_foo_src_nested_path)

        self.assertDeepEqual(deepdict(config.__config_data__), default_and_foo_config_data)

        config = module.Config('foo', path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(deepdict(config.__config_data__), default_and_foo_config_data)

        config = module.Config('production')

        self.assertDeepEqual(deepdict(config.__config_data__), {})

        config = module.Config('production', path = package_root_path)

        self.assertDeepEqual(deepdict(config.__config_data__), {})

        config = module.Config('production', path = package_root_path, detect = True)

        self.assertDeepEqual(deepdict(config.__config_data__), {})

        config = module.Config('production', path = fixture_foo_root_path)

        self.assertDeepEqual(deepdict(config.__config_data__), default_and_production_config_data)

        config = module.Config('production', path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(deepdict(config.__config_data__), default_and_production_config_data)

        config = module.Config('production', path = fixture_foo_src_nested_path)

        self.assertDeepEqual(deepdict(config.__config_data__), default_and_production_config_data)

        config = module.Config('production', path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(deepdict(config.__config_data__), default_and_production_config_data)

        config = module.Config('xxx')

        self.assertDeepEqual(deepdict(config.__config_data__), {})

        config = module.Config('xxx', path = package_root_path)

        self.assertDeepEqual(deepdict(config.__config_data__), {})

        config = module.Config('xxx', path = package_root_path, detect = True)

        self.assertDeepEqual(deepdict(config.__config_data__), {})

        config = module.Config('xxx', path = fixture_foo_root_path)

        self.assertDeepEqual(deepdict(config.__config_data__), default_config_data)

        config = module.Config('xxx', path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(deepdict(config.__config_data__), default_config_data)

        config = module.Config('xxx', path = fixture_foo_src_nested_path)

        self.assertDeepEqual(deepdict(config.__config_data__), default_config_data)

        config = module.Config('xxx', path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(deepdict(config.__config_data__), default_config_data)

    def test_files(self):
        self.assertTrue(hasattr(module.Config(), '__files__'))

        env['A1'] = CUSTOM_ENV.get('A1')
        env['A2'] = CUSTOM_ENV.get('A2')
        env['C2'] = CUSTOM_ENV.get('C2')

        config = module.Config()

        self.assertDeepEqual(map(deepdict, config.__files__), map(lambda x: x, []))

        config = module.Config(detect = True)

        self.assertDeepEqual(map(deepdict, config.__files__), map(lambda x: x, []))

        config = module.Config(path = package_root_path)

        self.assertDeepEqual(map(deepdict, config.__files__), map(lambda x: x, []))

        config = module.Config(path = package_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__files__), map(lambda x: x, []))

        config = module.Config(path = fixture_foo_root_path)

        self.assertDeepEqual(map(deepdict, config.__files__), map(deepdict, [default_config_file, env_variables_file]))

        config = module.Config(path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__files__), map(deepdict, [env_variables_file, default_config_file]))

        config = module.Config(path = fixture_foo_src_nested_path)

        self.assertDeepEqual(map(deepdict, config.__files__), map(deepdict, [env_variables_file, default_config_file]))

        config = module.Config(path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__files__), map(deepdict, [env_variables_file, default_config_file]))

        config = module.Config('development')

        self.assertDeepEqual(map(deepdict, config.__files__), map(lambda x: x, []))

        config = module.Config('development', path = package_root_path)

        self.assertDeepEqual(map(deepdict, config.__files__), map(lambda x: x, []))

        config = module.Config('development', path = package_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__files__), map(lambda x: x, []))

        config = module.Config('development', path = fixture_foo_root_path)

        self.assertDeepEqual(map(deepdict, config.__files__), map(deepdict, [env_variables_file, default_config_file, development_config_file]))

        config = module.Config('development', path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__files__), map(deepdict, [env_variables_file, default_config_file, development_config_file]))

        config = module.Config('development', path = fixture_foo_src_nested_path)

        self.assertDeepEqual(map(deepdict, config.__files__), map(deepdict, [env_variables_file, default_config_file, development_config_file]))

        config = module.Config('development', path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__files__), map(deepdict, [env_variables_file, default_config_file, development_config_file]))

        config = module.Config('foo')

        self.assertDeepEqual(map(deepdict, config.__files__), map(lambda x: x, []))

        config = module.Config('foo', path = package_root_path)

        self.assertDeepEqual(map(deepdict, config.__files__), map(lambda x: x, []))

        config = module.Config('foo', path = package_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__files__), map(lambda x: x, []))

        config = module.Config('foo', path = fixture_foo_root_path)

        self.assertDeepEqual(map(deepdict, config.__files__), map(deepdict, [env_variables_file, default_config_file, foo_config_file]))

        config = module.Config('foo', path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__files__), map(deepdict, [env_variables_file, default_config_file, foo_config_file]))

        config = module.Config('foo', path = fixture_foo_src_nested_path)

        self.assertDeepEqual(map(deepdict, config.__files__), map(deepdict, [env_variables_file, default_config_file, foo_config_file]))

        config = module.Config('foo', path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__files__), map(deepdict, [env_variables_file, default_config_file, foo_config_file]))

        config = module.Config('production')

        self.assertDeepEqual(map(deepdict, config.__files__), map(lambda x: x, []))

        config = module.Config('production', path = package_root_path)

        self.assertDeepEqual(map(deepdict, config.__files__), map(lambda x: x, []))

        config = module.Config('production', path = package_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__files__), map(lambda x: x, []))

        config = module.Config('production', path = fixture_foo_root_path)

        self.assertDeepEqual(map(deepdict, config.__files__), map(deepdict, [env_variables_file, default_config_file, production_config_file]))

        config = module.Config('production', path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__files__), map(deepdict, [env_variables_file, default_config_file, production_config_file]))

        config = module.Config('production', path = fixture_foo_src_nested_path)

        self.assertDeepEqual(map(deepdict, config.__files__), map(deepdict, [env_variables_file, default_config_file, production_config_file]))

        config = module.Config('production', path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__files__), map(deepdict, [env_variables_file, default_config_file, production_config_file]))

        config = module.Config('xxx')

        self.assertDeepEqual(map(deepdict, config.__files__), map(lambda x: x, []))

        config = module.Config('xxx', path = package_root_path)

        self.assertDeepEqual(map(deepdict, config.__files__), map(lambda x: x, []))

        config = module.Config('xxx', path = package_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__files__), map(lambda x: x, []))

        config = module.Config('xxx', path = fixture_foo_root_path)

        self.assertDeepEqual(map(deepdict, config.__files__), map(deepdict, [env_variables_file, default_config_file]))

        config = module.Config('xxx', path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__files__), map(deepdict, [env_variables_file, default_config_file]))

        config = module.Config('xxx', path = fixture_foo_src_nested_path)

        self.assertDeepEqual(map(deepdict, config.__files__), map(deepdict, [env_variables_file, default_config_file]))

        config = module.Config('xxx', path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__files__), map(deepdict, [env_variables_file, default_config_file]))

        del env['A1']
        del env['A2']
        del env['C2']

    def test_config_files(self):
        self.assertTrue(hasattr(module.Config(), '__config_files__'))

        try:
            del env['A1']
        except:
            pass

        try:
            del env['A2']
        except:
            pass

        try:
            del env['C2']
        except:
            pass

        config = module.Config()

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(lambda x: x, []))

        config = module.Config(detect = True)

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(lambda x: x, []))

        config = module.Config(path = package_root_path)

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(lambda x: x, []))

        config = module.Config(path = package_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(lambda x: x, []))

        config = module.Config(path = fixture_foo_root_path)

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(deepdict, [default_config_file]))

        config = module.Config(path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(deepdict, [default_config_file]))

        config = module.Config(path = fixture_foo_src_nested_path)

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(lambda x: x, [default_config_file]))

        config = module.Config(path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(deepdict, [default_config_file]))

        config = module.Config('development')

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(lambda x: x, []))

        config = module.Config('development', path = package_root_path)

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(lambda x: x, []))

        config = module.Config('development', path = package_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(lambda x: x, []))

        config = module.Config('development', path = fixture_foo_root_path)

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(deepdict, [default_config_file, development_config_file]))

        config = module.Config('development', path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(deepdict, [default_config_file, development_config_file]))

        config = module.Config('development', path = fixture_foo_src_nested_path)

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(deepdict, [default_config_file, development_config_file]))

        config = module.Config('development', path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(deepdict, [default_config_file, development_config_file]))

        config = module.Config('foo')

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(lambda x: x, []))

        config = module.Config('foo', path = package_root_path)

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(lambda x: x, []))

        config = module.Config('foo', path = package_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(lambda x: x, []))

        config = module.Config('foo', path = fixture_foo_root_path)

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(deepdict, [default_config_file, foo_config_file]))

        config = module.Config('foo', path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(deepdict, [default_config_file, foo_config_file]))

        config = module.Config('foo', path = fixture_foo_src_nested_path)

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(deepdict, [default_config_file, foo_config_file]))

        config = module.Config('foo', path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(deepdict, [default_config_file, foo_config_file]))

        config = module.Config('production')

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(lambda x: x, []))

        config = module.Config('production', path = package_root_path)

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(lambda x: x, []))

        config = module.Config('production', path = package_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(lambda x: x, []))

        config = module.Config('production', path = fixture_foo_root_path)

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(deepdict, [default_config_file, production_config_file]))

        config = module.Config('production', path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(deepdict, [default_config_file, production_config_file]))

        config = module.Config('production', path = fixture_foo_src_nested_path)

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(deepdict, [default_config_file, production_config_file]))

        config = module.Config('production', path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(deepdict, [default_config_file, production_config_file]))

        config = module.Config('xxx')

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(lambda x: x, []))

        config = module.Config('xxx', path = package_root_path)

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(lambda x: x, []))

        config = module.Config('xxx', path = package_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(lambda x: x, []))

        config = module.Config('xxx', path = fixture_foo_root_path)

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(deepdict, [default_config_file]))

        config = module.Config('xxx', path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(deepdict, [default_config_file]))

        config = module.Config('xxx', path = fixture_foo_src_nested_path)

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(deepdict, [default_config_file]))

        config = module.Config('xxx', path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__config_files__), map(deepdict, [default_config_file]))

    def test_default_config_file(self):
        self.assertTrue(hasattr(module.Config(), '__default_config_file__'))

        try:
            del env['A1']
        except:
            pass

        try:
            del env['A2']
        except:
            pass

        try:
            del env['C2']
        except:
            pass

        config = module.Config()

        self.assertDeepEqual(config.__default_config_file__, None)

        config = module.Config(detect = True)

        self.assertDeepEqual(config.__default_config_file__, None)

        config = module.Config(path = package_root_path)

        self.assertDeepEqual(config.__default_config_file__, None)

        config = module.Config(path = package_root_path, detect = True)

        self.assertDeepEqual(config.__default_config_file__, None)

        config = module.Config(path = fixture_foo_root_path)

        self.assertDeepEqual(deepdict(config.__default_config_file__), default_config_file)

        config = module.Config(path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(deepdict(config.__default_config_file__), default_config_file)

        config = module.Config(path = fixture_foo_src_nested_path)

        self.assertDeepEqual(deepdict(config.__default_config_file__), default_config_file)

        config = module.Config(path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(deepdict(config.__default_config_file__), default_config_file)

        config = module.Config('development')

        self.assertDeepEqual(config.__default_config_file__, None)

        config = module.Config('development', path = package_root_path)

        self.assertDeepEqual(config.__default_config_file__, None)

        config = module.Config('development', path = package_root_path, detect = True)

        self.assertDeepEqual(config.__default_config_file__, None)

        config = module.Config('development', path = fixture_foo_root_path)

        self.assertDeepEqual(deepdict(config.__default_config_file__), default_config_file)

        config = module.Config('development', path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(deepdict(config.__default_config_file__), default_config_file)

        config = module.Config('development', path = fixture_foo_src_nested_path)

        self.assertDeepEqual(deepdict(config.__default_config_file__), default_config_file)

        config = module.Config('development', path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(deepdict(config.__default_config_file__), default_config_file)

        config = module.Config('foo')

        self.assertDeepEqual(config.__default_config_file__, None)

        config = module.Config('foo', path = package_root_path)

        self.assertDeepEqual(config.__default_config_file__, None)

        config = module.Config('foo', path = package_root_path, detect = True)

        self.assertDeepEqual(config.__default_config_file__, None)

        config = module.Config('foo', path = fixture_foo_root_path)

        self.assertDeepEqual(deepdict(config.__default_config_file__), default_config_file)

        config = module.Config('foo', path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(deepdict(config.__default_config_file__), default_config_file)

        config = module.Config('foo', path = fixture_foo_src_nested_path)

        self.assertDeepEqual(deepdict(config.__default_config_file__), default_config_file)

        config = module.Config('foo', path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(deepdict(config.__default_config_file__), default_config_file)

        config = module.Config('production')

        self.assertDeepEqual(config.__default_config_file__, None)

        config = module.Config('production', path = package_root_path)

        self.assertDeepEqual(config.__default_config_file__, None)

        config = module.Config('production', path = package_root_path, detect = True)

        self.assertDeepEqual(config.__default_config_file__, None)

        config = module.Config('production', path = fixture_foo_root_path)

        self.assertDeepEqual(deepdict(config.__default_config_file__), default_config_file)

        config = module.Config('production', path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(deepdict(config.__default_config_file__), default_config_file)

        config = module.Config('production', path = fixture_foo_src_nested_path)

        self.assertDeepEqual(deepdict(config.__default_config_file__), default_config_file)

        config = module.Config('production', path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(deepdict(config.__default_config_file__), default_config_file)

        config = module.Config('xxx')

        self.assertDeepEqual(config.__default_config_file__, None)

        config = module.Config('xxx', path = package_root_path)

        self.assertDeepEqual(config.__default_config_file__, None)

        config = module.Config('xxx', path = package_root_path, detect = True)

        self.assertDeepEqual(config.__default_config_file__, None)

        config = module.Config('xxx', path = fixture_foo_root_path)

        self.assertDeepEqual(deepdict(config.__default_config_file__), default_config_file)

        config = module.Config('xxx', path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(deepdict(config.__default_config_file__), default_config_file)

        config = module.Config('xxx', path = fixture_foo_src_nested_path)

        self.assertDeepEqual(deepdict(config.__default_config_file__), default_config_file)

        config = module.Config('xxx', path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(deepdict(config.__default_config_file__), default_config_file)

    def test_env_config_files(self):
        self.assertTrue(hasattr(module.Config(), '__env_config_files__'))

        try:
            del env['A1']
        except:
            pass

        try:
            del env['A2']
        except:
            pass

        try:
            del env['C2']
        except:
            pass

        config = module.Config()

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(lambda x: x, []))

        config = module.Config(detect = True)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(lambda x: x, []))

        config = module.Config(path = package_root_path)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(lambda x: x, []))

        config = module.Config(path = package_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(lambda x: x, []))

        config = module.Config(path = fixture_foo_root_path)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(deepdict, env_config_files))

        config = module.Config(path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(deepdict, env_config_files))

        config = module.Config(path = fixture_foo_src_nested_path)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(deepdict, env_config_files))

        config = module.Config(path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(deepdict, env_config_files))

        config = module.Config('development')

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(lambda x: x, []))

        config = module.Config('development', path = package_root_path)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(lambda x: x, []))

        config = module.Config('development', path = package_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(lambda x: x, []))

        config = module.Config('development', path = fixture_foo_root_path)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(deepdict, env_config_files))

        config = module.Config('development', path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(deepdict, env_config_files))

        config = module.Config('development', path = fixture_foo_src_nested_path)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(deepdict, env_config_files))

        config = module.Config('development', path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(deepdict, env_config_files))

        config = module.Config('foo')

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(lambda x: x, []))

        config = module.Config('foo', path = package_root_path)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(lambda x: x, []))

        config = module.Config('foo', path = package_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(lambda x: x, []))

        config = module.Config('foo', path = fixture_foo_root_path)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(deepdict, env_config_files))

        config = module.Config('foo', path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(deepdict, env_config_files))

        config = module.Config('foo', path = fixture_foo_src_nested_path)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(deepdict, env_config_files))

        config = module.Config('foo', path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(deepdict, env_config_files))

        config = module.Config('production')

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(lambda x: x, []))

        config = module.Config('production', path = package_root_path)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(lambda x: x, []))

        config = module.Config('production', path = package_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(lambda x: x, []))

        config = module.Config('production', path = fixture_foo_root_path)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(deepdict, env_config_files))

        config = module.Config('production', path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(deepdict, env_config_files))

        config = module.Config('production', path = fixture_foo_src_nested_path)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(deepdict, env_config_files))

        config = module.Config('production', path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(deepdict, env_config_files))

        config = module.Config('xxx')

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(lambda x: x, []))

        config = module.Config('xxx', path = package_root_path)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(lambda x: x, []))

        config = module.Config('xxx', path = package_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(lambda x: x, []))

        config = module.Config('xxx', path = fixture_foo_root_path)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(deepdict, env_config_files))

        config = module.Config('xxx', path = fixture_foo_root_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(deepdict, env_config_files))

        config = module.Config('xxx', path = fixture_foo_src_nested_path)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(deepdict, env_config_files))

        config = module.Config('xxx', path = fixture_foo_src_nested_path, detect = True)

        self.assertDeepEqual(map(deepdict, config.__env_config_files__), map(deepdict, env_config_files))

    def test_config(self):
        try:
            del env['A1']
        except:
            pass

        try:
            del env['A2']
        except:
            pass

        try:
            del env['C2']
        except:
            pass

        config = module.Config(path = fixture_foo_root_path)

        self.assertDeepEqual(deepdict(config), deepdict({
            '__config_data__': config.__config_data__,
            '__config_directory_name__': config.__config_directory_name__,
            '__config_files__': config.__config_files__,
            '__config_path__': config.__config_path__,
            '__default_config_file__': config.__default_config_file__,
            '__env_config_file__': config.__env_config_file__,
            '__env_config_files__': config.__env_config_files__,
            '__env_variables_file__': config.__env_variables_file__,
            '__env__': config.__env__,
            '__files__': config.__files__,
            '__logger__': config.__logger__,
            '__path__': config.__path__,
            '__root_path__': config.__root_path__,
            '__silent__': config.__silent__,

            'a1': 'DEFAULT 1',
            'a2': {
                'b1': [1, 2, 3],
                'b2': ['foo', 'bar'],
                'b3': {
                    'c1': 1,
                    'c2': 'DEFAULT 2',
                },
            },
        }))

        config = module.Config('development', path = fixture_foo_root_path)

        self.assertDeepEqual(deepdict(config), deepdict({
            '__config_data__': config.__config_data__,
            '__config_directory_name__': config.__config_directory_name__,
            '__config_files__': config.__config_files__,
            '__config_path__': config.__config_path__,
            '__default_config_file__': config.__default_config_file__,
            '__env_config_file__': config.__env_config_file__,
            '__env_config_files__': config.__env_config_files__,
            '__env_variables_file__': config.__env_variables_file__,
            '__env__': config.__env__,
            '__files__': config.__files__,
            '__logger__': config.__logger__,
            '__path__': config.__path__,
            '__root_path__': config.__root_path__,
            '__silent__': config.__silent__,

            'a1': 'DEFAULT 1',
            'a2': {
                'b1': [1, 2, 3],
                'b2': ['DEV 1'],
                'b3': {
                    'c1': 1,
                    'c2': 'DEV 2',
                },
            },
            'some_key_only_for_dev': True,
        }))

        config = module.Config('foo', path = fixture_foo_root_path)

        self.assertDeepEqual(deepdict(config), deepdict({
            '__config_data__': config.__config_data__,
            '__config_directory_name__': config.__config_directory_name__,
            '__config_files__': config.__config_files__,
            '__config_path__': config.__config_path__,
            '__default_config_file__': config.__default_config_file__,
            '__env_config_file__': config.__env_config_file__,
            '__env_config_files__': config.__env_config_files__,
            '__env_variables_file__': config.__env_variables_file__,
            '__env__': config.__env__,
            '__files__': config.__files__,
            '__logger__': config.__logger__,
            '__path__': config.__path__,
            '__root_path__': config.__root_path__,
            '__silent__': config.__silent__,

            'a1': 'DEFAULT 1',
            'a2': {
                'b1': [1, 2, 3],
                'b2': ['FOO 1'],
                'b3': {
                    'c1': 1,
                    'c2': 'FOO 2',
                },
            },
            'some_key_only_for_foo': True,
        }))

        config = module.Config('production', path = fixture_foo_root_path)

        self.assertDeepEqual(deepdict(config), deepdict({
            '__config_data__': config.__config_data__,
            '__config_directory_name__': config.__config_directory_name__,
            '__config_files__': config.__config_files__,
            '__config_path__': config.__config_path__,
            '__default_config_file__': config.__default_config_file__,
            '__env_config_file__': config.__env_config_file__,
            '__env_config_files__': config.__env_config_files__,
            '__env_variables_file__': config.__env_variables_file__,
            '__env__': config.__env__,
            '__files__': config.__files__,
            '__logger__': config.__logger__,
            '__path__': config.__path__,
            '__root_path__': config.__root_path__,
            '__silent__': config.__silent__,

            'a1': 'DEFAULT 1',
            'a2': {
                'b1': [1, 2, 3],
                'b2': ['PROD 1'],
                'b3': {
                    'c1': 1,
                    'c2': 'PROD 2',
                },
            },
            'some_key_only_for_prod': True,
        }))

        config = module.Config('xxx', path = fixture_foo_root_path)

        self.assertDeepEqual(deepdict(config), deepdict({
            '__config_data__': config.__config_data__,
            '__config_directory_name__': config.__config_directory_name__,
            '__config_files__': config.__config_files__,
            '__config_path__': config.__config_path__,
            '__default_config_file__': config.__default_config_file__,
            '__env_config_file__': config.__env_config_file__,
            '__env_config_files__': config.__env_config_files__,
            '__env_variables_file__': config.__env_variables_file__,
            '__env__': config.__env__,
            '__files__': config.__files__,
            '__logger__': config.__logger__,
            '__path__': config.__path__,
            '__root_path__': config.__root_path__,
            '__silent__': config.__silent__,

            'a1': 'DEFAULT 1',
            'a2': {
                'b1': [1, 2, 3],
                'b2': ['foo', 'bar'],
                'b3': {
                    'c1': 1,
                    'c2': 'DEFAULT 2',
                },
            },
        }))

        env['A1'] = CUSTOM_ENV.get('A1')
        env['A2'] = CUSTOM_ENV.get('A2')
        env['C2'] = CUSTOM_ENV.get('C2')

        config = module.Config('foo', path = fixture_foo_root_path)

        self.assertDeepEqual(deepdict(config), deepdict({
            '__config_data__': config.__config_data__,
            '__config_directory_name__': config.__config_directory_name__,
            '__config_files__': config.__config_files__,
            '__config_path__': config.__config_path__,
            '__default_config_file__': config.__default_config_file__,
            '__env_config_file__': config.__env_config_file__,
            '__env_config_files__': config.__env_config_files__,
            '__env_variables_file__': config.__env_variables_file__,
            '__env__': config.__env__,
            '__files__': config.__files__,
            '__logger__': config.__logger__,
            '__path__': config.__path__,
            '__root_path__': config.__root_path__,
            '__silent__': config.__silent__,

            'a1': env['A1'],
            'a2': {
                'b1': [1, 2, 3],
                'b2': ['FOO 1'],
                'b3': {
                    'c1': 1,
                    'c2': env['C2'],
                },
            },
            'some_key_only_for_foo': True,
        }))

        del env['A1']
        del env['A2']
        del env['C2']

        # NOTE: verify case of `custom-environment-variables` empty
        config = module.Config('bar', path = fixture_bar_root_path, silent = False)

        self.assertDeepEqual(deepdict(config), deepdict({
            '__config_data__': config.__config_data__,
            '__config_directory_name__': config.__config_directory_name__,
            '__config_files__': config.__config_files__,
            '__config_path__': config.__config_path__,
            '__default_config_file__': config.__default_config_file__,
            '__env_config_file__': config.__env_config_file__,
            '__env_config_files__': config.__env_config_files__,
            '__env_variables_file__': config.__env_variables_file__,
            '__env__': config.__env__,
            '__files__': config.__files__,
            '__logger__': config.__logger__,
            '__path__': config.__path__,
            '__root_path__': config.__root_path__,
            '__silent__': config.__silent__,

            'a1': 'DEFAULT 1',
            'a2': {
                'b1': [1, 2, 3],
                'b2': ['foo', 'bar'],
                'b3': {
                    'c1': 1,
                    'c2': 'DEFAULT 2',
                },
            },
        }))

        # NOTE: verify case of `custom-environment-variables` non-existing
        config = module.Config('baz', path = fixture_baz_root_path, silent = False)

        self.assertDeepEqual(deepdict(config), deepdict({
            '__config_data__': config.__config_data__,
            '__config_directory_name__': config.__config_directory_name__,
            '__config_files__': config.__config_files__,
            '__config_path__': config.__config_path__,
            '__default_config_file__': config.__default_config_file__,
            '__env_config_file__': config.__env_config_file__,
            '__env_config_files__': config.__env_config_files__,
            '__env_variables_file__': config.__env_variables_file__,
            '__env__': config.__env__,
            '__files__': config.__files__,
            '__logger__': config.__logger__,
            '__path__': config.__path__,
            '__root_path__': config.__root_path__,
            '__silent__': config.__silent__,
        }))

    def test_get_env(self):
        self.assertTrue(hasattr(module.Config(), 'get_env'))

        try:
            del env['ENV']
        except:
            pass

        try:
            del env['PYTHON_ENV']
        except:
            pass

        config = module.Config('development')

        self.assertEqual(config.get_env(), 'development')

        config = module.Config('foo')

        self.assertEqual(config.get_env(), 'foo')

        config = module.Config('production')

        self.assertEqual(config.get_env(), 'production')

        env['PYTHON_ENV'] = 'development'

        # config = module.Config()
        config = module.Config.create()

        self.assertEqual(config.get_env(), 'development')

        env['PYTHON_ENV'] = 'foo'

        # config = module.Config()
        config = module.Config.create()

        self.assertEqual(config.get_env(), 'foo')

        env['PYTHON_ENV'] = 'production'

        # config = module.Config()
        config = module.Config.create()

        self.assertEqual(config.get_env(), 'production')

        try:
            del env['ENV']
        except:
            pass

        try:
            del env['PYTHON_ENV']
        except:
            pass

        # config = module.Config()
        config = module.Config.create()

        self.assertEqual(config.get_env(), None)

    def test_get(self):
        self.assertTrue(hasattr(module.Config(), 'get'))

        try:
            del env['A1']
        except:
            pass

        try:
            del env['A2']
        except:
            pass

        try:
            del env['C2']
        except:
            pass

        config = module.Config(path = fixture_foo_root_path)

        self.assertDeepEqual(deepdict(config.get()), deepdict({
            '__config_data__': config.__config_data__,
            '__config_directory_name__': config.__config_directory_name__,
            '__config_files__': config.__config_files__,
            '__config_path__': config.__config_path__,
            '__default_config_file__': config.__default_config_file__,
            '__env_config_file__': config.__env_config_file__,
            '__env_config_files__': config.__env_config_files__,
            '__env_variables_file__': config.__env_variables_file__,
            '__env__': config.__env__,
            '__files__': config.__files__,
            '__logger__': config.__logger__,
            '__path__': config.__path__,
            '__root_path__': config.__root_path__,
            '__silent__': config.__silent__,

            'a1': 'DEFAULT 1',
            'a2': {
                'b1': [1, 2, 3],
                'b2': ['foo', 'bar'],
                'b3': {
                    'c1': 1,
                    'c2': 'DEFAULT 2',
                },
            },
        }))

        config = module.Config('development', path = fixture_foo_root_path)

        self.assertEqual(config.__env__, 'development')
        self.assertTrue(isinstance(config.__env_config_file__, dict))
        self.assertTrue(config.__env__ in config.__env_config_file__.path)
        self.assertDeepEqual(deepdict(config.get()), deepdict({
            '__config_data__': config.__config_data__,
            '__config_directory_name__': config.__config_directory_name__,
            '__config_files__': config.__config_files__,
            '__config_path__': config.__config_path__,
            '__default_config_file__': config.__default_config_file__,
            '__env_config_file__': config.__env_config_file__,
            '__env_config_files__': config.__env_config_files__,
            '__env_variables_file__': config.__env_variables_file__,
            '__env__': config.__env__,
            '__files__': config.__files__,
            '__logger__': config.__logger__,
            '__path__': config.__path__,
            '__root_path__': config.__root_path__,
            '__silent__': config.__silent__,

            'a1': 'DEFAULT 1',
            'a2': {
                'b1': [1, 2, 3],
                'b2': ['DEV 1'],
                'b3': {
                    'c1': 1,
                    'c2': 'DEV 2',
                },
            },
            'some_key_only_for_dev': True,
        }))

        config = module.Config('foo', path = fixture_foo_root_path)

        self.assertEqual(config.__env__, 'foo')
        self.assertTrue(isinstance(config.__env_config_file__, dict))
        self.assertTrue(config.__env__ in config.__env_config_file__.path)
        self.assertDeepEqual(deepdict(config.get()), deepdict({
            '__config_data__': config.__config_data__,
            '__config_directory_name__': config.__config_directory_name__,
            '__config_files__': config.__config_files__,
            '__config_path__': config.__config_path__,
            '__default_config_file__': config.__default_config_file__,
            '__env_config_file__': config.__env_config_file__,
            '__env_config_files__': config.__env_config_files__,
            '__env_variables_file__': config.__env_variables_file__,
            '__env__': config.__env__,
            '__files__': config.__files__,
            '__logger__': config.__logger__,
            '__path__': config.__path__,
            '__root_path__': config.__root_path__,
            '__silent__': config.__silent__,

            'a1': 'DEFAULT 1',
            'a2': {
                'b1': [1, 2, 3],
                'b2': ['FOO 1'],
                'b3': {
                    'c1': 1,
                    'c2': 'FOO 2',
                },
            },
            'some_key_only_for_foo': True,
        }))

        config = module.Config('production', path = fixture_foo_root_path)

        self.assertEqual(config.__env__, 'production')
        self.assertTrue(isinstance(config.__env_config_file__, dict))
        self.assertTrue(config.__env__ in config.__env_config_file__.path)
        self.assertDeepEqual(deepdict(config.get()), deepdict({
            '__config_data__': config.__config_data__,
            '__config_directory_name__': config.__config_directory_name__,
            '__config_files__': config.__config_files__,
            '__config_path__': config.__config_path__,
            '__default_config_file__': config.__default_config_file__,
            '__env_config_file__': config.__env_config_file__,
            '__env_config_files__': config.__env_config_files__,
            '__env_variables_file__': config.__env_variables_file__,
            '__env__': config.__env__,
            '__files__': config.__files__,
            '__logger__': config.__logger__,
            '__path__': config.__path__,
            '__root_path__': config.__root_path__,
            '__silent__': config.__silent__,

            'a1': 'DEFAULT 1',
            'a2': {
                'b1': [1, 2, 3],
                'b2': ['PROD 1'],
                'b3': {
                    'c1': 1,
                    'c2': 'PROD 2',
                },
            },
            'some_key_only_for_prod': True,
        }))

        config = module.Config('xxx', path = fixture_foo_root_path)

        self.assertDeepEqual(deepdict(config.get()), deepdict({
            '__config_data__': config.__config_data__,
            '__config_directory_name__': config.__config_directory_name__,
            '__config_files__': config.__config_files__,
            '__config_path__': config.__config_path__,
            '__default_config_file__': config.__default_config_file__,
            '__env_config_file__': config.__env_config_file__,
            '__env_config_files__': config.__env_config_files__,
            '__env_variables_file__': config.__env_variables_file__,
            '__env__': config.__env__,
            '__files__': config.__files__,
            '__logger__': config.__logger__,
            '__path__': config.__path__,
            '__root_path__': config.__root_path__,
            '__silent__': config.__silent__,

            'a1': 'DEFAULT 1',
            'a2': {
                'b1': [1, 2, 3],
                'b2': ['foo', 'bar'],
                'b3': {
                    'c1': 1,
                    'c2': 'DEFAULT 2',
                },
            },
        }))

        env['A1'] = CUSTOM_ENV.get('A1')
        env['A2'] = CUSTOM_ENV.get('A2')
        env['C2'] = CUSTOM_ENV.get('C2')

        config = module.Config('foo', path = fixture_foo_root_path)

        self.assertDeepEqual(deepdict(config.get()), deepdict({
            '__config_data__': config.__config_data__,
            '__config_directory_name__': config.__config_directory_name__,
            '__config_files__': config.__config_files__,
            '__config_path__': config.__config_path__,
            '__default_config_file__': config.__default_config_file__,
            '__env_config_file__': config.__env_config_file__,
            '__env_config_files__': config.__env_config_files__,
            '__env_variables_file__': config.__env_variables_file__,
            '__env__': config.__env__,
            '__files__': config.__files__,
            '__logger__': config.__logger__,
            '__path__': config.__path__,
            '__root_path__': config.__root_path__,
            '__silent__': config.__silent__,

            'a1': env['A1'],
            'a2': {
                'b1': [1, 2, 3],
                'b2': ['FOO 1'],
                'b3': {
                    'c1': 1,
                    'c2': env['C2'],
                },
            },
            'some_key_only_for_foo': True,
        }))

        del env['A1']
        del env['A2']
        del env['C2']

    def test_keys(self):
        self.assertTrue(hasattr(module.Config(), 'keys'))

        try:
            del env['A1']
        except:
            pass

        try:
            del env['A2']
        except:
            pass

        try:
            del env['C2']
        except:
            pass

        config = module.Config(path = fixture_foo_root_path)

        self.assertDeepEqual(config.keys(), [
            '__config_data__',
            '__config_directory_name__',
            '__config_files__',
            '__config_path__',
            '__default_config_file__',
            '__env_config_file__',
            '__env_config_files__',
            '__env_variables_file__',
            '__env__',
            '__files__',
            '__logger__',
            '__path__',
            '__root_path__',
            '__silent__',

            'a1',
            'a2',
        ])

        config = module.Config('development', path = fixture_foo_root_path)

        self.assertDeepEqual(config.keys(), [
            '__config_data__',
            '__config_directory_name__',
            '__config_files__',
            '__config_path__',
            '__default_config_file__',
            '__env_config_file__',
            '__env_config_files__',
            '__env_variables_file__',
            '__env__',
            '__files__',
            '__logger__',
            '__path__',
            '__root_path__',
            '__silent__',

            'a1',
            'a2',
            'some_key_only_for_dev',
        ])

        config = module.Config('foo', path = fixture_foo_root_path)

        self.assertDeepEqual(config.keys(), [
            '__config_data__',
            '__config_directory_name__',
            '__config_files__',
            '__config_path__',
            '__default_config_file__',
            '__env_config_file__',
            '__env_config_files__',
            '__env_variables_file__',
            '__env__',
            '__files__',
            '__logger__',
            '__path__',
            '__root_path__',
            '__silent__',

            'a1',
            'a2',
            'some_key_only_for_foo',
        ])

        config = module.Config('production', path = fixture_foo_root_path)

        self.assertDeepEqual(config.keys(), [
            '__config_data__',
            '__config_directory_name__',
            '__config_files__',
            '__config_path__',
            '__default_config_file__',
            '__env_config_file__',
            '__env_config_files__',
            '__env_variables_file__',
            '__env__',
            '__files__',
            '__logger__',
            '__path__',
            '__root_path__',
            '__silent__',

            'a1',
            'a2',
            'some_key_only_for_prod',
        ])

        config = module.Config('xxx', path = fixture_foo_root_path)

        self.assertDeepEqual(config.keys(), [
            '__config_data__',
            '__config_directory_name__',
            '__config_files__',
            '__config_path__',
            '__default_config_file__',
            '__env_config_file__',
            '__env_config_files__',
            '__env_variables_file__',
            '__env__',
            '__files__',
            '__logger__',
            '__path__',
            '__root_path__',
            '__silent__',

            'a1',
            'a2',
        ])

        env['A1'] = CUSTOM_ENV.get('A1')
        env['A2'] = CUSTOM_ENV.get('A2')
        env['C2'] = CUSTOM_ENV.get('C2')

        config = module.Config('foo', path = fixture_foo_root_path)

        self.assertDeepEqual(config.keys(), [
            '__config_data__',
            '__config_directory_name__',
            '__config_files__',
            '__config_path__',
            '__default_config_file__',
            '__env_config_file__',
            '__env_config_files__',
            '__env_variables_file__',
            '__env__',
            '__files__',
            '__logger__',
            '__path__',
            '__root_path__',
            '__silent__',

            'a1',
            'a2',
            'some_key_only_for_foo',
        ])

        del env['A1']
        del env['A2']
        del env['C2']

    def test_values(self):
        self.assertTrue(hasattr(module.Config(), 'values'))

        try:
            del env['A1']
        except:
            pass

        try:
            del env['A2']
        except:
            pass

        try:
            del env['C2']
        except:
            pass

        config = module.Config(path = fixture_foo_root_path)

        self.assertDeepEqual(config.values(), [
            config.__config_data__,
            config.__config_directory_name__,
            config.__config_files__,
            config.__config_path__,
            config.__default_config_file__,
            config.__env_config_file__,
            config.__env_config_files__,
            config.__env_variables_file__,
            config.__env__,
            config.__files__,
            config.__logger__,
            config.__path__,
            config.__root_path__,
            config.__silent__,

            default_config_data['a1'],
            default_config_data['a2'],
        ])

        config = module.Config('development', path = fixture_foo_root_path)

        self.assertDeepEqual(config.values(), [
            config.__config_data__,
            config.__config_directory_name__,
            config.__config_files__,
            config.__config_path__,
            config.__default_config_file__,
            config.__env_config_file__,
            config.__env_config_files__,
            config.__env_variables_file__,
            config.__env__,
            config.__files__,
            config.__logger__,
            config.__path__,
            config.__root_path__,
            config.__silent__,

            default_and_development_config_data['a1'],
            default_and_development_config_data['a2'],
            default_and_development_config_data['some_key_only_for_dev'],
        ])

        config = module.Config('foo', path = fixture_foo_root_path)

        self.assertDeepEqual(config.values(), [
            config.__config_data__,
            config.__config_directory_name__,
            config.__config_files__,
            config.__config_path__,
            config.__default_config_file__,
            config.__env_config_file__,
            config.__env_config_files__,
            config.__env_variables_file__,
            config.__env__,
            config.__files__,
            config.__logger__,
            config.__path__,
            config.__root_path__,
            config.__silent__,

            default_and_foo_config_data['a1'],
            default_and_foo_config_data['a2'],
            default_and_foo_config_data['some_key_only_for_foo'],
        ])

        config = module.Config('production', path = fixture_foo_root_path)

        self.assertDeepEqual(config.values(), [
            config.__config_data__,
            config.__config_directory_name__,
            config.__config_files__,
            config.__config_path__,
            config.__default_config_file__,
            config.__env_config_file__,
            config.__env_config_files__,
            config.__env_variables_file__,
            config.__env__,
            config.__files__,
            config.__logger__,
            config.__path__,
            config.__root_path__,
            config.__silent__,

            default_and_production_config_data['a1'],
            default_and_production_config_data['a2'],
            default_and_production_config_data['some_key_only_for_prod'],
        ])

        config = module.Config('xxx', path = fixture_foo_root_path)

        self.assertDeepEqual(config.values(), [
            config.__config_data__,
            config.__config_directory_name__,
            config.__config_files__,
            config.__config_path__,
            config.__default_config_file__,
            config.__env_config_file__,
            config.__env_config_files__,
            config.__env_variables_file__,
            config.__env__,
            config.__files__,
            config.__logger__,
            config.__path__,
            config.__root_path__,
            config.__silent__,

            default_config_data['a1'],
            default_config_data['a2'],
        ])

        env['A1'] = CUSTOM_ENV.get('A1')
        env['A2'] = CUSTOM_ENV.get('A2')
        env['C2'] = CUSTOM_ENV.get('C2')

        config = module.Config('foo', path = fixture_foo_root_path)

        self.assertDeepEqual(config.values(), [
            config.__config_data__,
            config.__config_directory_name__,
            config.__config_files__,
            config.__config_path__,
            config.__default_config_file__,
            config.__env_config_file__,
            config.__env_config_files__,
            config.__env_variables_file__,
            config.__env__,
            config.__files__,
            config.__logger__,
            config.__path__,
            config.__root_path__,
            config.__silent__,

            env['A1'],
            Config.merge(
                default_and_foo_config_data['a2'],
                {
                    'b3': {
                        'c2': env['C2']
                    },
                },
            ),
            default_and_foo_config_data['some_key_only_for_foo'],
        ])

        del env['A1']
        del env['A2']
        del env['C2']

    def test_has(self):
        self.assertTrue(hasattr(module.Config(), 'has'))

        config = module.Config(path = fixture_foo_root_path)

        self.assertDeepEqual(config.has('a1'), True)
        self.assertDeepEqual(config.has('a2'), True)
        self.assertDeepEqual(config.has('some_key_only_for_dev'), False)
        self.assertDeepEqual(config.has('some_key_only_for_foo'), False)
        self.assertDeepEqual(config.has('some_key_only_for_prod'), False)
        self.assertDeepEqual(config.has('xxx'), False)

        config = module.Config('development', path = fixture_foo_root_path)

        self.assertDeepEqual(config.has('a1'), True)
        self.assertDeepEqual(config.has('a2'), True)
        self.assertDeepEqual(config.has('some_key_only_for_dev'), True)
        self.assertDeepEqual(config.has('some_key_only_for_foo'), False)
        self.assertDeepEqual(config.has('some_key_only_for_prod'), False)
        self.assertDeepEqual(config.has('xxx'), False)

        config = module.Config('foo', path = fixture_foo_root_path)

        self.assertDeepEqual(config.has('a1'), True)
        self.assertDeepEqual(config.has('a2'), True)
        self.assertDeepEqual(config.has('some_key_only_for_dev'), False)
        self.assertDeepEqual(config.has('some_key_only_for_foo'), True)
        self.assertDeepEqual(config.has('some_key_only_for_prod'), False)
        self.assertDeepEqual(config.has('xxx'), False)

        config = module.Config('production', path = fixture_foo_root_path)

        self.assertDeepEqual(config.has('a1'), True)
        self.assertDeepEqual(config.has('a2'), True)
        self.assertDeepEqual(config.has('some_key_only_for_dev'), False)
        self.assertDeepEqual(config.has('some_key_only_for_foo'), False)
        self.assertDeepEqual(config.has('some_key_only_for_prod'), True)
        self.assertDeepEqual(config.has('xxx'), False)

        config = module.Config('xxx', path = fixture_foo_root_path)

        self.assertDeepEqual(config.has('a1'), True)
        self.assertDeepEqual(config.has('a2'), True)
        self.assertDeepEqual(config.has('some_key_only_for_dev'), False)
        self.assertDeepEqual(config.has('some_key_only_for_foo'), False)
        self.assertDeepEqual(config.has('some_key_only_for_prod'), False)
        self.assertDeepEqual(config.has('xxx'), False)

        env['A1'] = CUSTOM_ENV.get('A1')
        env['A2'] = CUSTOM_ENV.get('A2')
        env['C2'] = CUSTOM_ENV.get('C2')

        config = module.Config('foo', path = fixture_foo_root_path)

        self.assertDeepEqual(config.has('a1'), True)
        self.assertDeepEqual(config.has('a2'), True)
        self.assertDeepEqual(config.has('some_key_only_for_dev'), False)
        self.assertDeepEqual(config.has('some_key_only_for_foo'), True)
        self.assertDeepEqual(config.has('some_key_only_for_prod'), False)
        self.assertDeepEqual(config.has('xxx'), False)

        del env['A1']
        del env['A2']
        del env['C2']

    def test_class_create(self):
        try:
            del env['ENV']
        except:
            pass

        self.assertEqual(env.get('ENV', None), None)

        try:
            del env['A1']
        except:
            pass

        try:
            del env['A2']
        except:
            pass

        try:
            del env['C2']
        except:
            pass

        config = module.Config.create(path = fixture_foo_root_path)

        self.assertEqual(config.__env__, None)
        self.assertDeepEqual(deepdict(config), deepdict({
            '__config_data__': config.__config_data__,
            '__config_directory_name__': config.__config_directory_name__,
            '__config_files__': config.__config_files__,
            '__config_path__': config.__config_path__,
            '__default_config_file__': config.__default_config_file__,
            '__env_config_file__': config.__env_config_file__,
            '__env_config_files__': config.__env_config_files__,
            '__env_variables_file__': config.__env_variables_file__,
            '__env__': config.__env__,
            '__files__': config.__files__,
            '__logger__': config.__logger__,
            '__path__': config.__path__,
            '__root_path__': config.__root_path__,
            '__silent__': config.__silent__,

            'a1': 'DEFAULT 1',
            'a2': {
                'b1': [1, 2, 3],
                'b2': ['foo', 'bar'],
                'b3': {
                    'c1': 1,
                    'c2': 'DEFAULT 2',
                },
            },
        }))

        env['ENV'] = 'development'

        self.assertEqual(env.get('ENV', None), 'development')

        config = module.Config.create(path = fixture_foo_root_path)

        self.assertEqual(config.__env__, 'development')
        self.assertDeepEqual(deepdict(config), deepdict({
            '__config_data__': config.__config_data__,
            '__config_directory_name__': config.__config_directory_name__,
            '__config_files__': config.__config_files__,
            '__config_path__': config.__config_path__,
            '__default_config_file__': config.__default_config_file__,
            '__env_config_file__': config.__env_config_file__,
            '__env_config_files__': config.__env_config_files__,
            '__env_variables_file__': config.__env_variables_file__,
            '__env__': config.__env__,
            '__files__': config.__files__,
            '__logger__': config.__logger__,
            '__path__': config.__path__,
            '__root_path__': config.__root_path__,
            '__silent__': config.__silent__,

            'a1': 'DEFAULT 1',
            'a2': {
                'b1': [1, 2, 3],
                'b2': ['DEV 1'],
                'b3': {
                    'c1': 1,
                    'c2': 'DEV 2',
                },
            },
            'some_key_only_for_dev': True,
        }))

        env['ENV'] = 'foo'

        self.assertEqual(env.get('ENV', None), 'foo')

        config = module.Config.create(path = fixture_foo_root_path)

        self.assertEqual(config.__env__, 'foo')
        self.assertDeepEqual(deepdict(config), deepdict({
            '__config_data__': config.__config_data__,
            '__config_directory_name__': config.__config_directory_name__,
            '__config_files__': config.__config_files__,
            '__config_path__': config.__config_path__,
            '__default_config_file__': config.__default_config_file__,
            '__env_config_file__': config.__env_config_file__,
            '__env_config_files__': config.__env_config_files__,
            '__env_variables_file__': config.__env_variables_file__,
            '__env__': config.__env__,
            '__files__': config.__files__,
            '__logger__': config.__logger__,
            '__path__': config.__path__,
            '__root_path__': config.__root_path__,
            '__silent__': config.__silent__,

            'a1': 'DEFAULT 1',
            'a2': {
                'b1': [1, 2, 3],
                'b2': ['FOO 1'],
                'b3': {
                    'c1': 1,
                    'c2': 'FOO 2',
                },
            },
            'some_key_only_for_foo': True,
        }))

        env['ENV'] = 'production'

        self.assertEqual(env.get('ENV', None), 'production')

        config = module.Config.create(path = fixture_foo_root_path)

        self.assertEqual(config.__env__, 'production')
        self.assertDeepEqual(deepdict(config), deepdict({
            '__config_data__': config.__config_data__,
            '__config_directory_name__': config.__config_directory_name__,
            '__config_files__': config.__config_files__,
            '__config_path__': config.__config_path__,
            '__default_config_file__': config.__default_config_file__,
            '__env_config_file__': config.__env_config_file__,
            '__env_config_files__': config.__env_config_files__,
            '__env_variables_file__': config.__env_variables_file__,
            '__env__': config.__env__,
            '__files__': config.__files__,
            '__logger__': config.__logger__,
            '__path__': config.__path__,
            '__root_path__': config.__root_path__,
            '__silent__': config.__silent__,

            'a1': 'DEFAULT 1',
            'a2': {
                'b1': [1, 2, 3],
                'b2': ['PROD 1'],
                'b3': {
                    'c1': 1,
                    'c2': 'PROD 2',
                },
            },
            'some_key_only_for_prod': True,
        }))

        env['ENV'] = 'xxx'

        self.assertEqual(env.get('ENV', None), 'xxx')

        config = module.Config.create(path = fixture_foo_root_path)

        self.assertEqual(config.__env__, 'xxx')
        self.assertDeepEqual(deepdict(config), deepdict({
            '__config_data__': config.__config_data__,
            '__config_directory_name__': config.__config_directory_name__,
            '__config_files__': config.__config_files__,
            '__config_path__': config.__config_path__,
            '__default_config_file__': config.__default_config_file__,
            '__env_config_file__': config.__env_config_file__,
            '__env_config_files__': config.__env_config_files__,
            '__env_variables_file__': config.__env_variables_file__,
            '__env__': config.__env__,
            '__files__': config.__files__,
            '__logger__': config.__logger__,
            '__path__': config.__path__,
            '__root_path__': config.__root_path__,
            '__silent__': config.__silent__,

            'a1': 'DEFAULT 1',
            'a2': {
                'b1': [1, 2, 3],
                'b2': ['foo', 'bar'],
                'b3': {
                    'c1': 1,
                    'c2': 'DEFAULT 2',
                },
            },
        }))

        env['A1'] = CUSTOM_ENV.get('A1')
        env['A2'] = CUSTOM_ENV.get('A2')
        env['C2'] = CUSTOM_ENV.get('C2')

        env['ENV'] = 'foo'

        self.assertEqual(env.get('ENV', None), 'foo')

        config = module.Config.create(path = fixture_foo_root_path)

        self.assertEqual(config.__env__, 'foo')
        self.assertDeepEqual(deepdict(config), deepdict({
            '__config_data__': config.__config_data__,
            '__config_directory_name__': config.__config_directory_name__,
            '__config_files__': config.__config_files__,
            '__config_path__': config.__config_path__,
            '__default_config_file__': config.__default_config_file__,
            '__env_config_file__': config.__env_config_file__,
            '__env_config_files__': config.__env_config_files__,
            '__env_variables_file__': config.__env_variables_file__,
            '__env__': config.__env__,
            '__files__': config.__files__,
            '__logger__': config.__logger__,
            '__path__': config.__path__,
            '__root_path__': config.__root_path__,
            '__silent__': config.__silent__,

            'a1': env['A1'],
            'a2': {
                'b1': [1, 2, 3],
                'b2': ['FOO 1'],
                'b3': {
                    'c1': 1,
                    'c2': env['C2'],
                },
            },
            'some_key_only_for_foo': True,
        }))

        del env['A1']
        del env['A2']
        del env['C2']

    def test_config_attribute_get(self):
        pass

    def test_config_attribute_set(self):
        pass

    def test_config_attribute_del(self):
        pass

    def test_config_item_get(self):
        pass

    def test_config_item_set(self):
        pass

    def test_config_item_del(self):
        pass


# =========================================
#       MAIN
# --------------------------------------

if __name__ == '__main__':
    helper.run(TestCase)
