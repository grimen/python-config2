
# =========================================
#       DEPS
# --------------------------------------

from easypackage.syspath import syspath

syspath()

from config2.tests import helper

import config2
import config2.config as module

Config = module.Config


# =========================================
#       TEST
# --------------------------------------

class TestCase(helper.TestCase):

    def test__import(self):
        self.assertModule(module)

    def test_create(self):
        config = module.Config()

        self.assertTrue(isinstance(config, dict))


# =========================================
#       MAIN
# --------------------------------------

if __name__ == '__main__':
    helper.run(TestCase)
