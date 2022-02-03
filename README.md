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
1. Sensitivity analysis of salt intrusion;
1. In-depth physical assessment(s) of nature-based solution(s);
1. Multidisciplinary assessment of nature-based solutions.

**Sensitivity analysis:** The sensitivity analysis determines the sensitivity of the salt intrusion in an estuary to 
thirteen variables assessed (three boundary conditions, and ten geometric characteristics). Due to the complexity of the
physical processes determining salt intrusion and the scale of the analysis, machine learning techniques are used.

**In-depth assessment:** TBD

**Multidisciplinary assessment:** TBD

# Python-package
This Python-package is created as support for the PhD research encapsulated by working package 7.1 (WP 7.1) of the 
consortium SALTISolutions. The Python-code in this package enables the auto-generation of input files for [Delft3D
Flexible Mesh](https://www.deltares.nl/en/software/delft3d-flexible-mesh-suite/) simulations (only the [D-FLOW 
module](https://www.deltares.nl/en/software/module/d-flow-flexible-mesh/), developed by Deltares). It does so based on 
the thirteen variables assessed in the sensitivity analysis. The created input files consist of:
- Unstructured grid (`*_net.nc`);
- Initial conditions (`*_ini.ext`);
    - Bathymetry data (`*.xyz`);
    - Initial salinity field (`*.xyz`);
    - Friction field (`*.xyz`).
- Boundary conditions (`*_bnd.ext`);
    - Boundary locations (`*.pli`);
    - Boundary condition specifications (`*.bc`).
- Observation stations (`*.xyn`).

In addition, the D-Flow model data file is also saved in the same working directory (i.e. the model's folder), which 
remains constant for all model configurations:
- D-FLOW specifications (`*.mdu`).

This last file is extracted from within the package, and includes the duration of the simulations. Therefore, the 
duration is automated and standardised. This can, however, easily be modified (via `pre_processing/model.py`).

In the working directory specified (i.e. `<model-working-directory>`), the following folder/file structure is created:
```
<model-working-directory>
+-- dflowfm
|   +-- *_net.nc
|   +-- *_ini.ext
|   +-- *.xyz
|   +-- *_bnd.ext
|   +-- *.pli
|   +-- *.bc
|   +-- *.xyn
|   +-- *.mdu
+-- check.config
+-- input.config
```
Note that some file-types will or may occur multiple times in the `dflowfm`-folder based on the model configurations: 
1. There are three `*.xyz`-files; see list above.
1. There are at least two `*.pli`-files, as good modelling practices require at least two boundary locations.
1. There are at least two `*.bc`-files, as good modelling practices require at least two boundary condition types.

Furthermore, the `*.config`-files are a result of checking the physical validity of the provided input data 
(`check.config`), and an overview-file of the input data provided (`input.config`).

The output of the D-Flow model simulations are stored in the `dflowfm`-folder, creating an `output`-folder in this
directory. Certain post-processing scripts might add files to the `<model-working-directory>` with the same format of
the built-in pre-processing files, i.e. `*.config`-file(s).

# Requirements
The package can be used in two ways: (1) auto-generate the input-files for D-Flow; and/or (2) auto-execute a multitude
of model simulations on an external server. In case of the former, the following packages are required, where the 
versions used are stated in between brackets:
- `Python` [3.7+];
- `numpy` [1.19.4];
- `pandas` [1.1.4];
- `netCDF4` [1.5.6].

For any post-processing by means of figures, the standard plotting package is used and integrated in various scripts:
- `matplotlib` [3.3.3].

In case of the latter, there are some additional packages required:
- `lhsmdu` [1.1];
- `scikit_learn` [0.24.2];
- `qcg_pilotjob` [0.12.2].

Note that these are **additions** to the previous set of packages. Furthermore, a virtual environment (i.e. `venv`) must
be created for the use of [`QCG.PilotJob`](https://qcg-pilotjob.readthedocs.io/en/latest/index.html). (For help with the
installation of `QCG.PilotJob`, see [their webpage](https://qcg-pilotjob.readthedocs.io/en/latest/installation.html).)

# Stand-alone usage
Many components in this package can used as stand-alone, i.e. without using the full functionality of auto-generating 
all input files for a D-Flow model. All these components can also be created separately using the corresponding 
components available in this package:
- **Grid generation:** `/modules/grid.py` provides objects suitable for generating in a relatively quick manner 
rectangular grids. It provides the possibility to nest grids in each other, and export the data confirming the
unstructured grid data file required for D-Flow models (i.e. `*_nec.nc`). Certain manipulations of the grid are also
included, which are limited to the requirements of grid-manipulation for this research, i.e. convergence and meandering.

- **Sampling:** `/sampling/batch.py` provides objects to sample the thirteen input parameters confirming the Latin
hypercube sampling approach (`LHS`) after which a subset can be extracted using the Maximum Dissimilarity Algorithm
(`MDA`). This algorithm can also be used separate for the objects provided in `/sampling/batch.py` by calling the method
in `sampling/mda.py`.

- **Boundary condition definitions:** `/modules/boundary_conditions.py` provides objects suitable for creating the input
files for boundary conditions suitable for a D-Flow model. However, not all boundary condition types are included; 
included are (1) water level, (2) discharge, (3) velocity, and (4) salinity. These types can be imposed as astronomical
or time-series boundary condition.

- **Observation locations:** `/modules/observations.py` provides objects for a virtual observation station and for a 
virtual cross-section. These types of observations are tailored to D-Flow, and the defined observation locations are
easily exported confirming the required file-types that can be imported in D-Flow.
