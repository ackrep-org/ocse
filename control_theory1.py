import pyerk as p


# noinspection PyUnresolvedReferences
from ipydex import IPS, activate_ips_on_exception  # noqa


ma = p.erkloader.load_mod_from_path("./math1.py", prefix="ma")


# todo: rename .scope("context") to .scope("setting")


__URI__ = "erk:/ocse/0.2/control_theory"

keymanager = p.KeyManager()
p.register_mod(__URI__, keymanager)
p.start_mod(__URI__)

I5948 = p.create_item(
    R1__has_label="dynamical system",
    R2__has_description="system with the capability to change over time, optionally with explicit input and/or output",
    R4__is_instance_of=p.I2["Metaclass"],  # this means: this Item is an ordinary class
)

I7641 = p.create_item(
    R1__has_label="general system model",
    R2__has_description="model of a dynamical system",
    R4__is_instance_of=p.I2["Metaclass"],
)

R7641 = p.create_relation(
    R1__has_label="has approximation",
    R2__has_description="object or class which is an approximation of a dynamical system",
    R8__has_domain_of_argument_1=I5948["dynamical system"],
    R11__has_range_of_result=I7641["general system model"],
)


I4466 = p.create_item(
    R1__has_label="Systems Theory",
    R2__has_description="academic field; might be regarded as part of applied mathematics",
    R4__is_instance_of=p.I3["Field of science"],
    R5__is_part_of=[p.I4["Mathematics"], p.I5["Engineering"]],
)

R1001 = p.create_relation(
    R1__has_label="studies", R2__has_description="object or class which an academic field studies"
)

I4466["Systems Theory"].set_relation(R1001["studies"], I5948["dynamical system"])


R4347 = p.create_relation(
    R1__has_label="has context",
    R2__has_description="establishes the context of a statement",
    # R8__has_domain_of_argument_1=I7723("general mathematical proposition"),
    # R11__has_range_of_result=<!! container of definition-items>
)

R4348 = p.create_relation(
    R1__has_label="has premise",
    R2__has_description="establishes the premise (if-part) of an implication",
    R8__has_domain_of_argument_1=p.I15["implication proposition"],
    # R11__has_range_of_result=<!! container of statements>
)

R4349 = p.create_relation(
    R1__has_label="has assertion",
    R2__has_description="establishes the assertion (then-part) of an implication",
    R8__has_domain_of_argument_1=p.I15["implication proposition"],
    # R11__has_range_of_result=<!! container of statements>
)


R9125 = p.create_relation(
    R1__has_label="has input dimension",
    R8__has_domain_of_argument_1=I7641["general system model"],
    R11__has_range_of_result=p.I38["non-negative integer"],
    R22__is_functional=True,
)

R8978 = p.create_relation(
    R1__has_label="has output dimension",
    R8__has_domain_of_argument_1=I7641["general system model"],
    R11__has_range_of_result=p.I38["non-negative integer"],
    R22__is_functional=True,
)

I1793 = p.create_item(
    R1__has_label="general model representation property",
    R2__has_description="general property of the representation of a model of a dynamical system \
        (not an intrinsic system property)",
    R4__is_instance_of=p.I11["mathematical property"],
)

I2928 = p.create_item(
    R1__has_label="general model representation",
    R2__has_description="general (mathematical) representation of a model of a dynamical system",
    R4__is_instance_of=p.I2["Metaclass"],
)

R2928 = p.create_relation(
    R1__has_label="has model representation",
    R2__has_description="system model has a mathematical representation",
    R8__has_domain_of_argument_1=I7641["general system model"],
    R11__has_range_of_result=I2928["general model representation"],
)

R5100 = p.create_relation(
    R1__has_label="has model representation property",
    R2__has_description="model representation has mathematical property",
    R8__has_domain_of_argument_1=I2928["general model representation"],
    R11__has_range_of_result=I1793["general model representation property"],
)

R2279 = p.create_relation(
    R1__has_label="does not have model representation property",
    R2__has_description="model representation does not have mathematical property",
    R8__has_domain_of_argument_1=I2928["general model representation"],
    R11__has_range_of_result=I1793["general model representation property"],
)

I6886 = p.create_item(
    R1__has_label="general ode state space representation",
    R2__has_description="explicit ODE system description of a dynamical system",
    R3__is_subclass_of=I2928["general model representation"],
    # TODO: this has to use create_equation (to be implemented)
    R6__has_defining_mathematical_relation=p.create_expression(r"$\dot x = f(x, u)$"),
)

R2112 = p.create_relation(
    R1__has_label="has state dimension",
    R2__has_description="number of components of the state vector",
    R8__has_domain_of_argument_1=I6886["general ode state space representation"],
    R11__has_range_of_result=p.I38["non-negative integer"],
)

I6850 = p.create_item(
    R1__has_label="state space model representation",
    R2__has_description="explicit state space model of a dynamical system",
    R3__is_subclass_of=I6886["general ode state space representation"],
    # TODO: this has to use create_equation (to be implemented)
    R6__has_defining_mathematical_relation=p.create_expression(r"$\dot x = Ax + Bu$"),
    # TODO: Rule, system order = 1
)

R7178 = p.create_relation(
    R1__has_label="has number of degrees of freedom",
    R2__has_description=(
        "number of independent parameters that define its configuration in space; applicable to mechanical systems"
    ),
    R8__has_domain_of_argument_1=I7641["general system model"],
    R11__has_range_of_result=p.I38["non-negative integer"],
    R33__has_corresponding_wikidata_entity="https://www.wikidata.org/entity/Q2480745"
    # TODO: add formal comment to clearify the conflicting usages of language:
    # "degree of freedom" vs. "number of degrees of freedom"
)

I5356 = p.create_item(
    R1__has_label="general system property",
    R2__has_description="general property of a model of a dynamical system (not of its representation)",
    R4__is_instance_of=p.I2["Metaclass"],
)

R8303 = p.create_relation(
    R1__has_label="has general system property",
    R2__has_description="model has mathematical property",
    R8__has_domain_of_argument_1=I7641["general system model"],
    R11__has_range_of_result=I5356["general system property"],
)

R7178 = p.create_relation(
    R1__has_label="does not have general system property",
    R2__has_description="model does not have mathematical property",
    R8__has_domain_of_argument_1=I7641["general system model"],
    R11__has_range_of_result=I5356["general system property"],
)

I5357 = p.create_item(
    R1__has_label="differential flatness",
    R4__is_instance_of=I5356["general system property"],
    R2__has_description="differential flatness",
)

I5358 = p.create_item(
    R1__has_label="exact input-to-state linearizability",
    R4__is_instance_of=I5356["general system property"],
    # TODO: it might be necessary to restrict this to ode-state-space-systems
    R2__has_description="exact input-to-state linearizability (via static state feedback)",
)

I7178 = p.create_item(
    R1__has_label="local strong accessibility",
    R4__is_instance_of=I5356["general system property"],
    R2__has_description="local strong accessibility",
    # TODO: put this in relation to controllability
)

"""
def create_I5847():
    R1__has_label = "Equivalence of flat systems and exact input-to-state linearizable systems"
    R4__is_instance_of = c.I15["implication proposition"]
    R2__has_description = (
                             "Establishes that differentially flat systems and exact input-to-state linearizable systems "
                             "are equivalent in the SISO case"
                         )

    def R4347__has_context():
        ctx = c.Context()
        ctx.sys = c.generic_instance(I6886["general_ode_state_space_representation"])
        c.set_restriction(ctx.sys, R9125["has input dimension"], 1)
        return ctx

    def R4348__has_premise(ctx: c.Context):
        ctx.sys.R

    def R4349__has_assertion():
        pass

    return c.create_item_from_namespace()


I5847 = create_I5847()

"""


# attempt without writing code

I2640 = p.create_item(
    R1__has_label="transfer function representation",
    R2__has_description="...",
    R4__is_instance_of=p.I2["Metaclass"],
)


p.R37["has definition"].set_relation(p.R8["has domain of argument 1"], p.I12["mathematical object"])


I4236 = ma.I4236["mathematical expression"]
I4237 = ma.I4237["monovariate rational function"]
I4239 = ma.I4239["monovariate polynomial"]

I5484 = ma.I5484["finite set of complex numbers"]

# todo: replace occurrences
I2738 = ma.I2738
I2739 = ma.I2739

R5323 = p.create_relation(
    R1__has_label="has denominator",
    R2__has_description="...",
    R8__has_domain_of_argument_1=I4237["monovariate rational function"],
    R11__has_range_of_result=I4239["monovariate polynomial"],
)


R5334 = p.create_relation(
    R1__has_label="has representation",
    R2__has_description="relates an entity with an abstract mathematical representation",
    # R8__has_domain_of_argument_1= ...
    R11__has_range_of_result=p.I12["mathematical object"],
)

R1757 = ma.R1757["has set of roots"]

I8181 = p.create_item(
    R1__has_label="properness",
    R2__has_description=(
        "applicable to monovariate rational functions; "
        "satisfied if degree of denominator is not smaller than degree of numerator"
    ),
    R4__is_instance_of=p.I11["mathematical property"],
)

I8182 = p.create_item(
    R1__has_label="strict properness",
    R2__has_description="satisfied if degree of denominator is greater than degree of numerator",
    R17__is_subproperty_of=I8181["properness"],
)

# I7206 = p.create_item(
#     R1__has_label="system-dynamical property",
#     R2__has_description="base class for all systemdynamical properties",
#     R3__is_subclass_of=p.I11["mathematical property"],
# )

I7207 = p.create_item(
    R1__has_label="stability",
    R2__has_description="tendency to stay close to some distinguished trajectory (e.g. equilibrium)",
    R4__is_instance_of=p.I11["mathematical property"],
)

I7599 = p.create_item(
    R1__has_label="instability",
    R2__has_description="tendency to not stay close to some distinguished trajectory (e.g. equilibrium)",
    # TODO: description not ideal
    R4__is_instance_of=p.I11["mathematical property"],
    R43__is_opposite_of=I7207["stability"],
)

# todo: this entity should be made more precise whether it is global or local
I7208 = p.create_item(
    R1__has_label="BIBO stability",
    R2__has_description=(
        "'bounded-input bounded-output stability'; "
        "satisfied if the system responds to every bounded input signal with a bounded output signal"
    ),
    R17__is_subproperty_of=I7207["stability"],
)

I4975 = p.create_item(
    R1__has_label="general algebraic equation",
    R2__has_description="explicit algebraic equation",
    R3__is_subclass_of=I4236["mathematical expression"],
    # TODO: this has to use create_equation (to be implemented)
    R6__has_defining_mathematical_relation=p.create_expression(r"$0 = f(x)$"),
)

I2865 = p.create_item(
    R1__has_label="differential algebraic system of equation",
    R2__has_description="system of differential algebraic equations representing a dynamical system",
    R3__is_subclass_of=I2928["general model representation"],
    R6__has_defining_mathematical_relation=p.create_expression(r"$0 = f(\dot{x}, x, t)$"),
    # TODO make connection to ode and algebraic equation
)

I2562 = p.create_item(
    R1__has_label="general property of pde",
    R2__has_description="general property of partial differential equations",
    R3__is_subclass_of=I1793["general model representation property"],
)

I8063 = p.create_item(
    R1__has_label="partial differential equation",
    R2__has_description="explicit partial differential equation",
    R3__is_subclass_of=I2928["general model representation"],
)

R5718 = p.create_relation(
    R1__has_label="has general pde property",
    R2__has_description="pde has mathematical property",
    R8__has_domain_of_argument_1=I8063["partial differential equation"],
    R11__has_range_of_result=I2562["general property of pde"],
)

I9964 = p.create_item(
    R1__has_label="strict nonlinearity",
    R2__has_description="states that the pde",
    R17__is_subproperty_of=I2562["general property of pde"],
)

I2557 = p.create_item(
    R1__has_label="quasilinearity",
    R2__has_description="states that in a pde the highest order derivatives appear linearly, with their coeffitients \
        being functions of the independant variables and their (lower order) derivatives",
    R17__is_subproperty_of=I2562["general property of pde"],
)

I3114 = p.create_item(
    R1__has_label="semilinearity",
    R2__has_description="states that in a pde the highest order derivatives appear linearly, with their coeffitients \
        being functions of only the independant variables",
    R17__is_subproperty_of=I2557["quasilinearity"],
)

I3863 = p.create_item(
    R1__has_label="linearity",
    R2__has_description="states that in a pde the unknown function and all its derivatives appear linearly, with their coeffitients \
        being functions of only the independant variables",
    R17__is_subproperty_of=I3114["semilinearity"],
)

I5325 = p.create_item(
    R1__has_label="Hurwitz polynomial",
    R2__has_description="monovariate polynomial of quadratic matrices",
    R3__is_subclass_of=I4239["monovariate polynomial"],
)

# <definition>
I4455 = p.create_item(
    R1__has_label="definition of Hurwitz polynomial",
    R2__has_description="the defining statement of what a Hurwitz polynomial is",
    R4__is_instance_of=p.I20["mathematical definition"],
)

with I4455.scope("context") as cm:
    cm.new_var(P=p.uq_instance_of(I4239["monovariate polynomial"]))
    cm.new_var(set_of_roots=p.instance_of(I5484["finite set of complex numbers"]))
    cm.new_rel(cm.P, R1757["has set of roots"], cm.set_of_roots)


with I4455.scope("premises") as cm:
    cm.new_rel(cm.set_of_roots, p.R14["is subset of"], I2739["open left half plane"])

with I4455.scope("assertions") as cm:
    cm.new_rel(cm.P, p.R30["is secondary instance of"], I5325["Hurwitz polynomial"])

I5325["Hurwitz polynomial"].set_relation(p.R37["has definition"], I4455["definition of Hurwitz polynomial"])
# </definition>


# TODO: open question should  I3007["stability theorem for a rational transfer function"] be constructed by using I5325["Hurwitz polynomial"]
# con: BIBO-stability might be meaningfull also for Transferfunctions with nonpolynomial denominators


# <theorem>
# todo this should be an equivalence instead of an implication
I3007 = p.create_item(
    R1__has_label="stability theorem for a rational transfer function",
    R2__has_description="establishes the relation between BIBO-Stability and the poles of the transfer function",
    R4__is_instance_of=p.I15["implication proposition"],
)

with I3007.scope("context") as cm:
    cm.new_var(sys=p.uq_instance_of(I7641["general system model"]))

    cm.new_var(tf_rep=p.instance_of(I2640["transfer function representation"]))
    cm.new_var(denom=p.instance_of(I4239["monovariate polynomial"]))
    cm.new_var(set_of_poles=p.instance_of(I5484["finite set of complex numbers"]))

    cm.new_rel(cm.sys, R5334["has representation"], cm.tf_rep)
    cm.new_rel(cm.tf_rep, R5323["has denominator"], cm.denom)
    cm.new_rel(cm.denom, R1757["has set of roots"], cm.set_of_poles)

with I3007.scope("premises") as cm:
    cm.new_rel(cm.set_of_poles, p.R14["is subset of"], I2739["open left half plane"])
    cm.new_rel(cm.tf_rep, p.R16["has property"], I8181["properness"])

with I3007.scope("assertions") as cm:
    cm.new_rel(cm.sys, p.R16["has property"], I7208["BIBO stability"])
# </theorem>


# preparation for next theorem


# manually import entities that were refactored to erk:/math/0.2
I9904 = ma.I9904["matrix"]
I9905 = ma.I9905["zero matrix"]
I9223 = ma.I9223["definition of zero matrix"]
I9906 = ma.I9906["square matrix"]
R5938 = ma.R5938["has row number"]
R5939 = ma.R5939["has column number"]


R5940 = p.create_relation(
    R1__has_label="has characteristic polynomial",
    R2__has_description="specifies the characteristic polynomial of a square matrix A, i.e. det(s·I-A)",
    R8__has_domain_of_argument_1=I9906["square matrix"],
    R11__has_range_of_result=I4239["monovariate polynomial"],
)

# <definition>
I9907 = p.create_item(
    R1__has_label="definition of square matrix",
    R2__has_description="the defining statement of what a square matrix is",
    R4__is_instance_of=p.I20["mathematical definition"],
)

with I9907.scope("context") as cm:
    cm.new_var(M=p.uq_instance_of(I9904["matrix"]))
    cm.new_var(nr=p.uq_instance_of(p.I39["positive integer"]))

    cm.new_var(nc=p.instance_of(p.I39["positive integer"]))

    cm.new_rel(cm.M, R5938["has row number"], cm.nr)
    cm.new_rel(cm.M, R5939["has column number"], cm.nc)

with I9907.scope("premises") as cm:
    # number of rows == number of columns
    cm.new_equation(lhs=cm.nr, rhs=cm.nc)

with I9907.scope("assertions") as cm:
    cm.new_rel(cm.M, p.R30["is secondary instance of"], I9906["square matrix"])

# </definition>

I9906["square matrix"].set_relation(p.R37["has definition"], I9907["definition of square matrix"])

# <theorem>

I3749 = p.create_item(
    R1__has_label="Cayley-Hamilton theorem",
    R2__has_description="establishes that every square matrix is a root of its own characteristic polynomial",
    R4__is_instance_of=p.I15["implication proposition"],
)

# TODO: specify universal quantification for A and n

with I3749["Cayley-Hamilton theorem"].scope("context") as cm:
    cm.new_var(A=p.uq_instance_of(I9906["square matrix"]))
    cm.new_var(n=p.uq_instance_of(p.I39["positive integer"]))

    cm.new_var(P=p.instance_of(ma.I4240["matrix polynomial"]))
    cm.new_var(Z=p.instance_of(I9905["zero matrix"]))

    cm.new_rel(cm.A, R5938["has row number"], cm.n)
    cm.new_rel(cm.A, R5940["has characteristic polynomial"], cm.P)
    cm.new_rel(cm.Z, R5938["has row number"], cm.n)
    cm.new_rel(cm.Z, R5939["has column number"], cm.n)
    cm.new_rel(cm.Z, p.R24["has LaTeX string"], r"\mathbf{0}")

with I3749["Cayley-Hamilton theorem"].scope("assertions") as cm:
    cm.new_equation(lhs=cm.P(cm.A), rhs=cm.Z)

# </theorem>


p.Sequence("y", p.I000["time derivative of order i"], link_op=p.I000["listing"], start=0, stop="k")

# → it would be nice if one could interactively execute/write out such a sequence for given variable values


I4349 = p.create_item(
    R1__has_label="equivalence of flatness and input-state-linearizability for SISO systems",
    R2__has_description="establishes the equivalence of flatness and input-state-linearizability for SISO systems",
    R4__is_instance_of=p.I15["implication proposition"],
)

# </theorem>
# <statement preparation>
I2277 = p.create_item(
    R1__has_label="statement",
    R2__has_description=(
        "models an 'ordinary statement' e.g. of a publication which is not distinguished as a formal theorem"
    ),
    R3__is_subclass_of=p.I15["implication proposition"],
)

# </statement preparation>

# <statement>
# source: A software framework for embedded nonlinear model predictive control using a gradient‐based augmented Lagrangian approach (GRAMPC)
# source doi: https://doi.org/10.1007/s11081-018-9417-2

# this is still unfinished work in progress:
I4216 = p.create_item(
    R1__has_label="statement about MPC for linear systems and the reducibility to quadratic problems",
    R2__has_description=(
        "for linear systems, the MPC problem can be reduced to a quadratic problem, for which the optimal control"
        "over the admissible polyhedral set can be precomputed."
    ),
    R4__is_instance_of=I2277["statement"],
)


with I4216.scope("context") as cm:
    cm.new_var(sys=p.instance_of(I5948["dynamical system"]))
    cm.new_var(state_space_sys=p.instance_of(I6886["general ode state space representation"]))
    cm.new_var(mpc_problem=p.instance_of(I5948["dynamical system"]))
    cm.new_var(quadratic_problem=p.instance_of(I5948["dynamical system"]))
    cm.new_var(mathematical_solution=p.instance_of(I5948["dynamical system"]))
    cm.new_var(optimal_control_law=p.instance_of(I5948["dynamical system"]))

    cm.new_rel(cm.mpc_problem, p.R000["refers to"], cm.sys)

with I4216.scope("premises") as cm:
    cm.new_rel(cm.sys, p.R000["refers to"], cm.sys)

with I4216.scope("assertions") as cm:
    cm.new_rel(cm.mpc_problem, p.R000["can be reduced to"], cm.quadratic_problem)

"""
Particularly for linear systems, the MPC problem can be reduced to a quadratic
problem, for which the optimal control over the admissible polyhedral set can be
precomputed.
"""

# </statement>


R3326 = p.create_relation(
    R1__has_label="has dimension",
    R2__has_description="specifies the dimension of a (dimensional) mathematical object",
    R8__has_domain_of_argument_1=p.I12["mathematical object"],
    R11__has_range_of_result=p.I38["non-negative integer"],
    R22__is_functional=True,
)

# TODO: consider "state manifold"
I5167 = p.create_item(
    R1__has_label="state space",
    R2__has_description="type for a state space of a dynamical system (I6886)",
    R3__is_subclass_of=p.I12["mathematical object"],
    # R33__has_corresponding_wikidata_entity= TODO,
    R41__has_required_instance_relation=R3326["has dimension"],
)


R5405 = p.create_relation(
    R1__has_label="has associated state space",
    R2__has_description="specifies the associated state space of the subject (e.g. a I9273__explicit...ode_system)",
    R8__has_domain_of_argument_1=p.I12["mathematical object"],
    R11__has_range_of_result=I5167["state space"],
    R22__is_functional=True,
)

I1168 = p.create_item(
    R1__has_label="point in state space",
    R2__has_description="type for a point in a given state space",
    R3__is_subclass_of=p.I12["mathematical object"],
    # R33__has_corresponding_wikidata_entity= TODO,
    R41__has_required_instance_relation=R5405["has associated state space"],
)
# TODO: it might be worth to generalize this: creating a type from a set (where the set is an instance of another type)


I9923 = p.create_item(
    R1__has_label="scalar field",
    R2__has_description="...",
    R3__is_subclass_of=ma.I4895["mathematical operator"],
)

I9841 = p.create_item(
    R1__has_label="vector field",
    R2__has_description="...",
    R3__is_subclass_of=ma.I4895["mathematical operator"],
)


I9273 = p.create_item(
    R1__has_label="explicit first order ODE system",
    R2__has_description="system of explicit first order ordinary differential equations",
    R3__is_subclass_of=p.I12["mathematical object"],
    R41__has_required_instance_relation=R5405["has associated state space"]
    # TODO: make explicit the relation to I6886["general ode state space representation"]
)

R4122 = p.create_relation(
    R1__has_label="has associated vector field",
    R2__has_description="specifies the associated vector field of the subject (e.g. a I9273__explicit...ode_system)",
    R8__has_domain_of_argument_1=I9273["explicit first order ODE system"],
    R11__has_range_of_result=I9841["vector field"],
    R22__is_functional=True,
)

# add this relation to the required relations
I9273["explicit first order ODE system"].set_relation(
    p.R41["has required instance relation"], R4122["has associated vector field"]
)

I2753 = p.create_item(
    R1__has_label="flow of a vector field",
    R2__has_description="operator yielding the solution of the associated I9273__explicit_first_order_ODE_system",
    R3__is_subclass_of=ma.I4895["mathematical operator"],
    R8__has_domain_of_argument_1=I1168["point in state space"],
    R9__has_domain_of_argument_2=p.I35["real number"],
    R10__has_domain_of_argument_3=I9273["explicit first order ODE system"],
    R11__has_range_of_result=I1168["point in state space"],
    # TODO: display and evaluate this notation
    # (\cdot_i) means: the i-th argument
    R13__has_canonical_symbol=r"$\varphi_{(\cdot_2)}^{(\cdot_3)}(\cdot_1)$",
)
# TODO: find a way to assign labels to the arguments: "initial value x", "time t", "vector field f"

I4122 = p.create_item(
    R1__has_label="independent variable",
    R2__has_description="type for an independent variable",
    R3__is_subclass_of=p.I12["mathematical object"],
)


I3513 = p.create_item(
    R1__has_label="derivative w.r.t. scalar parameter",
    R2__has_description="operator yielding the derivative of an expression w.r.t. a parameter",
    R3__is_subclass_of=ma.I4895["mathematical operator"],
    R8__has_domain_of_argument_1=I4236["mathematical expression"],
    R9__has_domain_of_argument_2=I4122["independent variable"],
    R11__has_range_of_result=I4236["mathematical expression"],
    R13__has_canonical_symbol=r"$\frac{d}{d(\cdot_2}) (\cdot_1)$",
)

I2075 = p.create_item(
    R1__has_label="substitution",
    R2__has_description=(
        "operator yielding an new expression where in expression arg1 the subexpression arg2 is replaced by arg3"
    ),
    R4__is_instance_of=ma.I4895["mathematical operator"],
    R8__has_domain_of_argument_1=I4236["mathematical expression"],
    R9__has_domain_of_argument_2=I4236["mathematical expression"],
    R10__has_domain_of_argument_3=I4236["mathematical expression"],
    R11__has_range_of_result=I4236["mathematical expression"],
    R13__has_canonical_symbol=r"$\left.(\cdot_1)\left|_{(\cdot_2)=(\cdot_3)}$",
)


I1347 = p.create_item(
    R1__has_label="Lie derivative of scalar field",
    R2__has_description=(
        "mathematical operation wich maps a scalar field h_1 to a new scalar field h_2, depending on a vector field f; "
        "h2 can be interpreted as the time derivative of h_1 along the solution of the ode associated with f; "
        "in other words: along the flow of f",
    ),
    R4__is_instance_of=ma.I4895["mathematical operator"],
    R8__has_domain_of_argument_1=I9923["scalar field"],
    R9__has_domain_of_argument_2=I9841["vector field"],
    R10__has_domain_of_argument_3=I1168["point in state space"],
    R11__has_range_of_result=I9923["scalar field"],
    R13__has_canonical_symbol=r"$L$",
    # TODO: complete defining equation
)

# <definition>
I6229 = p.create_item(
    R1__has_label="definition of Lie derivative of scalar field",
    R2__has_description="the defining statement of a Lie derivative of a scalar field",
    R4__is_instance_of=p.I20["mathematical definition"],
)

with I6229["definition of Lie derivative of scalar field"].scope("context") as cm:
    n = cm.new_var(n=p.uq_instance_of(p.I39["positive integer"]))
    M = cm.new_var(M=p.uq_instance_of(I5167["state space"]))
    h = cm.new_var(h=p.uq_instance_of(I9923["scalar field"]))
    f = cm.new_var(f=p.uq_instance_of(I9841["vector field"]))

    ode_sys = cm.new_var(ode_sys=p.instance_of(I9273["explicit first order ODE system"]))
    phi = cm.new_var(phi=p.instance_of(I2753["flow of a vector field"]))
    x = cm.new_var(x=p.instance_of(I1168["point in state space"]))
    t = cm.new_var(t=p.instance_of(I4122["independent variable"]))
    deriv = cm.new_var(deriv=p.instance_of(I3513["derivative w.r.t. scalar parameter"]))

    cm.new_rel(cm.M, R3326["has dimension"], cm.n)
    cm.new_rel(cm.h, R5405["has associated state space"], cm.M)
    cm.new_rel(cm.f, R5405["has associated state space"], cm.M)
    cm.new_rel(cm.ode_sys, R5405["has associated state space"], cm.M)
    cm.new_rel(cm.ode_sys, R4122["has associated vector field"], cm.f)

    # evaluate the mappings
    h_evaluated = h(phi(x, t, ode_sys))

    # perform the derivative
    deriv_evaluated = deriv(h_evaluated, t)

    cm.item.subs = I2075["substitution"](deriv_evaluated, t, 0)
    cm.item.L_evaluated = I1347["Lie derivative of scalar field"](h, f, x)


with I6229.scope("assertions") as cm:
    # TODO: encode the directional character of this equation (lhs := rhs)
    cm.new_equation(lhs=cm.L_evaluated, rhs=cm.subs)

I1347["Lie derivative of scalar field"].set_relation(
    p.R37["has definition"], I6229["definition of Lie derivative of scalar field"]
)
# </definition>


I1371 = p.create_item(
    R1__has_label="iterated Lie derivative of scalar field",
    R2__has_description="iterated version of I1347__Lie_derivative_of_scalar_field",
    R3__is_subclass_of=ma.I4895["mathematical operator"],
    R8__has_domain_of_argument_1=I9923["scalar field"],
    R9__has_domain_of_argument_2=I9841["vector field"],
    R10__has_domain_of_argument_3=p.I38["non-negative integer"],
    R11__has_range_of_result=I9923["scalar field"],
    # TODO: add defining equation
)

# <definition>
I8302 = p.create_item(
    R1__has_label="definition of iterated Lie derivative of scalar field",
    R2__has_description=("the defining statement of " "I1371['iterated Lie derivative of scalar field']"),
    R4__is_instance_of=p.I20["mathematical definition"],
)

with I8302["definition of iterated Lie derivative of scalar field"].scope("context") as cm:
    n = cm.new_var(n=p.uq_instance_of(p.I39["positive integer"]))
    M = cm.new_var(M=p.uq_instance_of(I5167["state space"]))
    h = cm.new_var(h=p.uq_instance_of(I9923["scalar field"]))
    f = cm.new_var(f=p.uq_instance_of(I9841["vector field"]))


# TODO: complete definition

# </definition>

# < Model Properties>

# reminder of already existing entities
assert I5356["general system property"]
assert I5357["differential flatness"]
assert I5358["exact input-to-state linearizability"]
assert p.R17["is subproperty of"]


I4101 = p.create_item(
    R1__has_label="general time variance",
    R2__has_description="states that the model of a dynamical system (i.e. its parameters) might change over time",
    R4__is_instance_of=I5356["general system property"],
)

I7733 = p.create_item(
    R1__has_label="time invariance",
    R2__has_description="states that the model of a dynamical system (i.e. its parameters) does not change over time",
    R4__is_instance_of=I5356["general system property"],
    R17__is_subproperty_of=I4101["general time variance"],
)

I9030 = p.create_item(
    R1__has_label="strict time variance",
    R2__has_description="states that the model of a dynamical system (i.e. its parameters) do change over time",
    R4__is_instance_of=I5356["general system property"],
    R17__is_subproperty_of=I4101["general time variance"],
    R43__is_opposite_of=I7733["time invariance"],
)

I9210 = p.create_item(
    R1__has_label="stabilizability",
    R2__has_description="states that for the model of a dynamical system there exists a state feedback such that the \
        system is asymptotically stable",
    R4__is_instance_of=I5356["general system property"],
)

I7864 = p.create_item(
    R1__has_label="controllability",
    R2__has_description="states that the state of the model of a dynamical system can be changed from any arbitrary \
        starting state to any desired state in a finite amount of time using an external input",
    R4__is_instance_of=I5356["general system property"],
    R17__is_subproperty_of=I9210["stabilizability"],
)

I9853 = p.create_item(
    R1__has_label="detectability",
    R2__has_description="states that all unobservable state components of the model of a dynamical system are \
        asymptotically stable",
    R4__is_instance_of=I5356["general system property"],
)

I3227 = p.create_item(
    R1__has_label="observability",
    R2__has_description="states that all state components of the model of a dynamical system can be reconstructed using\
        only information of the system outputs",
    R4__is_instance_of=I5356["general system property"],
    R17__is_subproperty_of=I9853["detectability"],
)

I3321 = p.create_item(
    R1__has_label="minimum phase",
    R2__has_description="states that the model of a dynamical system has asymptotically stable zero dynamics",
    R4__is_instance_of=I5356["general system property"],
)

I2827 = p.create_item(
    R1__has_label="general nonlinearity",
    R2__has_description="states that the system model equations might not be linear",
    R4__is_instance_of=I1793["general model representation property"],
)

I6091 = p.create_item(
    R1__has_label="control affine",
    R2__has_description="states that in the system model equations the input only appears linearly",
    R4__is_instance_of=I1793["general model representation property"],
    R6__has_defining_mathematical_relation=p.create_expression(r"$\dot{x}=f(x)+g(x)u$"),
    R17__is_subproperty_of=I2827["general nonlinearity"],
)

I5247 = p.create_item(
    R1__has_label="polynomial",
    R2__has_description="states that the system model equations are polynomial w.r.t. the state components",
    R4__is_instance_of=I1793["general model representation property"],
    R17__is_subproperty_of=I6091["control affine"],
)

I4761 = p.create_item(
    R1__has_label="linearity",
    R2__has_description="states that the system model equations are linear",
    R4__is_instance_of=I1793["general model representation property"],
    R17__is_subproperty_of=I5247["polynomial"],
)

I1898 = p.create_item(
    R1__has_label="lti",
    R2__has_description="states that the system model is linear and time-invariant",
    R4__is_instance_of=I5356["general system property"],
    R17__is_subproperty_of=[I4761["linearity"], I7733["time invariance"]],
)

I4478 = p.create_item(
    R1__has_label="strict nonlinearity",
    R2__has_description="states that the system model equations are not linear",
    R4__is_instance_of=I1793["general model representation property"],
    R17__is_subproperty_of=I2827["general nonlinearity"],
    R43__is_opposite_of=I4761["linearity"],
)

I8978 = p.create_item(
    R1__has_label="time continuity",
    R2__has_description="states that the system is modeled continuously",
    R4__is_instance_of=I1793["general model representation property"],
)

I5031 = p.create_item(
    R1__has_label="time discreteness",
    R2__has_description="states that the system is modeled discretely",
    R4__is_instance_of=I1793["general model representation property"],
    R43__is_opposite_of=I8978["time continuity"],
)

I5718 = p.create_item(
    R1__has_label="autonomy",
    R2__has_description="states that the model of a dynamical system is autonomous",
    R4__is_instance_of=I5356["general system property"],
    # TODO rule with R9125["has input dimension"] 0
)

I5236 = p.create_item(
    R1__has_label="general trajectory property",
    R2__has_description="general property of a trajectory",
    R4__is_instance_of=p.I11["mathematical property"],
)

I7062 = p.create_item(
    R1__has_label="trajectory",
    R2__has_description="solution to a differential equation",
    R3__is_subclass_of=p.I12["mathematical object"],
)

R7062 = p.create_relation(
    R1__has_label="has general trajectory property",
    R2__has_description="trajectory has mathematical property",
    R8__has_domain_of_argument_1=I7062["trajectory"],
    R11__has_range_of_result=I5236["general trajectory property"],
)

R5031 = p.create_relation(
    R1__has_label="has trajectory",
    R2__has_description="object or class has a trajectory",
    R8__has_domain_of_argument_1=I7641["general system model"],
    R11__has_range_of_result=I7062["trajectory"],
)

I9820 = p.create_item(
    R1__has_label="equilibrium point",
    R2__has_description="constant solution to a diffenrential equation",
    R3__is_subclass_of=I7062["trajectory"],
)

I1664 = p.create_item(
    R1__has_label="limit cycle",
    R2__has_description="closed trajectory which other trajectories spiral into or out of",
    R3__is_subclass_of=I7062["trajectory"],
)

R3898 = p.create_relation(
    R1__has_label="has system order",
    R2__has_description="highest time derivative present in the system equations",
    R8__has_domain_of_argument_1=I2928["general model representation"],
    R11__has_range_of_result=p.I38["non-negative integer"],
    R22__is_functional=True,
)

R6134 = p.create_relation(
    R1__has_label="has highest time derivative",
    R2__has_description="the highest time derivative occuring in the model equations",
    R8__has_domain_of_argument_1=I7641["general system model"],
    R11__has_range_of_result=p.I38["non-negative integer"],
    R22__is_functional=True,
)

# ljapunov stability

I5082 = p.create_item(
    R1__has_label="local attractiveness",
    R2__has_description="states that all trajectories that start close enough to the trajectory in consideration will \
        converge to it",
    R4__is_instance_of=I5236["general trajectory property"],
)

I8059 = p.create_item(
    R1__has_label="global attractiveness",
    R2__has_description="states that all trajectories will converge to the trajectory in consideration",
    R4__is_instance_of=I5236["general trajectory property"],
    R17__is_subproperty_of=I5082["local attractiveness"],
)

I2931 = p.create_item(
    R1__has_label="local ljapunov stability",
    R2__has_description="states that all trajectories that start close enough to the equilibrium will not leave a \
        certain neighborhood",
    R4__is_instance_of=I5236["general trajectory property"],
    R17__is_subproperty_of=I7207["stability"],
)

I8744 = p.create_item(
    R1__has_label="global ljapunov stability",
    R2__has_description="states that all trajectories will not leave a certain neighborhood around the equilibrium",
    R4__is_instance_of=I5236["general trajectory property"],
    R17__is_subproperty_of=I2931["local ljapunov stability"],
)

I4900 = p.create_item(
    R1__has_label="local asymtotical stability",
    R2__has_description="states that all trajectories that start close enough to the equilibrium remain close enough \
        and will converge to it",
    R4__is_instance_of=I5236["general trajectory property"],
    R17__is_subproperty_of=[I2931["local ljapunov stability"], I5082["local attractiveness"]],
)

I5677 = p.create_item(
    R1__has_label="global asymtotical stability",
    R2__has_description="states that all trajectories remain close enough to the equilibrium and will converge to it",
    R4__is_instance_of=I5236["general trajectory property"],
    R17__is_subproperty_of=[
        I8744["global ljapunov stability"],
        I8059["global attractiveness"],
        I4900["local asymtotical stability"],
    ],
)

I9642 = p.create_item(
    R1__has_label="local exponential stability",
    R2__has_description="states that an equilibrium is locally asymptotically stable and all trajectories converge at \
        least exponentially fast",
    R4__is_instance_of=I5236["general trajectory property"],
    R17__is_subproperty_of=I4900["local asymtotical stability"],
)

I5100 = p.create_item(
    R1__has_label="global exponential stability",
    R2__has_description="states that an equilibrium is globally asymptotically stable and all trajectories converge at \
        least exponentially fast",
    R4__is_instance_of=I5236["general trajectory property"],
    R17__is_subproperty_of=[I5677["global asymtotical stability"], I9642["local exponential stability"]],
)

I8303 = p.create_item(
    R1__has_label="strict ljapunov instability",
    R2__has_description="states that some trajectories that start close enough to the equilibrium will still leave a \
        certain neighborhood",
    R4__is_instance_of=I5236["general trajectory property"],
    R43__is_opposite_of=I2931["local ljapunov stability"],
)

I9304 = p.create_item(
    R1__has_label="knot",
    R2__has_description="states that the phase portrait forms a knot near the equilibrium point",
    R4__is_instance_of=I5236["general trajectory property"],
    # rule system order=2,
)

I6467 = p.create_item(
    R1__has_label="saddle",
    R2__has_description="states that the phase portrait forms a saddle near the equilibrium point",
    R4__is_instance_of=I5236["general trajectory property"],
    # rule system order=2,
    # TODO: Implement rule that saddle is always unstable
)


I4610 = p.create_item(
    R1__has_label="spiral",
    R2__has_description="states that the phase portrait forms a spiral near the equilibrium point",
    R4__is_instance_of=I5236["general trajectory property"],
    # rule system order=2,
)

I3241 = p.create_item(
    R1__has_label="chaotic behavior",
    R2__has_description="states that small deviations in the initial conditions result in qualitative changes in the \
        trajectory",
    R4__is_instance_of=I5236["general trajectory property"],
)

I1779 = p.create_item(
    R1__has_label="driftlessness",
    R2__has_description="states that the dirft term of an input affine system is always 0",
    R4__is_instance_of=I1793["general model representation property"],
    R17__is_subproperty_of=I6091["control affine"],
)

I4131 = p.create_item(
    R1__has_label="domain",
    R2__has_description="area of research",
    R4__is_instance_of=p.I2["Metaclass"],
)

R8316 = p.create_relation(
    R1__has_label="belongs to domain",
    R2__has_description="states that the model of a dynamical system belongs to a specific domain",
    R8__has_domain_of_argument_1=I7641["general system model"],
    R11__has_range_of_result=I4131["domain"],
)

I4498 = p.create_item(
    R1__has_label="artifical domain",
    R2__has_description="domain containing research on the topic of artificial systems",
    R4__is_instance_of=I4131["domain"],
)

I7667 = p.create_item(
    R1__has_label="thermal domain",
    R2__has_description="domain containing research on the topic of thermodynamics",
    R4__is_instance_of=I4131["domain"],
)

I1052 = p.create_item(
    R1__has_label="electrical domain",
    R2__has_description="domain containing research on the topic of electrical systems",
    R4__is_instance_of=I4131["domain"],
)

I6203 = p.create_item(
    R1__has_label="chemical domain",
    R2__has_description="domain containing research on the topic of chemical systems",
    R4__is_instance_of=I4131["domain"],
)

I1696 = p.create_item(
    R1__has_label="physical domain",
    R2__has_description="domain containing research on the topic of physical systems (e.g. mechanical systems)",
    R4__is_instance_of=I4131["domain"],
)

I4931 = p.create_item(
    R1__has_label="biological domain",
    R2__has_description="domain containing research on the topic of biological systems",
    R4__is_instance_of=I4131["domain"],
)

I9223 = p.create_item(
    R1__has_label="mechanical domain",
    R2__has_description="domain containing research on the topic of mechanical systems",
    R3__is_subclass_of=I1696["physical domain"],
)

# general equation of linear second order pde with 2 independant variables
I2112 = p.instance_of(I4236["mathematical expression"])
I2112.set_relation(p.R24["has LaTeX string"], r"$A(x,y)u_{xx} + 2B(x,y)u_{xy} + C(x,y)u_{yy} + f(x,y,u,u_x,u_y)$")

I1070 = p.new_equation(lhs=I2112, rhs=ma.I5000["scalar zero"])

I6963 = p.instance_of(I4236["mathematical expression"])
I6963.set_relation(p.R24["has LaTeX string"], r"$B^2-AC$")

I2279 = p.new_mathematical_relation(lhs=I6963, rsgn="<", rhs=ma.I5000["scalar zero"])
I9769 = p.new_mathematical_relation(lhs=I6963, rsgn="==", rhs=ma.I5000["scalar zero"])
I6458 = p.new_mathematical_relation(lhs=I6963, rsgn=">", rhs=ma.I5000["scalar zero"])

I4704 = p.create_item(
    R1__has_label="hyperbolic",
    R2__has_description="b²-ac>0",
    R6__has_defining_mathematical_relation=I6458,
    R17__is_subproperty_of=I3863["linearity"],
    # rule system order=2,
)

I8844 = p.create_item(
    R1__has_label="parabolic",
    R2__has_description="b²-ac=0",
    R6__has_defining_mathematical_relation=I9769,
    R17__is_subproperty_of=I3863["linearity"],
    # rule system order=2,
)

I5239 = p.create_item(
    R1__has_label="elliptic",
    R2__has_description="b²-ac<0",
    R6__has_defining_mathematical_relation=I2279,
    R17__is_subproperty_of=I3863["linearity"],
    # rule system order=2,
)

I1892 = p.create_item(
    R1__has_label="boundary condition",
    R2__has_description="boundary condition of a pde",
    R4__is_instance_of=p.I12["mathematical object"],
)

R9746 = p.create_relation(
    R1__has_label="has boundary condition",
    R2__has_description="state that the pde has a specific boundary condition",
    R8__has_domain_of_argument_1=I8063["partial differential equation"],
    R11__has_range_of_result=I1892["boundary condition"],
)

# TODO: make a connection to system order >= 2 , consistency checking rule
I6830 = p.create_item(
    R1__has_label="dirichlet boundary condition",
    R2__has_description="explicit specification of the values of the solution at the boundary of the domain",
    R3__is_subclass_of=I1892["boundary condition"],
)

I7095 = p.create_item(
    R1__has_label="robin boundary condition",
    R2__has_description="explicit specification of a linear combination solution values and solution derivative values \
        at the boundary of the domain",
    R3__is_subclass_of=I1892["boundary condition"],
)

I3659 = p.create_item(
    R1__has_label="neumann boundary condition",
    R2__has_description="explicit specification of the values of the derivative of the solution at the boundary of \
        the domain",
    R3__is_subclass_of=I1892["boundary condition"],
)

I8316 = p.create_item(
    R1__has_label="bifurcation",
    R2__has_description="states that a small change in the bifurcation parameter causes a qualitative change in the \
        systems trajectory",
    R3__is_subclass_of=I5356["general system property"],
    R6__has_defining_mathematical_relation=p.I23["equation"],
)

R2950 = p.create_relation(
    R1__has_label="has corresponding ackrep key",
    R2__has_description="...",
    R8__has_domain_of_argument_1=I7641["general system model"],
    R11__has_range_of_result=str,
    R22__is_functional=True,
)

I2699 = p.create_item(
    R1__has_label="general ackrep entity",
    R2__has_description="general ackrep entity",
    R4__is_instance_of=p.I2["Metaclass"],
)

I5919 = p.create_item(
    R1__has_label="problem specification",
    R2__has_description="type of ackrep entity",
    R3__is_subclass_of=I2699["general ackrep entity"],
)

I4635 = p.create_item(
    R1__has_label="problem solution",
    R2__has_description="type of ackrep entity",
    R3__is_subclass_of=I2699["general ackrep entity"],
)

I1161 = p.create_item(
    R1__has_label="old tag",
    R2__has_description="",
    R3__is_subclass_of=p.I1["general item"],
)

R1070 = p.create_relation(
    R1__has_label="has old tag",
    R2__has_description="state that an ackrep entity has an old tag",
    R8__has_domain_of_argument_1=I2699["general ackrep entity"],
    R11__has_range_of_result=I1161["old tag"],
)

"""
template:
= p.create_item(
    R1__has_label="",
    R2__has_description="",
    R4__is_instance_of=I5356["general system property"],
    R4__is_instance_of=I1793["general model representation property"],
)

key reservoir J







     R6458
      R5919
      R4635
      R1161
      R2699
      R4931

      R1195



I2933      R2933
I5483      R5483
I3369      R3369
I4663      R4663
I8733      R8733
I5106      R5106
I5600      R5600
I8026      R8026
I5536      R5536
I4703      R4703
I6660      R6660
I9594      R9594
I2975      R2975
I6204      R6204
I9015      R9015
I8509      R8509
I5288      R5288
I4766      R4766
I4147      R4147
I6210      R6210
I1775      R1775
I7006      R7006
I4432      R4432
I8142      R8142






R9820
R1664
R5236
R9642
R4900
R5082
R2931
"""

"""
key reservoir C
I9987
I6548
I6189
I4274
I3712
I6338
I2613
I2983
"""

p.end_mod()
