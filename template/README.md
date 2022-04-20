PROJECT_NAME
===============================================================================

A short description of the project.

Project Organization
--------------------

    ├── LICENSE            <- License for project contents
    ├── Makefile           <- Makefile with commands like `make data`
    ├── README.md          <- The top-level README for this project
    |
    ├── data
    │   ├── external       <- Data from third party sources
    │   ├── interim        <- Intermediate data that has been transformed
    │   ├── processed      <- The final, canonical data sets for analysis
    │   └── raw            <- The original, immutable data dump
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for
    |                         details
    │
    ├── notebooks          <- Jupyter notebooks. See "Project Conventions"
    |                         section for notebook naming convention. 
    │
    ├── references         <- Data dictionaries, manuals, and all other
    |                         explanatory materials
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures
    │
    ├── requirements.txt   <- The requirements file for reproducing the
    |                         analysis environment, e.g. generated with
    |                         `pip freeze > requirements.txt`
    │
    ├── setup.py           <- Makes project pip installable (pip install -e .)
    |                         so src can be imported
    |
    ├── src                <- Custom source code for use in this project
    |   |
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   └── data           <- Scripts to download or generate data
    │       └── make_dataset.py
    │
    └── tox.ini            <- tox file with settings for running tox; see
                              tox.readthedocs.io

------------------------------------------------------------------------------

Project Conventions
-------------------

### `notebooks` directory

* Jupyter notebooks in the `notebooks` directory should be named using the
  following convention: `YYYY-MM-DD-AUTHOR_INITIALS-BRIEF_DESCRIPTION.ipynb`.

  * Example: `2019-01-17-KC-information_theory_analysis.ipynb`

* Depending on the nature of the project, it may be useful to organize
  notebooks into sub-directories (e.g., by team member, by sub-project).

------------------------------------------------------------------------------

Usage
-----

### Environment

If `direnv` is enabled, the following environment variables are automatically
set.

* `DATA_DIR`: absolute path to `data` directory

export PYTHONPATH=$TOP_DIR
export CONDA_ENVS_PATH=$TOP_DIR/.conda/envs
export CONDA_PKGS_DIRS=$TOP_DIR/.conda/pkgs
export JULIA_PROJECT=@.
export JULIA_LOAD_PATH=$TOP_DIR
export JULIA_LOAD_PATH=$JULIA_LOAD_PATH:  # Append trailing ":" so that Julia
export JUPYTER_CONFIG_DIR=$TOP_DIR/.jupyter
export MLFLOW_CONDA_HOME=`dirname $(dirname $(which conda))`
export MLFLOW_TRACKING_URI
* __TODO__

### Using JupyterLab

* Launching a JupyterLab session.

    ```shell
    $ jupyter-lab
    ```

* Use the GUI to create Jupyter notebooks, edit and run Jupyter notebooks,
  manage files in the file system, etc.

------------------------------------------------------------------------------
