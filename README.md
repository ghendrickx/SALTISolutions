# SALTISolutions: Working package 7.1

## Introduction about SALTISolutions
SALTISolutions is a research consortium in which five Dutch universities are involved in collaboration with companies in
the fields related to salt intrusion. The consortium focuses on different aspects of salt intrusion and its impact on 
nature and society. The main goal is the development of a Virtual Delta that encompasses a digital twin and a serious
game. For more information, see the [website of SALTISolutions](https://kbase.ncr-web.org/saltisolutions/).

## Working package 7.1
Working package 7.1 (WP 7.1) of SALTISolutions focuses on the development of nature-based solutions to mitigate salt 
intrusion. This PhD research consists of three phases:
1.  Sensitivity analysis of salt intrusion;
1.  In-depth physical assessment(s) of nature-based solution(s);
1.  Multidisciplinary assessment of nature-based solutions.

**Phase 1: Sensitivity analysis:**
The sensitivity analysis determines the sensitivity of the salt intrusion in an estuary to thirteen variables assessed 
(three boundary conditions, and ten geometric characteristics). Due to the complexity of the physical processes 
determining salt intrusion and the scale of the analysis, machine learning techniques are used.

**Phase 2: In-depth assessment:**
Based on the sensitivity analysis of the first phase, some high-potential nature-based solutions are drawn and 
investigated in more detail.

**Phase 3: Multidisciplinary assessment:**
The _Building with Nature_-approach includes three perspectives in its assessment of nature-based solutions: 
(1) physics, (2) ecology, and (3) socio-economy. In this last phase, the ecological and socio-economical perspectives
are added to the assessment of nature-based solutions to mitigate salt intrusion.

# This repository
This repository functions as a collective overview of all work performed as part of the introduced research topic. The
result is a repository without any code, but cross-references to the standalone repositories containing products that
resulted from the research, so-called _sub-repositories_.

All code is developed on a private repository, and once ready for publication, stored in (or added to) a sub-repository.

## Author
Gijs G. Hendrickx 
[![alt text](https://camo.githubusercontent.com/e1ec0e2167b22db46b0a5d60525c3e4a4f879590a04c370fef77e6a7e00eb234/68747470733a2f2f696e666f2e6f726369642e6f72672f77702d636f6e74656e742f75706c6f6164732f323031392f31312f6f726369645f31367831362e706e67) 0000-0001-9523-7657](https://orcid.org/0000-0001-9523-7657)
(_Delft University of Technology_)

Contact: [G.G.Hendrickx@tudelft.nl](mailto:G.G.Hendrickx@tudelft.nl?subject=[GitHub]%20SALTISolutions:%20).

## Sub-repositories
Every sub-repository contains its own elaborate, case-specific `README`-file to assist in its use. The following
sub-repositories are included:
 1. [**ANNESI**](https://github.com/ghendrickx/ANNESI): 
    Artificial neural network for estuarine salt intrusion.
    (_Coupled web-API at [**ANNESI-web**](https://github.com/ghendrickx/ANNESI-web)._)
 1. [**EMMA**](https://github.com/ghendrickx/EMMA):
    Ecotope-map maker based on abiotics.
 1. [**GAPool**](https://github.com/ghendrickx/GAPool):
    Genetic algorithm with "best pool" functionality.
 1. [**HybridModelling**](https://github.com/ghendrickx/HybridModelling): 
    Hybrid modelling using machine learning techniques and process-based models,
    i.e., implementation of work-flow as described in 
    [Hendrickx _et al._ (2023)](https://doi.org/10.1016/j.coastaleng.2023.104289).
    (_Private repository, accessible upon 
    [reasonable request](mailto:G.G.Hendrickx@tudelft.nl?subject=[GitHub]%20HybridModelling:%20)._)
 1. [**SaltFluxDecomposition**](https://github.com/ghendrickx/SaltFluxDecomposition):
    `NumPy`-based salt flux decomposition.

Relevant publications associated with the sub-repositories are stated in their respective `README`-files.

## References
An overview of related publications is presented below.

### Peer-reviewed articles
The following peer-reviewed articles include aspects of this PhD research:

 1. [Hendrickx, G.G.](https://orcid.org/0000-0001-9523-7657),
    [Antol&iacute;nez, J.A.A.](https://orcid.org/0000-0002-0694-4817), and
    [Herman, P.M.J.](https://orcid.org/0000-0003-2188-6341)
    (2023).
    Predicting the response of complex systems for coastal management. 
    _Coastal Engineering_, 
    **182**:104289.
    doi:[10.1016/j.coastaleng.2023.104289](https://doi.org/10.1016/j.coastaleng.2023.104289).
    
 1. [Hendrickx, G.G.](https://orcid.org/0000-0001-9523-7657),
    [Kranenburg, W.M.](https://orcid.org/0000-0002-4736-7913),
    [Antol&iacute;nez, J.A.A.](https://orcid.org/0000-0002-0694-4817),
    [Huismans, Y.](https://orcid.org/0000-0001-6537-6111),
    [Aarninkhof, S.G.J.](https://orcid.org/0000-0002-4591-0257), and
    [Herman, P.M.J.](https://orcid.org/0000-0003-2188-6341)
    (2023).
    Sensitivity of salt intrusion to estuary-scale changes: 
    A systematic modelling study towards nature-based mitigation measures.
    _Estuarine, Coastal and Shelf Science_,
    **295**:108564.
    doi:[10.1016/j.ecss.2023.108564](https://doi.org/10.1016/j.ecss.2023.108564).
    
 1. [Hendrickx, G.G.](https://orcid.org/0000-0001-9523-7657),
    [Manuel, L.A.](https://orcid.org/0000-0001-5424-1270),
    [Pearson, S.G.](https://orcid.org/0000-0002-3986-4469),
    [Aarninkhof, S.G.J.](https://orcid.org/0000-0002-4591-0257), and
    [Meselhe, E.A.](https://orcid.org/0000-0002-5832-8864)
    (2024).
    An earthen sill as a measure to mitigate salt intrusion in estuaries.
    _Estuaries \& Coasts_,
    **47**(5):1199-1208.
    doi:[10.1007/s12237-024-01359-2](https://doi.org/10.1007/s12237-024-01359-2).
    
 1. [Brunink, S.](https://orcid.org/0009-0007-4626-8909), and
    [Hendrickx, G.G.](https://orcid.org/0000-0001-9523-7657).
    (2024).
    Predicting ecotopes from hydrodynamic model data:
        Towards an ecological assessment of nature-based solutions.
    _Nature-Based Solutions_,
    **6**:100145.
    doi:[10.1016/j.nbsj.2024.100145](https://doi.org/10.1016/j.nbsj.2024.100145).    
    
 1. [Hendrickx, G.G.](https://orcid.org/0000-0001-9523-7657), and
    [Pearson, S.G.](https://orcid.org/0000-0002-3986-4469)
    (2024).
    On the effects of intertidal area on estuarine salt intrusion.
    _Journal of Geophysical Research: Oceans_,
    **129**(9):e2023JC020750.
    doi:[10.1029/2023JC020750](https://doi.org/10.1029/2023JC020750).
    
 1. [Bakker, F.P.](https://orcid.org/0009-0004-8385-8981),
    [Hendrickx, G.G.](https://orcid.org/0000-0001-9523-7657),
    [Keyzer, L.M.](https://orcid.org/0000-0002-1501-163X),
    Iglesias, S.R.,
    [Aarninkhof, S.G.J.](https://orcid.org/0000-0002-4591-0257), and
    [van Koningsveld, M.](https://orcid.org/0000-0001-6161-9681).
    (_in review_).
    Trading off dissimilar stakeholders interests:
    Changing the bed level of the main shipping channel of the Rhine-Meuse Delta while considering freshwater 
        availability.
    _Environmental Changes_.
    
 1. [Saccon, E.](https://orcid.org/0009-0005-3867-8233),
    [Hendrickx, G.G.](https://orcid.org/0000-0001-9523-7657),
    [Hulscher, S.J.M.H.](https://orcid.org/0000-0002-8734-1830),
    [Bouma, T.J.](https://orcid.org/0000-0001-7824-7546), and
    [van de Koppel, J.](https://orcid.org/0000-0002-0103-4275).
    (_in review_).
    Wetland topography drives salinity resilience in freshwater tidal ecosystems.
    _Ecological Engineering_.

### Conferences
The following presentations at conferences include aspects of this PhD research (_presenter in **bold**_):

 1. [**Hendrickx, G.G.**](https://orcid.org/0000-0001-9523-7657),
    [Aarninkhof, S.G.J.](https://orcid.org/0000-0002-4591-0257), and
    [Herman, P.M.J.](https://orcid.org/0000-0003-2188-6341)
    (March 25, 2021).
    Nature-based solutions to mitigate salt intrusion.
    _NCK Days 2021_.
    Online.

 1. [**Hendrickx, G.G.**](https://orcid.org/0000-0001-9523-7657),
    [Antol&iacute;nez, J.A.A.](https://orcid.org/0000-0002-0694-4817),
    [Aarninkhof, S.G.J.](https://orcid.org/0000-0002-4591-0257),
    [Huismans, Y.](https://orcid.org/0000-0001-6537-6111),
    [Kranenburg, W.M.](https://orcid.org/0000-0002-4736-7913), and
    [Herman, P.M.J.](https://orcid.org/0000-0003-2188-6341)
    (March 4, 2022).
    Combining machine learning and process-based models to enhance the understanding of estuarine salt intrusion and
    development of estuary-scale nature-based solutions. 
    _Ocean Sciences Meeting 2022_.
    Online.

 1. [**Hendrickx, G.G.**](https://orcid.org/0000-0001-9523-7657),
    [Aarninkhof, S.G.J.](https://orcid.org/0000-0002-4591-0257), and
    [Herman, P.M.J.](https://orcid.org/0000-0003-2188-6341)
    (March 17, 2022). 
    Estuarine sensitivity to salt intrusion mitigation measures. 
    _NCK Days 2022_.
    Enschede, the Netherlands.

 1. [**Hendrickx, G.G.**](https://orcid.org/0000-0001-9523-7657),
    [Antol&iacute;nez, J.A.A.](https://orcid.org/0000-0002-0694-4817),
    [Herman, P.M.J.](https://orcid.org/0000-0003-2188-6341), and
    [Aarninkhof, S.G.J.](https://orcid.org/0000-0002-4591-0257)
    (December 5, 2022).
    Estuarine sensitivity to nature-based salt intrusion mitigation measures.
    _37th International Conference on Coastal Engineering 2022_.
    Sydney, Australia.
    doi:[10.9753/icce.v37.management.146](https://doi.org/10.9753/icce.v37.management.146).

 1. [**Hendrickx, G.G.**](https://orcid.org/0000-0001-9523-7657),
    [Meselhe, E.A.](https://orcid.org/0000-0002-5832-8864),
    [Herman, P.M.J.](https://orcid.org/0000-0003-2188-6341), and
    [Aarninkhof, S.G.J.](https://orcid.org/0000-0002-4591-0257)
    (April 13, 2023).
    A sill as nature-based solution to mitigate salt intrusion.
    _Coastal Sediments 2023_.
    New Orleans, LA, the United States of America.
    doi:[10.1142/9789811275135_0184](https://doi.org/10.1142/9789811275135_0184).

 1. [**Hendrickx, G.G.**](https://orcid.org/0000-0001-9523-7657),
    [Meselhe, E.A.](https://orcid.org/0000-0002-5832-8864),
    [Aarninkhof, S.G.J.](https://orcid.org/0000-0002-4591-0257), and
    [Herman, P.M.J.](https://orcid.org/0000-0003-2188-6341)
    (April 27, 2023).
    Designing a sill to mitigate salt intrusion.
    _Lower Mississippi River Science Symposium_.
    New Orleans, LA, the United States of America.
    
 1. **de Wilde, J.**,
    [Kranenburg, W.M.](https://orcid.org/0000-0002-4736-7913),
    [Huismans, Y.](https://orcid.org/0000-0001-6537-6111),
    [Pietrzak, J.D.](https://orcid.org/0000-0003-1285-5391), and
    [Hendrickx, G.G.](https://orcid.org/0000-0001-9523-7657).
    (March 14, 2024).
    Tidal phase differences in multi-branch systems and their effect on salinity intrusion.
    _NCK Days 2024_.
    Amersfoort, the Netherlands.
 
 1. [**Hendrickx, G.G.**](https://orcid.org/0000-0001-9523-7657),
    [Manuel, L.A.](https://orcid.org/0000-0001-5424-1270),
    [Pearson, S.G.](https://orcid.org/0000-0002-3986-4469),
    [Aarninkhof, S.G.J.](https://orcid.org/0000-0002-4591-0257), and
    [Meselhe, E.A.](https://orcid.org/0000-0002-5832-8864).
    (March 14, 2024).
    When and where to construct a sill to mitigate estuarine salt intrusion.
    _NCK Days 2024_.
    Amersfoort, the Netherlands.
    
 1. [**Hendrickx, G.G.**](https://orcid.org/0000-0001-9523-7657),
    [Pearson, S.G.](https://orcid.org/0000-0002-3986-4469), and
    [Aarninkhof, S.G.J.](https://orcid.org/0000-0002-4591-0257).
    (September 13, 2024).
    Engineering guidelines for nature-based solutions to mitigate salt intrusion.
    _International Conference on Coastal Engineering 2024_.
    Rome, Italy.
    
### Software and datasets
The following software and datasets have been produced as part of this PhD research:

 1. [Hendrickx, G.G.](https://orcid.org/0000-0001-9523-7657)
    (2022).
    _ANNESI: An open-source artificial neural network for estuarine salt intrusion_.
    4TU.ResearchData. Software.
    doi:[10.4121/19307693](https://doi.org/10.4121/19307693).
    
 1. [Hendrickx, G.G.](https://orcid.org/0000-0001-9523-7657)
    (2023).
    _NEESI: Numerical experiments of estuarine salt intrusion dataset_.
    4TU.ResearchData. Dataset.
    doi:[10.4121/22272247](https://doi.org/10.4121/22272247).
    
 1. [Hendrickx, G.G.](https://orcid.org/0000-0001-9523-7657)
    (2023).
    _`NumPy`-based Salt Flux Decomposition_.
    4TU.ResearchData. Software.
    doi:[10.4121/bccbe767-667b-40ba-a4d1-d8fcad900772](https://doi.org/10.4121/bccbe767-667b-40ba-a4d1-d8fcad900772).
    
 1. [Hendrickx, G.G.](https://orcid.org/0000-0001-9523-7657), and
    [Brunink, S.](https://orcid.org/0009-0007-4626-8909).
    (2023).
    _EMMA: Ecotope-Map Maker based on Abiotics_.
    4TU.ResearchData. Software.
    doi:[10.4121/0100fc5a-a99c-4002-9864-3faade3899e3](https://doi.org/10.4121/0100fc5a-a99c-4002-9864-3faade3899e3).
    
 1. [Hendrickx, G.G.](https://orcid.org/0000-0001-9523-7657),
    [Manuel, L.A.](https://orcid.org/0000-0001-5424-1270),
    [Pearson, S.G.](https://orcid.org/0000-0002-3986-4469),
    [Aarninkhof, S.G.J.](https://orcid.org/0000-0002-4591-0257), and
    [Meselhe, E.A.](https://orcid.org/0000-0002-5832-8864)
    (2024).
    Dataset underlying the study
        ''An earthen sill as a measure to mitigate salt intrusion in estuaries.''
    4TU.ResearchData. Dataset.
    doi:[10.4121/10d493df-8efb-442b-8c3d-04e92bcf4c4e](https://doi.org/10.4121/10d493df-8efb-442b-8c3d-04e92bcf4c4e).
    
 1. [Hendrickx, G.G.](https://orcid.org/0000-0001-9523-7657), and
    [Pearson, S.G.](https://orcid.org/0000-0002-3986-4469)
    (2024).
    Dataset underlying the study
        ''On the effects of intertidal area on estuarine salt intrusion.''
    4TU.ResearchData. Dataset.
    doi:[10.4121/c357f1c7-dea8-4971-b5a1-c54c42e4172a](https://doi.org/10.4121/c357f1c7-dea8-4971-b5a1-c54c42e4172a).
    
 1. [Saccon, E.](https://orcid.org/0009-0005-3867-8233),
    [Hendrickx, G.G.](https://orcid.org/0000-0001-9523-7657),
    [Hulscher, S.J.M.H.](https://orcid.org/0000-0002-8734-1830),
    [Bouma, T.J.](https://orcid.org/0000-0001-7824-7546), and
    [van de Koppel, J.](https://orcid.org/0000-0002-0103-4275).
    (2024).
    Dataset underlying the study
        ''Wetland topography drives salinity resilience in freshwater tidal ecosystems.''
    4TU.ResearchData. Dataset.
    doi:[10.4121/93d8d223-e2ab-486e-a85b-da14789532d4](https://doi.org/10.4121/93d8d223-e2ab-486e-a85b-da14789532d4).
