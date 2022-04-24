Velexi Research Project Cookiecutter
====================================

__Authors__  
Kevin T. Chu `<kevin@velexi.com>`

-------------------------------------------------------------------------------

Table of Contents
-----------------

1. [Overview][#1]

   1.1. [Repository Contents][#1.1]

   1.2. [License][#1.2]

2. [Setting Up a New Research Project][#2]

   2.1. [Instructions][#2.1]

   2.2. [Known Issues][#2.2]

3. [Contributor Notes][#3]

   3.1. [Software Requirements][#3.1]

   3.2. [Setting Up to Develop the Cookiecutter][#3.2]

   3.3. [Additional Notes][#3.3]

4. [Documentation][#4]

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
└── {{cookiecutter.project_directory}}/  <- cookiecutter template
```

### 1.2. License

The contents of this cookiecutter are covered under the Apache License
contained in the `LICENSE` file.

-------------------------------------------------------------------------------

## 2. Setting Up a New Research Project

## 2.1. Instructions

1. ___Prerequisites___.

   * Install the [Cookiecutter][cookiecutter] Python package.

   * Install [Poetry](https://python-poetry.org/).

     * __Note__. The project template uses `poetry` instead of `pip` for
       management of Python package dependencies.

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

   * Configure the Python package dependencies for the project.

     * Install the base Python package dependencies, and update them to the
       latest available versions.

       ```shell
       $ poetry install
       $ poetry update
       ```

     * Review the Python package dependencies for the project, and modify them
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

     * Commit the updated `pyproject.toml` and `poetry.lock` files to the
       project Git repository.

   * Configure the Julia package dependencies for the project (if the project
     was created with Julia support enabled).

     ```julia
     julia> ]

     (...) pkg> instantiate
     ```

     * Review the Julia package dependencies for the project, and modify them
       as needed using the Julia package manager. For a quick reference of
       Julia package manager REPL commands, see the
       [Julia Quick Reference][julia-quick-reference].

     * Commit the updated `Project.toml` file to the project Git repository.

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

## 2.2. Known Issues

* When including numba as a project dependency, the Python version constraint
  `pyproject.toml` needs to be more restrictive than default `^3.9`. For
  numba 0.55, the Python version constraint in `pyproject.toml` should be set
  to:

  ```
  python = ">=3.9,<3.11"
  ```

-------------------------------------------------------------------------------

## 3. Contributor Notes

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

3. Make the cookiecutter better!

### 3.3. Additional Notes

#### Updating the Cookiecutter Project Dependencies

When using `poetry` to update the Python dependencies for the project template
(contained in the `{{cookiecutter.project_directory}}/pyproject.toml` file),
special care is needed to work around the error caused by the templated
`version` number in the template `pyproject.toml` file.

* Temporarily set the `version` parameter in `pyproject.toml` to a valid
  version number (e.g., `"0.1.0"`).

* Use `poetry` to (1) make changes to the package dependency list and/or
  (2) update the package dependency versions.

* Restore the `version` parameter in `pyproject.toml` to its original value:
  `"{{ cookiecutter.version }}"`.

* Commit the updated `pyproject.toml` and `poetry.lock` files to the Git
  repository.

-------------------------------------------------------------------------------

## 4. Documentation

* [FastDS Quick Reference][fastds-quick-reference]

* [Julia Quick Reference][julia-quick-reference]

* [MLflow Quick Reference][mlflow-quick-reference]

* [Poetry Quick Reference][poetry-quick-reference]

-------------------------------------------------------------------------------

[-----------------------------INTERNAL LINKS-----------------------------]: #

[#1]: #1-overview
[#1.1]: #11-repository-contents
[#1.2]: #12-license

[#2]: #2-setting-up-a-new-research-project
[#2.1]: #21-instructions
[#2.2]: #22-known-issues

[#3]: #3-contributor-notes
[#3.1]: #31-software-requirements
[#3.2]: #32-setting-up-to-develop-the-cookiecutter
[#3.3]: #33-additional-notes

[#4]: #4-documentation

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

[whitmore-2016]: https://www.svds.com/tbt-jupyter-notebook-best-practices-data-science/
