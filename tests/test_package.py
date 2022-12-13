import os
import unittest
from packaging import version

from os.path import join as pjoin
from pathlib import Path
import pyerk as p
from ipydex import IPS, activate_ips_on_exception  # noqa


if os.environ.get("IPYDEX_AIOE") == "true":
    activate_ips_on_exception()


PACKAGE_ROOT_PATH = Path(__file__).parent.parent.absolute().as_posix()
ma = p.erkloader.load_mod_from_path(pjoin(PACKAGE_ROOT_PATH, "math1.py"), prefix="ma")


class Test_01_math(unittest.TestCase):

    def setUp(self):
        p.start_mod(ma.__URI__)

    def tearDown(self):
        p.end_mod()

    def test_a00_ensure_version(self):
        self.assertGreaterEqual(version.parse(p.__version__), version.parse("0.6.4"))

    def test_a01_column_stack(self):
        cs1: p.Item = p.instance_of(ma.I3237["column stack"])
        A = p.instance_of(ma.I9904["matrix"])
        b = p.instance_of(ma.I9904["matrix"])

        cs1.set_mutliple_relations(ma.R7490["has sequence element"], (A, b))

        rels = cs1.get_relations("ma__R7490__has_sequence_element", return_obj=True)
        self.assertEqual(rels, [A, b])

        # construct a situation like in the Kalman controlability matrix: Q = (b, A*b, A^2*b, ...)
        cs2: p.Item = p.instance_of(ma.I3237["column stack"])

        # arbitrary range
        with ma.IntegerRangeElement(start=0, stop=9) as i:
            prod = ma.I5177["matmul"](ma.I1474["matpow"](A, i), b)
            cs2.set_relation("ma__R7490__has_sequence_element", prod)
