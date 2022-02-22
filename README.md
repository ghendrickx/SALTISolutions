# SALTISolutions: Working package 7.1

## Introduction about SALTISolutions
SALTISolutions is a research consortium in which five Dutch universities are involved in collaboration with companies in
the fields related to salt intrusion. The consortium focuses on different aspects of salt intrusion and its impact on 
nature and society. The main goal is the development of a Virtual Delta that encompasses a digital twin and a serious
game. For more information, click 
[here](https://www.nwo.nl/en/researchprogrammes/perspectief/perspectief-programmes/saltisolutions).

## Working package 7.1
Working package 7.1 (WP 7.1) of SALTISolutions focuses on the development of nature-based solutions to mitigate salt 
intrusion. This PhD research consists of three phases:
1.  Sensitivity analysis of salt intrusion;
1.  In-depth physical assessment(s) of nature-based solution(s);
1.  Multidisciplinary assessment of nature-based solutions.

**Phase 1: Sensitivity analysis:** The sensitivity analysis determines the sensitivity of the salt intrusion in an estuary to 
thirteen variables assessed (three boundary conditions, and ten geometric characteristics). Due to the complexity of the
physical processes determining salt intrusion and the scale of the analysis, machine learning techniques are used.

**Phase 2: In-depth assessment:** TBD

**Phase 3: Multidisciplinary assessment:** TBD

# This repository
This repository is aimed at containing all relevant code produced during an ongoing research. Great effort is put into
structuring this repository such that the code corresponding to the various aspects of the research are clearly stated.
The code is developed on a private repository, and once ready for publication, added to this (public) repository.

## Author
Gijs G. Hendrickx 
[![alt text](https://camo.githubusercontent.com/e1ec0e2167b22db46b0a5d60525c3e4a4f879590a04c370fef77e6a7e00eb234/68747470733a2f2f696e666f2e6f726369642e6f72672f77702d636f6e74656e742f75706c6f6164732f323031392f31312f6f726369645f31367831362e706e67) 0000-0001-9523-7657](https://orcid.org/0000-0001-9523-7657)
(*Delft University of Technology*)

## Sub-repositories
Every sub-repository contains its own elaborate, case-specific `README.md` to assist in its use. The following
sub-repositories are included:
1.  [Neural network](https://github.com/ghendrickx/SALTISolutions/tree/master/neural_network)

## References
As this is a living repository, the exact way of citing depends on the version/release of the code used, which is included
in the respective publications for which they are used.
1.  Pre-release: [`v0.1-beta`](https://github.com/ghendrickx/SALTISolutions/tree/v0.1-beta)
    > Hendrickx, G.G. (2022). SALTISolutions: A neural network for estuarine salt dynamics. 4TU.ResearchData. Software.
    [doi:10.4121/19161752](https://doi.org/10.4121/19161752.v1).

## Structure
The structure of the repository consists of sub-repositories and a utilisation-folder (`utils`) containing objects and
methods used across the board.
```
+-- neural_network/
    +-- application/
        +-- __init__.py
        +-- app.py
        +-- components.py
    +-- machine_learning/
        +-- _data/
            +-- __init__.py
            +-- nn_default.pkl
            +-- nn_scaler.gz
        +-- __init__.py
        +-- _backend.py
        +-- neural_network.py
    +-- api.py
+-- utils/
    +-- __init__.py
    +-- data_conv.py
    +-- files_dirs.py
```
