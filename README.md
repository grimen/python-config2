
# Config2 [![Build Status](https://travis-ci.com/grimen/python-config2.svg?branch=master)](https://travis-ci.com/grimen/python-config2) [![PyPI version](https://badge.fury.io/py/config2.svg)](https://badge.fury.io/py/config2)

*Python environment configuration simplified.*


## Introduction

**Config2** (for Python) - which is highly inspired by [`node-config`](https://github.com/lorenwest/node-config) - organizes hierarchical configurations for your app deployments.

It lets you define a set of default parameters, and extend them for different deployment environments (development, qa, staging, production, etc.).

Configurations are stored in **configuration files** within your application, and can be overridden and extended by **environment variables**, **command line parameters**, or **external sources**.

This gives your application a consistent configuration interface shared among a growing list of npm modules also using node-config.

**NOTE:** This project is more or less in pair with [`node-config`](https://github.com/lorenwest/node-config) implementation, with exception for some fluff that could be considered too much magic such as deployment specific *multi-instance deployments* which I so far haven't found any good motivation for, and some other questionable advanced features mentioned in the wiki pages.


## Project Guidelines

...based on [`node-config`](https://github.com/lorenwest/node-config) project guidelines:

- *Simple* - Get started fast
- ~~*Powerful* - For multi-node enterprise deployment~~ - excluded because [with power comes responsability](https://en.wikipedia.org/wiki/Principle_of_least_astonishment)
- *Flexible* - Supporting multiple config file formats
- *Lightweight* - Small file and memory footprint
- *Predictable* - Well tested foundation for module and app developers


## Install

Install using **pip**:

```sh
$ pip install config2
```


## Use

**1.** Assuming we have a **python application** project...

```
some_project
└── app.py
```

`app.py` - some app making serious **&#36;&#36;&#36;**

```python
# business logic
print('$$$')
```


**2.** Let's add some environment specific **config files**...

```
some_project
└── config
    ├── default.yml
    ├── development.yml
    ├── foo.yml
    └── production.yml
└── app.py
```

`default.yml` - with some bogus nested settings shared for all environments (defaults)

```yaml
a1: DEFAULT 1
a2:
    b1: [1, 2, 3]
    b2:
        -   foo
        -   bar
    b3:
        c1: 1
        c2: "DEFAULT 2"
```

`development.yml` - with some bogus nested settings overriden for `development` environment (overriden)

```yaml
a2:
    b2:
        -   DEV 1
    b3:
        c2: "DEV 2"
some_key_only_for_dev: true
```

`foo.yml` - with some bogus nested settings overriden for `foo` environment (overriden)

```yaml
a2:
    b2:
        -   FOO 1
    b3:
        c2: "FOO 2"
some_key_only_for_foo: true
```

`production.yml` - with some bogus nested settings overriden for `production` environment (overriden)

```yaml
a2:
    b2:
        -   PROD 1
    b3:
        c2: "PROD 2"
some_key_only_for_prod: true
```


**3.** Let's now **run the app** using **various environments**...

`$ python app.py`

```python
from config2.config import config

config.get_env() # => None
config.get() # => {'a1': 'DEFAULT 1', 'a2': {'b1': [1, 2, 3], 'b2': ['foo', 'bar'], 'b3': {'c1': 1, 'c2': 'DEFAULT 2'}}}

config.a1 # => 'DEFAULT 1'
config.a2 # => {'b1': [1, 2, 3], 'b2': ['foo', 'bar'], 'b3': {'c1': 1, 'c2': 'DEFAULT 2'}}
config.a2.b3.c2 # => 'DEFAULT 2'

print('$$$')
```

`$ ENV=development python app.py`

```python
from config2.config import config

config.get_env() # => 'development'
config.get() # => {'a1': 'DEFAULT 1', 'a2': {'b1': [1, 2, 3], 'b2': ['DEV 1'], 'b3': {'c1': 1, 'c2': 'DEV 2'}}, 'some_key_only_for_dev': True}

config.a1 # => 'DEFAULT 1'
config.a2 # => {'b1': [1, 2, 3], 'b2': ['DEV 1'], 'b3': {'c1': 1, 'c2': 'DEV 2'}}
config.a2.b3.c2 # => 'DEV was here 2'

config.some_key_only_for_dev # => True

config.some_key_only_for_foo # => AttributeError
config.some_key_only_for_prod # => AttributeError

print('$$$')
```

`$ ENV=foo python app.py`

```python
from config2.config import config

config.get_env() # => 'foo'
config.get() # => {'a1': 'DEFAULT 1', 'a2': {'b1': [1, 2, 3], 'b2': ['FOO 1'], 'b3': {'c1': 1, 'c2': 'FOO 2'}}, 'some_key_only_for_foo': True}

config.a1 # => 'DEFAULT 1'
config.a2 # => {'b1': [1, 2, 3], 'b2': ['FOO 1'], 'b3': {'c1': 1, 'c2': 'FOO 2'}}
config.a2.b3.c2 # => 'FOO was here 2'

config.key_only_for_foo # => True

config.some_key_only_for_dev # => AttributeError
config.some_key_only_for_prod # => AttributeError

print('$$$')
```

`$ ENV=production python app.py`

```python
from config2.config import config

config.get_env() # => 'production'
config.get() # => {'a1': 'DEFAULT 1', 'a2': {'b1': [1, 2, 3], 'b2': ['PROD 1'], 'b3': {'c1': 1, 'c2': 'PROD 2'}}, 'some_key_only_for_foo': True}

config.a1 # => 'DEFAULT 1'
config.a2 # => {'b1': [1, 2, 3], 'b2': ['PROD 1'], 'b3': {'c1': 1, 'c2': 'PROD 2'}}
config.a2.b3.c2 # => 'PROD was here 2'

config.some_key_only_for_prod # => True

config.some_key_only_for_dev # => AttributeError
config.some_key_only_for_foo # => AttributeError

print('$$$')
```

etc.


**4.** Optionally, let's now introduce custom **config environment variables**...


```
some_project
└── config
    ├── custom-environment-variables.yml
    ├── default.yml
    ├── development.yml
    ├── foo.yml
    └── production.yml
└── app.py
```

`custom-environment-variables.yml` - with mappings of config keys to environment variables

```yaml
a1: A1
a2:
    b3:
        c2: C2
```

**5.** Let's now **run the app** using **custom environment variables** to override config...

`$ A1=x C2=y python app.py`

```python
from config2.config import config

config.get_env() # => None
config.get() # => {'a1': 'x', 'a2': {'b1': [1, 2, 3], 'b2': ['foo', 'bar'], 'b3': {'c1': 1, 'c2': 'y'}}}

config.a1 # => 'x'
config.a2 # => {'b1': [1, 2, 3], 'b2': ['foo', 'bar'], 'b3': {'c1': 1, 'c2': 'y'}}
config.a2.b3.c2 # => 'y'

print('$$$')
```


## Test

Clone down source code:

```sh
$ make install
```

Run **colorful tests**, with only native environment (dependency sandboxing up to you):

```sh
$ make test
```

Run **less colorful tests**, with **multi-environment** (using **tox**):

```sh
$ make test-tox
```


## About

This project was mainly initiated - in lack of existing alternatives - to be used at our work at **[Markable.ai](https://markable.ai)** to have common code conventions between various programming environments where **Python** (research, CV, AI) and **Node.js** (I/O, APIs, UIs, scripts) currently are most used.


## License

Released under the MIT license.
