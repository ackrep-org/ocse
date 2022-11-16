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


p.end_mod()


"""

I3240      R3240
I7169      R7169
I1608      R1608
I8133      R8133
I3033      R3033

"""
