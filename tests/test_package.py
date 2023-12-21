import os
import unittest
from packaging import version

from os.path import join as pjoin
from pathlib import Path
import pyirk as p
from ipydex import IPS, activate_ips_on_exception  # noqa


if os.environ.get("IPYDEX_AIOE") == "true":
    activate_ips_on_exception()

if not os.environ.get("PYIRK_DISABLE_CONSISTENCY_CHECKING", "").lower() == "true":
    p.cc.enable_consistency_checking()

PACKAGE_ROOT_PATH = Path(__file__).parent.parent.absolute().as_posix()
ag = p.irkloader.load_mod_from_path(pjoin(PACKAGE_ROOT_PATH, "agents1.py"), prefix="ag")
ma = p.irkloader.load_mod_from_path(pjoin(PACKAGE_ROOT_PATH, "math1.py"), prefix="ma", reuse_loaded=True)
ct = p.irkloader.load_mod_from_path(pjoin(PACKAGE_ROOT_PATH, "control_theory1.py"), prefix="ct", reuse_loaded=True)


class Test_01_basics(unittest.TestCase):
    def test_a00__ensure_version(self):
        self.assertGreaterEqual(version.parse(p.__version__), version.parse("0.11.2"))


class Test_02_math(unittest.TestCase):
    def setUp(self):
        p.start_mod(ma.__URI__)

    def tearDown(self):
        p.end_mod()

    def test_c01__column_stack(self):

        # create some matrices which will be stacked later
        A = p.instance_of(ma.I9904["matrix"])
        b = p.instance_of(ma.I9904["matrix"])

        # different ways to define column stacks:
        colstack1: p.Item = p.instance_of(ma.I3237["column stack"])

        # add the elements of the column-stack element by element
        colstack1.set_relation(ma.R7490["has sequence element"], A)
        colstack1.set_relation(ma.R7490["has sequence element"], b)

        # check
        rels = colstack1.get_relations("ma__R7490__has_sequence_element", return_obj=True)
        self.assertEqual(rels, [A, b])

        # add the elements of the column-stack all at once
        colstack2: p.Item = p.instance_of(ma.I3237["column stack"])
        colstack2.set_multiple_relations(ma.R7490["has sequence element"], (A, b))

        # check
        rels = colstack2.get_relations("ma__R7490__has_sequence_element", return_obj=True)
        self.assertEqual(rels, [A, b])

        # construct a situation like in the Kalman controllability matrix: Q = (b, A*b, A^2*b, ...)
        colstack3: p.Item = p.instance_of(ma.I3237["column stack"])

        # arbitrary range (here from 0 to 24)
        with ma.IntegerRangeElement(start=0, stop=24) as i:
            prod = ma.I5177["matmul"](ma.I1474["matpow"](A, i), b)
            colstack3.set_relation("ma__R7490__has_sequence_element", prod)

    def test_c02__eigenvalues(self):
        A = p.instance_of(ma.I9906["square matrix"])
        s = p.instance_of(ma.I5030["variable"])

        # construct sI - A
        M = ma.I6324["canonical first order monic polynomial matrix"](A, s)

        # TODO: __automate_typing__
        M.R30__is_secondary_instance_of = ma.I9906["square matrix"]

        self.assertTrue(M.R4__is_instance_of, ma.I1935["polynomial matrix"])
        self.assertTrue(M.ma__R8736__depends_polynomially_on, s)

        d = ma.I5359["determinant"](M)
        self.assertTrue(d.ma__R8736__depends_polynomially_on, s)

    def test_c04_symbolic_formula1(self):

        t = p.instance_of(ma.I2917["planar triangle"])
        sides = ma.I9148["polygon sides ordered by length"](t)
        a, b, c = sides.R39__has_element

        la, lb, lc = ma.items_to_symbols(a, b, c, relation=ma.R2495["has length"])
        symbolic_sum = la + lb + lc

        se2ge = ma.symbolic_expression_to_graph_expression

        sum_item = se2ge(symbolic_sum)
        self.assertEqual(sum_item.get_arguments()[0].get_arguments(), [a.R2495__has_length, b.R2495__has_length])
        self.assertEqual(sum_item.get_arguments()[1], c.R2495__has_length)
        self.assertEqual(sum_item.R4__is_instance_of, ma.I6043["sum"])

        symbolic_prod = la*lb
        prod_item = se2ge(symbolic_prod)
        self.assertEqual(prod_item.get_arguments(), [a.R2495__has_length, b.R2495__has_length])
        self.assertEqual(prod_item.R4__is_instance_of, ma.I5916["product"])

        square = se2ge(la**2)
        self.assertEqual(square.R4__is_instance_of, ma.I5916["product"])
        self.assertEqual(square.get_arguments(), [a.R2495__has_length, a.R2495__has_length])

        square_sum = se2ge(la**2 + lb**2)
        self.assertEqual(square_sum.R4__is_instance_of, ma.I6043["sum"])
        self.assertEqual(square_sum.get_arguments()[0].R4__is_instance_of, ma.I5916["product"])
        self.assertEqual(square_sum.get_arguments()[1].R4__is_instance_of, ma.I5916["product"])
        self.assertEqual(square_sum.get_arguments()[1].get_arguments(), [b.R2495__has_length, b.R2495__has_length])

    def test_c05__cc_matrix_dimensions(self):

        I5073 = ma.I5073

        # test the rule which produces a I48["constraint violation"] instance
        res = p.ruleengine.apply_semantic_rule(I5073, ma.__URI__)

        self.assertGreaterEqual(len(res.new_statements), 1)
        self.assertEqual(len(res.new_entities), 1)

        cvio, = ma.failed_multiplication.R74__has_constraint_violation
        self.assertEqual(cvio.R76__has_associated_rule, I5073)
        self.assertEqual(cvio.R4__is_instance_of, p.I48["constraint violation"])

        # self.assertEqual(A2B.R74__has_constraint_violation, [])

        # test propagation of matrix dimensions in the product: x.T * P * x

        itm = ct.I2613["theorem for Lyapunov functions for linear systems"]
        stm = itm.scp__assertion.get_inv_relations("R20", return_subj=True)[3]
        self.assertTrue(isinstance(stm, p.Statement))
        res = stm.object
        self.assertEqual(res.R4__is_instance_of, ma.I1063["scalar function"])

        # get the matmul-result
        xTPx = res.R36__has_argument_tuple.R39__has_element[0]
        xTP, x = xTPx.R36__has_argument_tuple.R39__has_element
        xT, P = xTP.R36__has_argument_tuple.R39__has_element

        x_vect = x.R36__has_argument_tuple.R39__has_element[0]

        n = P.R5938__has_row_number
        self.assertEqual(str(n.R1__has_label), "n")
        self.assertEqual(P.R5939__has_column_number, n)
        self.assertEqual(x_vect.R3326__has_dimension, n)
        self.assertEqual(x.R5938__has_row_number, n)
        self.assertEqual(x.R5939__has_column_number, 1)

        self.assertEqual(xT.R5938__has_row_number, 1)
        self.assertEqual(xT.R5939__has_column_number, n)


class Test_02_control_theory(unittest.TestCase):
    def test_b01__test_multilinguality(self):
        ct.I5290["reference value"].R1__has_label__de == "Sollwert"@p.de


class Test_03_agents(unittest.TestCase):
    def test_c03__publications(self):
        x = ag.I7558["2002_Khalil"]
        self.assertEqual(x.ag__R8433__has_authors[0], ag.I9700["Hassan Khalil"])

        segment = ag.get_source_segment(ag.I7558["2002_Khalil"], "Section 4.1")
        self.assertEqual(segment.ag__R8437__has_segment_specification, ["Section 4.1"])

        segment2 = ag.get_source_segment(ag.I7558["2002_Khalil"], "Section 4.1")
        self.assertTrue(segment2 is segment)
