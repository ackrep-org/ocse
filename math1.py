from typing import Union
import pyerk as p

# noinspection PyUnresolvedReferences
from ipydex import IPS, activate_ips_on_exception  #noqa

__URI__ = "erk:/math/0.2"

keymanager = p.KeyManager()
p.register_mod(__URI__, keymanager)
p.start_mod(__URI__)


I5000 = p.create_item(
    R1__has_label="scalar zero",
    R2__has_description="entity representing the zero-element in the set of complex numbers and its subsets",
    R4__is_instance_of=p.I34["complex number"],
    R24__has_LaTeX_string="$0$",
)


I5001 = p.create_item(
    R1__has_label="scalar one",
    R2__has_description="entity representing the one-element in the set of complex numbers and its subsets",
    R4__is_instance_of=p.I34["complex number"],
    R24__has_LaTeX_string="$1$",
)


I4235 = p.create_item(
    R1__has_label="mathematical object",
    R2__has_description="...",
    R4__is_instance_of=p.I2["Metaclass"],
)


I4895 = p.create_item(
    R1__has_label="mathematical operator",
    R2__has_description="general (unspecified) mathematical operator",
    R3__is_subclass_of=I4235["mathematical object"],
)

# make all instances of operators callable:
I4895["mathematical operator"].add_method(p.create_evaluated_mapping, "_custom_call")


I9904 = p.create_item(
    R1__has_label="matrix",
    R2__has_description="matrix of (in general) complex numbers, i.e. matrix over the field of complex numbers",
    R3__is_subclass_of=I4235["mathematical object"],
)


I3240 = p.create_item(
    R1__has_label="matrix element",
    R2__has_description=(
        "mathematical operation wich maps a Matrix A, and two integers i, j to the scalar matrix entry A[i, j]."
        "Index counting starts at 1",
    ),
    R4__is_instance_of=I4895["mathematical operator"],
    R8__has_domain_of_argument_1=I9904["matrix"],
    R9__has_domain_of_argument_2=p.I39["positive integer"],
    R10__has_domain_of_argument_3=p.I39["positive integer"],
    R11__has_range_of_result=p.I34["complex number"],
    R13__has_canonical_symbol=r"$\mathrm{elt}$",
    R18__has_usage_hint=(
        "This operator is assumed be used as callable , e.g. `A_3_6 = I3240['matrix element'](A, 3, 6)`"
    )
)

I3240["matrix element"].add_method(p.create_evaluated_mapping, "_custom_call")


# currently we do not need this (we attach start, stop, step to the range-element directly)
I1195 = p.create_item(
    R1__has_label="integer range",
    R2__has_description="represents an integer range with start-, stop- and step-value",
    R4__is_instance_of=p.I2["Metaclass"],
)


R1616 = p.create_relation(
    R1__has_label="has start value",
    R2__has_description="...",
    R8__has_domain_of_argument_1=I1195["integer range"],
    R11__has_range_of_result=p.I37["integer number"],
    R22__is_functional=True,
)

R1617 = p.create_relation(
    R1__has_label="has stop value",
    R2__has_description="...",
    R8__has_domain_of_argument_1=I1195["integer range"],
    R11__has_range_of_result=p.I37["integer number"],
    R22__is_functional=True,
)

R1618 = p.create_relation(
    R1__has_label="has step value",
    R2__has_description="...",
    R8__has_domain_of_argument_1=I1195["integer range"],
    R11__has_range_of_result=p.I37["integer number"],
    R22__is_functional=True,
)


# TODO: this is probably obsolete
def Range(start, stop, step=1, r1: str = None, r2: str = None):

    range_item = p.instance_of(I1195["integer range"], r1, r2)
    range_item.R1616__has_start_value = start
    range_item.R1617__has_stop_value = stop
    range_item.R1618__has_step_value = step

    return range_item


I6012 = p.create_item(
    R1__has_label="integer range element",
    R2__has_description="class whose instances represent an element from a specified range (I1195)",
    R3__is_subclass_of=p.I37["integer number"],
    R18__has_usage_hint=(
        "Should always have an R3240__has_associated_range relation; ",
        "should be created via the context manager IntegerRangeElement (see below)",
    ),
)


R3240 = p.create_relation(
    R1__has_label="has associated range",
    R2__has_description="...",
    R8__has_domain_of_argument_1=I6012["integer range element"],
    R11__has_range_of_result=I1195["integer range"],
    R22__is_functional=True,
)


class IntegerRangeElement:
    """
    Context manager to model that a statement (or more) have an assertive claim for all elements of a sequence.

    ```
    with RangeElement(start=1, end=3) as i:
        I456["some item"].R789_has_some_property(i)
    ```

    Has (roughly) the same meaning as

    ```
    I456["some item"].R789_has_some_property(1)
    I456["some item"].R789_has_some_property(2)
    I456["some item"].R789_has_some_property(3)
    ```

    Note, however, that the defining attributes of RangeElement, i.e. `start`, `stop`, `step` can be also variables.

    Behind the sc

    """

    def __init__(self, start: Union[int, p.Item], stop: Union[int, p.Item], step: Union[int, p.Item] = 1):
        self.start = start
        self.stop = stop
        self.step = step

        # these might serve to provide optional information to the range_element_item
        self.r1 = None
        self.r2 = None

    def __enter__(self):
        """
        implicitly called in the head of the with statemet
        :return:
        """

        element = p.instance_of(I6012["integer range element"], self.r1, self.r2)

        element.R1616__has_start_value = self.start
        element.R1617__has_stop_value = self.stop
        element.R1618__has_step_value = self.step

        return element

    def __exit__(self, exc_type, exc_val, exc_tb):
        # this is the place to handle exceptions
        pass


I9905 = p.create_item(
    R1__has_label="zero matrix",
    R2__has_description="like its superclass but with all entries equal to zero",
    R3__is_subclass_of=I9904["matrix"],
)

I9906 = p.create_item(
    R1__has_label="square matrix",
    R2__has_description="a matrix for which the number of rows and columns are equal",
    R3__is_subclass_of=I9904["matrix"],
    # TODO: formalize the condition inspired by OWL
)

R5938 = p.create_relation(
    R1__has_label="has row number",
    R2__has_description="specifies the number of rows of a matrix",
    R8__has_domain_of_argument_1=I9904["matrix"],
    R11__has_range_of_result=p.I38["non-negative integer"],
)

# todo: specifies that this item defines I9905
R5939 = p.create_relation(
    R1__has_label="has column number",
    R2__has_description="specifies the number of columns of a matrix",
    R8__has_domain_of_argument_1=I9904["matrix"],
    R11__has_range_of_result=p.I38["non-negative integer"],
)


#            start defintion

I9223 = p.create_item(
    R1__has_label="definition of zero matrix",
    R2__has_description="the defining statement of what a zero matrix is",
    R4__is_instance_of=p.I20["mathematical definition"],
    )


with I9223["definition of zero matrix"].scope("setting") as cm:
    cm.new_var(M=p.uq_instance_of(I9904["matrix"]))

    cm.new_var(nr=p.uq_instance_of(p.I39["positive integer"]))
    cm.new_var(nc=p.instance_of(p.I39["positive integer"]))

    cm.new_rel(cm.M, R5938["has row number"], cm.nr)
    cm.new_rel(cm.M, R5939["has column number"], cm.nc)


with I9223["definition of zero matrix"].scope("premises") as cm:
    with IntegerRangeElement(start=1, stop=cm.nr) as i:
        with IntegerRangeElement(start=1, stop=cm.nc) as j:

            # create an auxiliary variable (not part part of the graph)
            M_ij = I3240["matrix element"](cm.M, i, j)
            cm.new_equation(lhs=M_ij, rhs=I5000["scalar zero"])


with I9223["definition of zero matrix"].scope("assertions") as cm:
    cm.new_rel(cm.M, p.R30["is secondary instance of"], I9905["zero matrix"])

#            end defintion

# ---------------------------------------------------------------------------------------------------------------------

#            start defintion

I1608 = p.create_item(
    R1__has_label="identity matrix",  # TODO: also known as "unit matrix"
    R2__has_description="square matrix with only ones at the main diagonal and every other element zero",
    R3__is_subclass_of=I9906["square matrix"],
)


I7169 = p.create_item(
    R1__has_label="definition of identity matrix",
    R2__has_description="the defining statement of what an identity matrix is",
    R4__is_instance_of=p.I20["mathematical definition"],
)

I1608["identity matrix"].set_relation(p.R37["has definition"], I7169["definition of identity matrix"])


with I7169["definition of identity matrix"].scope("setting") as cm:
    cm.new_var(M=p.uq_instance_of(I9906["square matrix"]))

    cm.new_var(nr=p.uq_instance_of(p.I39["positive integer"]))

    cm.new_rel(cm.M, R5938["has row number"], cm.nr)


with I7169["definition of identity matrix"].scope("premises") as cm:

    # todo: the running indicses should be related to the context cm
    # there should be a context stack
    with IntegerRangeElement(start=1, stop=cm.nr) as i:
        with IntegerRangeElement(start=1, stop=cm.nr) as j:

            # create an auxiliary variable (not part part of the graph)
            M_ij = I3240["matrix element"](cm.M, i, j)

            # Condition in human-readible form:
            # In case i != j, the matrix element M_ij must be 0
            # In case i == j, the matrix element M_ij must be 1

            # These are two implications (as logical statement, with their specific truth table)
            # Both implications must be fulfilled for the premise of the definition to be fulfilled

            with p.ImplicationStatement() as imp1:
                imp1.antecedent_relation(lhs=i, rsgn="!=", rhs=j)
                imp1.consequent_relation(lhs=M_ij, rhs=I5000["scalar zero"])

            with p.ImplicationStatement() as imp2:
                imp1.antecedent_relation(lhs=i, rsgn="==", rhs=j)
                imp1.consequent_relation(lhs=M_ij, rhs=I5001["scalar one"])


with I7169["definition of identity matrix"].scope("assertions") as cm:
    cm.new_rel(cm.M, p.R30["is secondary instance of"], I1608["identity matrix"])

#            end defintion

# ---------------------------------------------------------------------------------------------------------------------

p.end_mod()


"""

I1608      R1608
I8133      R8133
I3033      R3033

"""
