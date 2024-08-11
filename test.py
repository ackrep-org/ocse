import os
import unittest
from packaging import version
import itertools

from os.path import join as pjoin
from pathlib import Path
import pyirk as p
from ipydex import IPS, activate_ips_on_exception  # noqa


if os.environ.get("IPYDEX_AIOE") == "true":
    activate_ips_on_exception()

if not os.environ.get("PYIRK_DISABLE_CONSISTENCY_CHECKING", "").lower() == "true":
    p.cc.enable_consistency_checking()

PACKAGE_ROOT_PATH = Path(__file__).parent.absolute().as_posix()
ag = p.irkloader.load_mod_from_path(pjoin(PACKAGE_ROOT_PATH, "agents1.py"), prefix="ag")
ma = p.irkloader.load_mod_from_path(pjoin(PACKAGE_ROOT_PATH, "math1.py"), prefix="ma", reuse_loaded=True)
ct = p.irkloader.load_mod_from_path(pjoin(PACKAGE_ROOT_PATH, "control_theory1.py"), prefix="ct", reuse_loaded=True)


theorems = p.get_all_instances_of(p.I14["mathematical proposition"])
systems = p.get_all_instances_of(ct.I7641["general system model"])

def cond_func(sys, rep, th):
    # Note: most sys items here will be the systems created in the scope of a theorem. matching those doesnt make sense.
    # they have to be filtered out first
    # sys is from a setting scope:
    if sys.get_relations("R20"):
        if sys.get_relations("R20", return_obj=True)[0].R64 == "SETTING":
            return False


    scopes = th.get_inv_relations("R21",return_subj=True)
    set, pre, ass = None, None, None
    for scope in scopes:
        match scope.R64:
            case "SETTING":
                set = scope
            case "PREMISE":
                pre = scope
            case "ASSERTION":
                ass = scope

    if set is None:
        return False

    setting_items = set.get_inv_relations("R20", return_subj=True)
    systh = [i for i in setting_items if isinstance(i, p.Item) and p.is_instance_of(i, ct.I7641["general system model"])]
    if len(systh) != 1:
        return False
    systh = systh[0]

    repth = [i for i in setting_items if isinstance(i, p.Item) and p.is_instance_of(i, ct.I2928["general model representation"])]
    if len(repth) != 1:
        return False
    repth = repth[0]

    cond = True
    # for each statement regarding sys in theorem
    for statement in sum(systh.get_relations().values(), []):
        # take only the property relations for now
        if "property" in statement.relation.R1:
            rel_uri = statement.relation.uri
            obj = statement.object
            # make sure the systems has the same or more restrictive property as sys in th
            # if relation does not exist -> False
            cond = cond and (len(sys.get_relations(rel_uri)) > 0)
            for stm in sys.get_relations(rel_uri):
                if not p.is_subproperty(stm.object, obj):
                    cond = False
    # same for rep
    for statement in sum(repth.get_relations().values(), []):
        if "property" in statement.relation.R1:
            rel_uri = statement.relation.uri
            obj = statement.object
            cond = cond and (len(rep.get_relations(rel_uri)) > 0)
            for stm in rep.get_relations(rel_uri):
                if not p.is_subproperty(stm.object, obj):
                    cond = cond and False


    return cond

res_list = []
for th, sys in itertools.product(theorems, systems):

    rep = sys.get_relations("irk:/ocse/0.2/control_theory#R2928", return_obj=True)
    if len(rep) == 1:
        if cond_func(sys, rep[0], th):
            res_list.append((sys, th))
    elif len(rep) == 0:
        continue
    else:
        raise IndexError

res = p.RuleResult()
for s, t in res_list:
    # res.new_statements.append(t.set_relation(p.R80["applies to"], s))
    # t.set_relation(p.R80["applies to"], s)
    print(t, "applies to", s)


# for stm in res.new_statements:
#     print(stm)


# IPS()
