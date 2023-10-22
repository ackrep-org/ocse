"""
created: 2022-11-30
original author Carsten Knoll <firstname.lastname@tu-dresden.de>

This module collects knowledge about people and institutions related to control theory. It thus contains personal data,
however only such which is considered to be publicly available already elswhere (e.g. institution websites, wikidata).

If you want to be deleted from or added to this file please create a pull-request (preferred) or contact the author(s).
"""


import pyerk as p


__URI__ = "erk:/ocse/0.2/agents"

keymanager = p.KeyManager(keyseed=1239)
p.register_mod(__URI__, keymanager)
p.start_mod(__URI__)


R7781 = p.create_relation(
    R1__has_label="has family name",
    R2__has_description="part of the full name of a person",
    R33__has_corresponding_wikidata_entity="http://www.wikidata.org/entity/734",
)

R7782 = p.create_relation(
    R1__has_label="has given name",
    R2__has_description="first name or another given name of this person",
    R18__has_usage_hint=[
        "this relation is non-functional, i.e. a person can have multiple given names; order matters",
        "if given name is unknown, it is acceptable to use initials here",
    ],
    R33__has_corresponding_wikidata_entity="http://www.wikidata.org/entity/P735",
)


I7435 = p.create_item(
    R1__has_label="human",
    R2__has_description="human being",
    R4__is_instance_of=p.I2["Metaclass"],
    R33__has_corresponding_wikidata_entity="https://www.wikidata.org/entity/Q5",
)


def create_person(given_name: str, family_name: str, r2):
    """
    This is a convenience function that simplifies the creation of items for humans
    """
    item_key = p.get_key_str_by_inspection()

    r1 = f"{given_name} {family_name}"
    item = p.create_item(
        item_key,
        R1__has_label=r1,
        R2__has_description=r2,
        R4__is_instance_of=I7435["human"],
        R7781__has_family_name=family_name,
        R7782__has_given_name=given_name,
    )

    return item


I2746 = create_person("Rudolf", "Kalman", "electrical engineer and mathematician")


I1342 = p.create_item(
    R1__has_label="academic institution",
    R2__has_description="educational institution dedicated to education and research",
    R4__is_instance_of=p.I2["Metaclass"],
    R33__has_corresponding_wikidata_entity="https://www.wikidata.org/entity/Q4671277",
)

I9942 = p.create_item(
    R1__has_label="Stanford University",
    R2__has_description="private research university in California, USA",
    R4__is_instance_of=I1342["academic institution"],
    R33__has_corresponding_wikidata_entity="https://www.wikidata.org/entity/Q41506",
)

I7301 = p.create_item(
    R1__has_label="ETH Zürich",
    R2__has_description="Swiss Federal Institute of Technology in Zürich",
    R4__is_instance_of=I1342["academic institution"],
    R33__has_corresponding_wikidata_entity="https://www.wikidata.org/entity/Q11942",
)

R1833 = p.create_relation(
    R1__has_label="has employer",
    R2__has_description="specifies for which entity (organisation/person) the subject works",
    R33__has_corresponding_wikidata_entity="https://www.wikidata.org/entity/P108",
)


# the following is for testing qualifiers:

start_time = p.QualifierFactory(p.R48["has start time"])
end_time = p.QualifierFactory(p.R49["has end time"])

I2746["Rudolf Kalman"].set_relation(
    R1833["has employer"], I9942["Stanford University"], qualifiers=[start_time("1964"), end_time("1971")]
)
I2746["Rudolf Kalman"].set_relation(
    R1833["has employer"], I7301["ETH Zürich"], qualifiers=[start_time("1973"), end_time("1997")]
)

I4720 = create_person("Klaus", "Röbenack", "electrical engineer and mathematician")

I8124 = create_person("Carsten", "Knoll", "engineer and researcher")
I8124.set_relation(p.R33["has corresponding wikidata entity"], "http://www.wikidata.org/entity/Q110983632")


I2478 = p.create_item(
    R1__has_label="TU Dresden",
    R2__has_description="Dresden University of Technology",
    R4__is_instance_of=I1342["academic institution"],
    R33__has_corresponding_wikidata_entity="https://www.wikidata.org/entity/Q158158",
)


I2276 = create_person("Aurel", "Stodola", "Slovak scientist")
I2276.set_relation("R33__has_corresponding_wikidata_entity", "https://www.wikidata.org/entity/Q666875")


R6876 = p.create_relation(
    R1__has_label="is named after",
    R2__has_description="specifies that the subject is an eponym named after the object",
    R33__has_corresponding_wikidata_entity="https://www.wikidata.org/entity/P138",
)

I2151 = create_person("Aleksandr", "Lyapunov", "mathematician and physicist")
I2151.set_relation(p.R33["has corresponding wikidata entity"], "https://www.wikidata.org/wiki/Q310788")



p.end_mod()


"""
key reservoir created with: `pyerk -l agents1.py ag -nk 100`

I1257      R1257
I8430      R8430
I7906      R7906
I4853      R4853
I6591      R6591
I8433      R8433
I7558      R7558
I9700      R9700
I7800      R7800
I1848      R1848
I7115      R7115
I3474      R3474
I1639      R1639
I8885      R8885
I9437      R9437
I1635      R1635
I5667      R5667
I8521      R8521
I3973      R3973
I7642      R7642
I3749      R3749
I3520      R3520
I1690      R1690
I3238      R3238
I9404      R9404
I2377      R2377
I6176      R6176
I6725      R6725
I9170      R9170
I7086      R7086
I4786      R4786
I3764      R3764
I8739      R8739
I9992      R9992
I3854      R3854
I7934      R7934
I6514      R6514
I8469      R8469
I5543      R5543
I2792      R2792
I8019      R8019
I6589      R6589
I7064      R7064
I6656      R6656
I1928      R1928
I1361      R1361
I3431      R3431
I4854      R4854
I4666      R4666
I6334      R6334
I3867      R3867
I7912      R7912
I6846      R6846
I4722      R4722
I7718      R7718
I4329      R4329
I8526      R8526
I6009      R6009
I3563      R3563
I8388      R8388
I2175      R2175
I9157      R9157
I9661      R9661
I6612      R6612
I9318      R9318
I4247      R4247
I6854      R6854
I3131      R3131
I7191      R7191
I3791      R3791
I3963      R3963
I8266      R8266
I6860      R6860
I3806      R3806
I8337      R8337
I1969      R1969
I3088      R3088
I1173      R1173
I3948      R3948
I4757      R4757
I1943      R1943
I8189      R8189
I2777      R2777
I1236      R1236
I7447      R7447
I6181      R6181
I7364      R7364
I3552      R3552
I7965      R7965
I9438      R9438
I1098      R1098
I9216      R9216
I2888      R2888


"""
