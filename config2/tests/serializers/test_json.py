
# =========================================
#       DEPS
# --------------------------------------

import types

from os import path

import rootpath

rootpath.append()

from config2.tests import helper
from config2.compat import string_types

from config2.serializers import json_ as json


# =========================================
#       TEST
# --------------------------------------

class TestCase(helper.TestCase):

    def test__import(self):
        self.assertModule(json)

    def test_json_pack(self):
        self.assertEqual(type(json.pack), types.FunctionType)

        data = {'foo': [1, 2, 3]}

        with self.assertNotRaises(Exception):
            result = json.pack(data)

        self.assertTrue(isinstance(result, string_types))
        self.assertEqual(result.replace('\n', '').replace('    ', '').replace(', ', ','), '{"foo": [1, 2, 3]}'.replace(', ', ','))

        data = None

        with self.assertNotRaises(Exception):
            result = json.pack(data)

        self.assertEqual(result, 'null')

    def test_json_unpack(self):
        self.assertEqual(type(json.pack), types.FunctionType)

        data = '{"foo":[1,2,3]}'

        with self.assertNotRaises(Exception):
            result = json.unpack(data)

        self.assertTrue(isinstance(result, (dict)))
        self.assertEqual(result, {u'foo': [1, 2, 3]})

        data = 'null'

        with self.assertNotRaises(Exception):
            result = json.unpack(data)

        self.assertEqual(result, None)

    def test_json_test(self):
        self.assertEqual(type(json.test), types.FunctionType)

        data = None

        with self.assertNotRaises(Exception):
            result = json.test(data)

        self.assertEqual(result, False)

        data = 'eyJmb28iOiBbMSwgMiwgM119'

        with self.assertNotRaises(Exception):
            result = json.test(data)

        self.assertEqual(result, False)

        data = {}

        with self.assertNotRaises(Exception):
            result = json.test(data)

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
            result = json.test(data)

        self.assertEqual(result, False)

        data = {
            'a1.b1.c1': [1, 2, 3],
            'a1.b1.c2': 100,
            'a2': True,
        }

        with self.assertNotRaises(Exception):
            result = json.test(data)

        self.assertEqual(result, False)

        data = '{"foo":[1,2,3]}'

        with self.assertNotRaises(Exception):
            result = json.test(data)

        self.assertEqual(result, True)

        data = '[{"foo":[1,2,3]}]'

        with self.assertNotRaises(Exception):
            result = json.test(data)

        self.assertEqual(result, True)

        data = '\x81\xa3foo\x93\x01\x02\x03'

        with self.assertNotRaises(Exception):
            result = json.test(data)

        self.assertEqual(result, False)

        data = 'foo:\n- 1\n- 2\n- 3'

        with self.assertNotRaises(Exception):
            result = json.test(data)

        self.assertEqual(result, False)


# =========================================
#       MAIN
# --------------------------------------

if __name__ == '__main__':
    helper.run(TestCase)
