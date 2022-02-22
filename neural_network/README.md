# Neural network: Estuarine dynamics
As a by-product of the sensitivity analysis, a neural network has been trained to the elaborate data set created, 
consisting of approximately 2,000 simulations with 
[Delft3D Flexible Mesh](https://www.deltares.nl/en/software/delft3d-flexible-mesh-suite/) (specifically the 
[D-Flow module](https://www.deltares.nl/en/software/module/d-flow-flexible-mesh/)).

The neural network is accessible via a web-API that can be locally hosted by running [`api.py`](api.py). Efforts are 
made to host this web-API publicly.

## Requirements
This sub-repository has the following requirements (see also [`requirements.txt`](requirements.txt)):
*   dash==2.0.0
*   numpy==1.19.4
*   pandas==1.1.4
*   joblib==1.0.1
*   Shapely==1.8.0
*   torch==1.9.0
*   plotly==5.5.0
*   scikit_learn==1.0.2

In addition, the [`utils`](../utils)-folder is required for the functioning of the `neural_network` (i.e. the web-API).

## Structure
The neural network and web-API are located in the folders [`machine_learning`](machine_learning) and 
[`application`](application), respectively:
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
```
For the use of the web-API, [`api.py`](api.py) must be executed with `Python`. This provides a link to a local-host, 
which allows to use the neural network locally in a web-browser.

## Author
Gijs G. Hendrickx 
[![alt text](https://camo.githubusercontent.com/e1ec0e2167b22db46b0a5d60525c3e4a4f879590a04c370fef77e6a7e00eb234/68747470733a2f2f696e666f2e6f726369642e6f72672f77702d636f6e74656e742f75706c6f6164732f323031392f31312f6f726369645f31367831362e706e67) 0000-0001-9523-7657](https://orcid.org/0000-0001-9523-7657)
(*Delft University of Technology*)

## References
If you would like to (re)use the code, please cite accordingly:
1.  Pre-release: [`v0.1-beta`](https://github.com/ghendrickx/SALTISolutions/tree/v0.1-beta/neural_network)
    > Hendrickx, G.G. (2022). SALTISolutions: A neural network for estuarine salt dynamics. 4TU.ResearchData. Software.
    [doi:10.4121/19161752](https://doi.org/10.4121/19161752.v1).

### Version-control
The neural network, and so the web-API, are subject to updates. These updates are reflected by different versions of the
repository.
