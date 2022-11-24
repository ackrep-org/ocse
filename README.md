# Ontology of Control Systems Engineering (OCSE)

This repo contains formally represented knowledge of the domain of *Control Engineering*.

Further information is available in the [pyerk repository](https://github.com/ackrep-org/pyerk-core).


# PyERK Unittests

Appart from representing control theoretic knowledge this repo also serves as test-data for the [pyerk repository](https://github.com/ackrep-org/pyerk-core).
The various purposes of the data in this repo, which sometimes during development require different states are managed via separate branches:

- purpose of `main`: holding the latest "stable" version of the OCSE intended for public usage (although the whole project is still in heavy development)
- purpose of `develop`: holding the latest development version which likely will become `main` in the future. All tests should pass.
- purpose of `develop_*`: holding experimental version which might be work in progress and thus non-functioning. Tests might fail.
- purpose of `for-unittests`: holding a version of the data which is intended to be uses in the unittests of pyerk. This might be newer or older than `main`.


## History and Background

Until 2022-10-01 the repo with primary URL (<https://github.com/ackrep-org/ocse/>) held the OWL-based version 0.1 of the OCSE, which was referenced in some publications. The current version of the OCSE (0.2) is developed using the [ERK framework](https://github.com/ackrep-org/pyerk-core) and is thus incompatible. Version 0.1 is now available under <https://github.com/ackrep-org/ocse-0.1>.
