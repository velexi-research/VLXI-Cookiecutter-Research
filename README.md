Velexi Research Project Cookiecutter
====================================

__Version__: 0.3.0

__Authors__  
Kevin T. Chu `<kevin@velexi.com>`

-------------------------------------------------------------------------------

Table of Contents
-----------------

1. [Overview][#1]

   1.1. [Repository Contents][#1.1]

   1.2. [License][#1.2]

2. [Setting Up a New Research Project][#2]

3. [Notes for Developers][#3]

   3.1. [Software Requirements][#3.1]

   3.2. [Setting Up to Develop the Cookiecutter][#3.2]

4. [Known Issues][#4]

5. [Documentation][#5]

-------------------------------------------------------------------------------

## 1. Overview

The [Velexi Research Project Cookiecutter][vlxi-cookiecutter-research] is
intended to streamline the process of setting up a general Jupyter-based
research project involving computational work that is not centered around data
science and machine learning models. The structure of this research project
template is inspired by [Cookiecutter Data Science][cookiecutter-data-science],
Kuygen Tran's [Data Science Template][khuyentran-data-science-template], the
blog article ["Jupyter Notebook Best Practices for Data Science"][whitmore-2016]
by Jonathan Whitmore.

### Features

* Support for common research workflows (for both individuals and teams)

* A directory structure that organizes and separates different components of
  research data, exploration/experimentation (e.g., Jupyter notebooks),
  documentation (e.g., reports, references), and software (e.g., custom
  functions and test code)

* Automatic generation of HTML and pure code versions of Jupyter notebooks to
  facilitate review of both (1) research results and (2) implementation

* Quick references for commonly software components (e.g., [FastDS][fastds],
  [MLflow][mlflow], [Poetry][poetry], etc.)

* Git and DVC integration to encourage code and data version control

* Python package and dependency management using [Poetry][poetry]

* Default Python packages for data and experiment management, interactive work
  environments, and code quality

  * [MLflow Tracking][mlflow-tracking] to encourage good scientific record
    keeping habits

  * [FastDS][fastds] to reduce common errors that arise when Git and DVC are
    used separately

* Support for Julia

* Directory-based shell (and Python) environment isolation for systems with
  `direnv` installed

### 1.1. Repository Contents

```
├── README.md          <- this file
├── RELEASE-NOTES.md   <- release notes for the cookiecutter
├── LICENSE            <- license for the cookiecutter
├── cookiecutter.json  <- cookiecutter configuration file
├── pyproject.toml     <- project configuration file cookiecutter development
├── docs/              <- cookiecutter documentation
├── extras/            <- additional files that may be useful for cookiecutter development
├── hooks/             <- cookiecutter scripts that run before or after project generation
└── {{cookiecutter.project_directory}}/  <- cookiecutter template files
```

### 1.2. License

The contents of this cookiecutter are covered under the Apache License
contained in the `LICENSE` file.

-------------------------------------------------------------------------------

## 2. Setting Up a New Research Project

1. ___Prerequisite___. Install the [Cookiecutter][cookiecutter] Python package.

2. Use `cookiecutter` to create a new research project.

   ```shell
   $ cookiecutter https://github.com/velexi-corporation/VLXI-Cookiecutter-Research.git
   ```

3. Finish setting up the new research project.

   * ___Optional___. Set up the project to use `direnv` to manage the
     environment (for both Python and the shell).

     * Copy `extras/dot-envrc` to the project root directory, and rename it to
       `.envrc`.

     * Grant permission to `direnv` to execute the `.envrc` file.

       ```shell
       $ direnv allow
       ```

   * Install the Python package dependencies.

     ```shell
     $ poetry install
     ```

     * Review the Python package dependencies for the project, and update them
       as needed using the `poetry` CLI tool. For a quick reference of `poetry`
       commands, see the [Poetry Quick Reference][poetry-quick-reference].

       Packages that may be useful (but are not included by default):

       * numpy
       * numba
       * scipy
       * pandas
       * scikit-learn
       * matplotlib
       * seaborn

   * If the project was created with Julia support enabled, install the Julia
     package dependencies.

     ```julia
     julia> ]

     (...) pkg> instantiate
     ```

     * Review the Julia package dependencies for the project, and update them
       as needed using the Julia package manager. For a quick reference of
       Julia package manager REPL commands, see the
       [Julia Quick Reference][julia-quick-reference].

4. Configure Git.

   * Set up a remote Git repository (e.g., GitHub repository).

   * Configure the remote Git repository.

     ```shell
     $ git remote add origin GIT_REMOTE
     ```

     where `GIT_REMOTE` is the URL to the remote Git repository.

5. Configure DVC.

   * Initialize DVC (data version control). In the following command
     `PROJECT_DIR` should be replaced by the path to the newly created research
     project.

     * Using `fds`.

       ```shell
       $ cd PROJECT_DIR
       $ fds init
       $ fds commit -m "Initialize DVC"
       ```

     * Using `dvc` + `git`.

       ```shell
       $ cd PROJECT_DIR
       $ dvc init
       $ git commit -m "Initialize DVC"
       ```

   * Add a remote DVC repository.

     * Set up a remote DVC repository (e.g., S3 bucket).

     * Configure the remote DVC repository.

       ```shell
       $ dvc remote add -d storage DVC_REMOTE
       ```

       where `storage` is the name for the remote repository and `DVC_REMOTE`
       is the URL to the remote DVC repository. __Note__: the `-d` option
       indicates that `storage` should be used as the default remote DVC
       repository.

   * Configure DVC to automatically stage changes to `*.dvc` files with Git.

     ```shell
     $dvc config core.autostage true
     ```

6. Update the project documentation.

   * Customize the `README.md` file to reflect the specifics of the project.

   * Verify the correctness of the `LICENSE` file. In particular, check the
     year and name of the copyright owner.

-------------------------------------------------------------------------------

## 3. Notes for Developers

### 3.1. Software Requirements

#### Base Requirements

* Git
* Python (>=3.7)
* [Poetry][poetry]

#### Optional Packages

* `direnv`

#### Python Packages

See `[tool.poetry.dependencies]` section of [`pyproject.toml`](pyproject.toml).

### 3.2. Setting Up to Develop the Cookiecutter

1. ___Optional___. Set up the project to use `direnv` to manage the environment
  (for both Python and the shell).

    * Copy `extras/dot-envrc` to the Git repository's root directory, and
      rename it to `.envrc`.

    * Grant permission to `direnv` to execute the `.envrc` file.

      ```shell
      $ direnv allow
      ```

2. Install the Python packages required for development.

   ```shell
   $ poetry install
   ```

3. Work on improving the cookiecutter.

-------------------------------------------------------------------------------

## 4. Known Issues

* When including numba as a project dependency, the Python version constraint
  `pyproject.toml` needs to be more restrictive than default `^3.9`. For
  numba 0.55, the Python version constraint in `pyproject.toml` should be set
  to:

  ```
  python = ">=3.9,<3.11"
  ```

-------------------------------------------------------------------------------

## 5. Documentation

* [FastDS Quick Reference][fastds-quick-reference]

* [MLflow Quick Reference][mlflow-quick-reference]

* [Poetry Quick Reference][poetry-quick-reference]

* [Julia Quick Reference][julia-quick-reference]

-------------------------------------------------------------------------------

[-----------------------------INTERNAL LINKS-----------------------------]: #

[#1]: #1-overview
[#1.1]: #11-repository-contents
[#1.2]: #12-license

[#2]: #2-setting-up-a-new-research-project

[#3]: #3-notes-for-developers
[#3.1]: #31-software-requirements
[#3.2]: #32-setting-up-to-develop-the-cookiecutter

[#4]: #4-known-issues

[#5]: #5-documentation

[-----------------------------REPOSITORY LINKS-----------------------------]: #

[fastds-quick-reference]: {{cookiecutter.project_directory}}/docs/references/FastDS-Quick-Reference.md

[julia-quick-reference]: {{cookiecutter.project_directory}}/docs/references/Julia-Quick-Reference.md

[mlflow-quick-reference]: {{cookiecutter.project_directory}}/docs/references/MLflow-Quick-Reference.md

[poetry-quick-reference]: {{cookiecutter.project_directory}}/docs/references/Poetry-Quick-Reference.md

[vlxi-cookiecutter-research]: https://github.com/velexi-corporation/VLXI-Cookiecutter-Research

[-----------------------------EXTERNAL LINKS-----------------------------]: #

[cookiecutter]: https://cookiecutter.readthedocs.io/en/latest/

[cookiecutter-data-science]: https://github.com/drivendata/cookiecutter-data-science

[fastds]: https://github.com/DAGsHub/fds/

[khuyentran-data-science-template]: https://github.com/khuyentran1401/data-science-template

[mlflow]: https://www.mlflow.org

[mlflow-tracking]: https://www.mlflow.org/docs/latest/tracking.html

[poetry]: https://python-poetry.org/

[whitmore-2016]:
  https://www.svds.com/tbt-jupyter-notebook-best-practices-data-science/
