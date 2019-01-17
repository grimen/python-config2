
# =========================================
#       DEPS
# --------------------------------------

import types

from os import path

import rootpath

rootpath.append()

from config2.tests import helper
from config2.compat import string_types

from config2.serializers import yaml_ as yaml


# =========================================
#       TEST
# --------------------------------------

class TestCase(helper.TestCase):

    def test__import(self):
        self.assertModule(yaml)

    def test_yaml_pack(self):
        self.assertEqual(type(yaml.pack), types.FunctionType)

        data = {'foo': [1, 2, 3]}

        with self.assertNotRaises(Exception):
            result = yaml.pack(data)

        self.assertEqual(result, 'foo:\n- 1\n- 2\n- 3')

        data = None

        with self.assertNotRaises(Exception):
            result = yaml.pack(data)

        self.assertEqual(result, '')

    def test_yaml_unpack(self):
        self.assertEqual(type(yaml.pack), types.FunctionType)

        data = 'foo:\n- 1\n- 2\n- 3'

        with self.assertNotRaises(Exception):
            result = yaml.unpack(data)

        self.assertEqual(result, {u'foo': [1, 2, 3]})

        data = 'null'

        with self.assertNotRaises(Exception):
            result = yaml.unpack(data)

        self.assertEqual(result, None)

    def test_yaml_test(self):
        self.assertEqual(type(yaml.test), types.FunctionType)

        data = None

        with self.assertNotRaises(Exception):
            result = yaml.test(data)

        self.assertEqual(result, False)

        data = 'eyJmb28iOiBbMSwgMiwgM119'

        with self.assertNotRaises(Exception):
            result = yaml.test(data)

        self.assertEqual(result, False)

        data = {}

        with self.assertNotRaises(Exception):
            result = yaml.test(data)

        self.assertEqual(result, False)

        data = {
            'a1': {
                'b1': {
                    'c1': [1, 2, 3],
                    'c2': 100
                }
            },
            'a2': True,
        }

        with self.assertNotRaises(Exception):
            result = yaml.test(data)

        self.assertEqual(result, False)

        data = {
            'a1.b1.c1': [1, 2, 3],
            'a1.b1.c2': 100,
            'a2': True,
        }

        with self.assertNotRaises(Exception):
            result = yaml.test(data)

        self.assertEqual(result, False)

        data = '{"foo":[1,2,3]}'

        with self.assertNotRaises(Exception):
            result = yaml.test(data)

        self.assertEqual(result, False)

        data = '[{"foo":[1,2,3]}]'

        with self.assertNotRaises(Exception):
            result = yaml.test(data)

        self.assertEqual(result, False)

        data = '\x81\xa3foo\x93\x01\x02\x03'

        with self.assertNotRaises(Exception):
            result = yaml.test(data)

        self.assertEqual(result, False)

        data = 'foo:\n- 1\n- 2\n- 3'

        with self.assertNotRaises(Exception):
            result = yaml.test(data)

        self.assertEqual(result, True)


# =========================================
#       MAIN
# --------------------------------------

if __name__ == '__main__':
    helper.run(TestCase)
