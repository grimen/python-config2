
import rootpath

rootpath.append()

from os import environ as env

env['PYTHON_ENV'] = 'development'

from config2.config import config

# print(config)

assert config.get_env() == 'development' # => 'development'
assert config.get() # => {'a1': 'DEFAULT 1', 'a2': {'b1': [1, 2, 3], 'b2': ['DEV 1'], 'b3': {'c1': 1, 'c2': 'DEV 2'}}, 'some_key_only_for_dev': True}

print(config.a1) # => 'DEFAULT 1'
print(config.a2) # => {'b1': [1, 2, 3], 'b2': ['DEV 1'], 'b3': {'c1': 1, 'c2': 'DEV 2'}}
print(config.a2.b3.c2) # => 'DEV was here 2'

try:
    print('config.some_key_only_for_dev', config.some_key_only_for_dev)
except Exception as error:
    print('config.some_key_only_for_dev', error)

try:
    print('config.some_key_only_for_foo', config.some_key_only_for_foo)
except Exception as error:
    print('config.some_key_only_for_foo', error)

try:
    print('config.some_key_only_for_prod', config.some_key_only_for_prod)
except Exception as error:
    print('config.some_key_only_for_foo', error)

print('$$$')
