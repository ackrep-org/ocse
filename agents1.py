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
    R33__has_corresponding_wikidata_entity="https://www.wikidata.org/wiki/Property:P734",
)

R7782 = p.create_relation(
    R1__has_label="has given name",
    R2__has_description="first name or another given name of this person",
    R18__has_usage_hint=[
        "this relation is non-functional, i.e. a person can have multiple given names; order matters",
        "if given name is unknown, it is acceptable to use initials here",
    ],
    R33__has_corresponding_wikidata_entity="https://www.wikidata.org/wiki/Property:P735",
)

R3474 = p.create_relation(
    R1__has_label="has ORCID",
    R2__has_description="specifies the orcid of a researcher",
    R18__has_usage_hint="This can be used if no wikidata entry is yet available",
    R33__has_corresponding_wikidata_entity="https://www.wikidata.org/wiki/Property:P496",
)


I7435 = p.create_item(
    R1__has_label="human",
    R2__has_description="human being",
    R4__is_instance_of=p.I2["Metaclass"],
    R33__has_corresponding_wikidata_entity="https://www.wikidata.org/entity/Q5",
)


def create_person(given_name: str, family_name: str, r2: str, r33=None, r3474=None):
    """
    This is a convenience function that simplifies the creation of items for humans
    """
    item_key = p.get_key_str_by_inspection()

    r1 = f"{given_name} {family_name}"
    item: p.Item  = p.create_item(
        item_key,
        R1__has_label=r1,
        R2__has_description=r2,
        R4__is_instance_of=I7435["human"],
        R7781__has_family_name=family_name,
        R7782__has_given_name=given_name,
    )

    if r33:
        assert isinstance(r33, str)
        item.set_relation(p.R33["has corresponding wikidata entity"], r33)
    if r3474:
        assert isinstance(r3474, str)
        item.set_relation(R3474["has ORCID"], r3474)

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

I1257 = create_person("Joseph Pierre", "LaSalle", "mathematician", r33="https://www.wikidata.org/wiki/Q15455952")

I8430 = create_person("Eduardo Daniel", "Sontag", "mathematician", r33="https://www.wikidata.org/wiki/Q3709600")

I7906 = create_person("Rudolf", "Lipschitz", "mathematician", r33="https://www.wikidata.org/wiki/Q77322")

I4853 = create_person("Sophus", "Lie", "mathematician", r33="https://www.wikidata.org/wiki/Q30769")

I7115 = create_person("Michel", "Fliess", "computer scientist", r33="https://www.wikidata.org/wiki/Q3309635")

I3474 = create_person("Joachim", "Rudolph", "engineer", r3474="https://orcid.org/0000-0001-8402-2458")

I8885 = create_person("Frank", "Allgöwer", "engineer", r33="https://www.wikidata.org/wiki/Q1238632")

I1639 = create_person("Frank", "Woittennek", "engineer", r3474="https://orcid.org/0000-0001-8268-9582")

I9437 = create_person("Albrecht", "Gensior", "engineer", r3474="https://orcid.org/0000-0002-4276-6819")

I1635 = create_person("Johannes", "Reuter", "engineer", r3474="https://orcid.org/0000-0003-2069-5682")

I5667 = create_person("Kathrin", "Flaßkamp", "engineer", r3474="https://orcid.org/0000-0001-5983-1907")

I8521 = create_person("Jan", "Winkler", "engineer", r3474="https://orcid.org/0000-0001-9499-0030")

I3973 = create_person("Kurt", "Schlacher", "engineer")

I7642 = create_person("Hugues", "Mounier", "engineer", r3474="https://orcid.org/0000-0002-7069-3119")

I3749 = create_person("Greta", "Zimmer", "engineer")

I3520 = create_person("Jörg", "Raisch", "engineer", r33="https://www.wikidata.org/wiki/Q107287703")

I1690 = create_person("Nicole", "Gehring", "engineer", r33="https://www.wikidata.org/wiki/Q60780539")

I3238 = create_person("Matthias", "Franke", "engineer", r33="https://www.wikidata.org/wiki/Q57423172")

I9404 = create_person("Kurt", "Reinschke", "engineer", r33="https://www.wikidata.org/wiki/Q106238929")

I2377 = create_person("Andreas", "Kugi", "engineer", r33="https://www.wikidata.org/wiki/Q102409925")

I6176 = create_person("Alberto", "Isidori", "control theorist", r33="https://www.wikidata.org/wiki/Q3608377")

I8526 = create_person("Jens", "Saak", "researcher", r33="https://www.wikidata.org/wiki/Q87670704")

I4329 = create_person("Jürgen", "Adamy", "researcher", r33="https://www.wikidata.org/wiki/Q99739075")

I7718 = create_person("Joachim", "Deutscher", "researcher", r3474="https://orcid.org/0000-0001-6596-6066")

I4722 = create_person("Knut", "Graichen", "researcher", r33="https://www.wikidata.org/wiki/Q102409924")

I6846 = create_person("Thomas", "Meurer", "researcher", r33="https://www.wikidata.org/wiki/Q60576394")

I7912 = create_person("Stefan", "Ecklebe", "engineer", r3474="https://orcid.org/0000-0002-4911-1233")

I3867 = create_person("Timm", "Faulwasser", "researcher", r33="https://www.wikidata.org/wiki/Q56426088")

I6334 = create_person("Rolf", "Findeisen", "researcher", r33="https://www.wikidata.org/wiki/Q56426090")

I4666 = create_person("Daniel", "Gerbet", "engineer", r3474="https://orcid.org/0000-0002-8527-8727")

I6725 = create_person("Claus", "Hillermeier", "engineer", r33="https://www.wikidata.org/wiki/Q112355168")

I9170 = create_person("Peter", "Hippe", "engineer")

I7086 = create_person("Abdurrahman", "Irscheid", "engineer", r3474="https://orcid.org/0000-0002-5913-2468")

I4786 = create_person("Paul", "Kotyczka", "engineer", r3474="https://orcid.org/0000-0002-6669-6368")

I3764 = create_person("Boris", "Lohmann", "engineer", r33="https://www.wikidata.org/wiki/Q59543808")

# note: unclear whether orcid exists (too many people with this name)
I8739 = create_person("Victor", "Lopez", "engineer")

# note: unclear whether orcid exists (too many people with this name)
I9992 = create_person("Matthias", "Müller", "engineer")

I4854 = create_person("Amine", "Othmane", "engineer")

I3431 = create_person("Karl", "Worthmann", "mathematician")

I1361 = create_person("Jens", "Wurm", "engineer", r3474="https://orcid.org/0000-0002-6760-7160")





I6591 = p.create_item(
    R1__has_label="source document",
    R2__has_description="type for items that represent books, papers etc",
    R4__is_instance_of=p.I2["Metaclass"],
)

R8433 = p.create_relation(
    R1__has_label="has authors",
    R2__has_description="...",
    R8__has_domain_of_argument_1=I6591["source document"],
    R11__has_range_of_result=I7435["human"],
)

R8434 = p.create_relation(
    R1__has_label="has title",
    R2__has_description="...",
    R8__has_domain_of_argument_1=I6591["source document"],
    R11__has_range_of_result=p.I19["multilingual string literal"],
)

R8435 = p.create_relation(
    R1__has_label="has year",
    R2__has_description="...",
    R8__has_domain_of_argument_1=I6591["source document"],
    R11__has_range_of_result=p.I37["integer number"],
)

R8436 = p.create_relation(
    R1__has_label="has DOI",
    R2__has_description="...",
    R8__has_domain_of_argument_1=I6591["source document"],
    R11__has_range_of_result=str,
)


def create_source(title:str, authors, year: int, doi: str=None):
    """
    This is a convenience function that simplifies the creation of a published source (paper, book, ...)
    """
    item_key = p.get_key_str_by_inspection()

    if not isinstance(authors, (list, tuple)):
        authors = [authors]

    for author in authors:
        assert isinstance(author, p.Item)
    assert len(authors) > 0

    first_authors_name = authors[0].R7781__has_family_name[0]
    if len(authors) > 1:
        suffix = "_etal"
    else:
        suffix = ""

    r1 = f"{year}_{first_authors_name}{suffix}"
    r2 = f"publication '{title}' by {first_authors_name}{suffix.replace('_', ' ')}"
    new_item: p.Item  = p.create_item(
        item_key,
        R1__has_label=r1,
        R2__has_description=r2,
        R4__is_instance_of=I6591["source document"],
        R8433__has_authors=authors,
        R8434__has_title=title,
        R8435__has_year=year,
    )

    if doi:
        new_item.set_relation(R8436["hasDOI"], doi)
    return new_item


I9700 = create_person("Hassan", "Khalil", "electrical engineneer", r33="https://www.wikidata.org/wiki/Q102278369")

I7558 = create_source("Nonlinear Systems", I9700["Hassan Khalil"], 2002)


I7800 = p.create_item(
    R1__has_label="source segment",
    R2__has_description="type to represent a segment (chapter, section, ...) of an I6591__source_document instance",
    R4__is_instance_of=p.I2["Metaclass"],
)



R8437 = p.create_relation(
    R1__has_label="has segment specification",
    R2__has_description="...",
    R8__has_domain_of_argument_1=I7800["source segment"],
    R11__has_range_of_result=str,
)



SOURCE_SEGMENT_CACHE = {}

@p.wrap_function_with_search_uri_context
def get_source_segment(source_doc: p.Item, segment_specification: str):
    """
    :param segment_specification:   str, e.g. "Chapter 3" or "Section 2.5.2" or "Page 84"

    This is a convenience function which creates (or returns an existing) item
    representing a segment of a source document (section, chapter, page, ...)
    """

    r1 = f"{source_doc.R1__has_label} -- {segment_specification}"
    key = (source_doc.uri, segment_specification)
    if item := SOURCE_SEGMENT_CACHE.get(key):
        pass
    else:
        item = p.instance_of(I7800["source segment"], r1=r1)
        SOURCE_SEGMENT_CACHE[key] = item
        item.R8437__has_segment_specification = segment_specification
    return item


R8439 = p.create_relation(
    R1__has_label="is based on source",
    R2__has_description="specifies that the item (e.g. a theorem) is based on some source document",
    R8__has_domain_of_argument_1=p.I46["knowledge artifact"],
    R11__has_range_of_result=[I7800["source segment"], I6591["source document"]],
)



p.end_mod()

"""
key reservoir created with: `pyerk -l agents1.py ag -nk 100`

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
