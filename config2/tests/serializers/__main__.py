
# =========================================
#       DEPS
# --------------------------------------

from easypackage.syspath import syspath

syspath()

from config2.tests import helper


# =========================================
#       RUN
# --------------------------------------

helper.run(__file__)
