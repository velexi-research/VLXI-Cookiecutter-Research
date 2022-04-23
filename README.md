Velexi Research Project Cookiecutter
====================================

__Version__: 0.3.0

__Authors__  
Kevin T. Chu `<kevin@velexi.com>`

------------------------------------------------------------------------------

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

5. [References][#5]

### Appendices

A. [`poetry` Quick Reference][#Appendix.A]

B. [Julia Package Manager Quick Reference][#Appendix.B]

C. [Making a Julia Package Importable][#Appendix.C]

------------------------------------------------------------------------------

## 1. Overview

The [Velexi Research Project Cookiecutter][vlxi-cookiecutter-research] is
intended to streamline the process of setting up a general Jupyter-based
research project involving computational work that is not centered around data
science and machine learning models. The structure of this research project
template is inspired by [Cookiecutter Data Science][cookiecutter-data-science],
Kuygen Tran's [Data Science Template][khuyentran-data-science-template], the
blog article ["Jupyter Notebook Best Practices for Data Science"][whitmore-2016]
by Jonathan Whitmore.

Features include:

* support for common research workflows (for both individuals and teams);

* a directory structure that organizes and separates different components of
  research data, exploration/experimentation (e.g., Jupyter notebooks),
  documentation (e.g., reports, references), and software (e.g., custom
  functions and test code);

* automatic generation of HTML and pure code versions of Jupyter notebooks to
  facilitate review of both (1) research results and (2) implementation;

* inclusion of [FastDS][fastds] (a wrapper CLI tool that combines Git and DVC
  commands) to simplify code and data version control and reduce errors that
  arise when Git and DVC are used separately;

* Python package and dependency management using [Poetry][python-poetry];

* default Python packages for data and experiment management, interactive work
  environments, and code quality;

* support for Julia; and

* directory-based shell (and Python) environment isolation for systems with
  `direnv` installed.

### 1.1. Repository Contents

```
├── README.md          <- this file
├── RELEASE-NOTES.md   <- release notes for the cookiecutter
├── LICENSE            <- license for the cookiecutter
├── cookiecutter.json  <- cookiecutter configuration file
├── pyproject.toml     <- project configuration file cookiecutter development
│
├── extras/            <- additional files that may be useful for cookiecutter development
│
├── hooks/             <- cookiecutter scripts that run before or after project generation
│
└── {{cookiecutter.project_directory}}/  <- cookiecutter template files
```

### 1.2. License

The contents of this cookiecutter are covered under the Apache License
contained in the `LICENSE` file.

------------------------------------------------------------------------------

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
       as needed using the `poetry` CLI tool. See [Appendix A][#Appendix.A] for
       a quick reference of `poetry` commands.

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
       as needed using the Julia package manager. See [Appendix B][#Appendix.B]
       for a quick reference of Julia package manager REPL commands.

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

4. Update the project documentation.

   * Customize the `README.md` file to reflect the specifics of the project.

   * Verify the correctness of the `LICENSE` file. In particular, check the
     year and name of the copyright owner.

------------------------------------------------------------------------------

## 3. Notes for Developers

### 3.1. Software Requirements

#### Base Requirements

* Git
* Python (>=3.7)
* [Poetry][python-poetry]

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

------------------------------------------------------------------------------

## 4. Known Issues

* When including numba as a project dependency, the Python version constraint
  `pyproject.toml` may need to be more restrictive than default `^3.9`. For
  numba 0.55, the Python version constraint in `pyproject.toml` should be set
  to:

  ```
  python = ">=3.9,<3.11"
  ```

------------------------------------------------------------------------------

## 5. References

* [Cookiecutter Data Science][cookiecutter-data-science]

* [Data Science Template][khuyentran-data-science-template]

* J. Whitmore.
  ["Jupyter Notebook Best Practices for Data Science"][whitmore-2016]
  (2016/09).

------------------------------------------------------------------------------

## Appendix A. `poetry` Quick Reference

* Display the list of Python package dependencies.

  ```shell
  $ poetry show
  ```

* Add a Python package dependency.

  ```shell
  $ poetry add PKG_NAME
  ```

* Remove a Python package dependency.

  ```shell
  $ poetry remove PKG_NAME
  ```

------------------------------------------------------------------------------

## Appendix B. Julia Package Manager Quick Reference

* Activate Julia package manager REPL.

  ```julia
  julia> ]

  (...) pkg>
  ```

* Display the list of Julia package dependencies.

  ```julia
  (...) pkg> status
  ```

  or

  ```julia
  (...) pkg> st
  ```

* Add a Julia package dependency.

  ```julia
  (...) pkg> add PKG_NAME
  ```

* Remove a Julia package dependency.

  ```julia
  (...) pkg> remove PKG_NAME
  ```

  or

  ```julia
  (...) pkg> rm PKG_NAME
  ```

------------------------------------------------------------------------------

## Appendix C. Making a Julia Package Importable

To make Julia code in the `src` directory importable using the `import X`
syntax in Julia, the following conditions must be satisified.

* `Project.toml` must contain the name of the Julia package/module.

  ```toml
  name = "X"
  ```

* A file named `X.jl` must exist in the `src` directory.

* If `/PATH/TO/PROJECT_DIR` is the parent directory of the `src` directory, it
  must be included in

  * the `JULIA_LOAD_PATH` environment variable

    ```shell
    $ export JULIA_LOAD_PATH=/PATH/TO/PROJECT_DIR:$JULIA_LOAD_PATH
    ```

    or

  * the `LOAD_PATH` Julia variable

    ```julia
    julia> push!(LOAD_PATH, "/PATH/TO/PROJECT_DIR")
    ```

------------------------------------------------------------------------------

[-----------------------------INTERNAL LINKS-----------------------------]: #

[#1]: #1-overview
[#1.1]: #11-repository-contents
[#1.2]: #12-license

[#2]: #2-setting-up-a-new-research-project

[#3]: #3-notes-for-developers
[#3.1]: #31-software-requirements
[#3.2]: #32-setting-up-to-develop-the-cookiecutter

[#4]: #4-known-issues

[#5]: #5-references

[#Appendix.A]: #appendix-a-poetry-quick-reference
[#Appendix.B]: #appendix-b-julia-package-manager-quick-reference
[#Appendix.C]: #appendix-c-making-a-julia-package-importable

[-----------------------------EXTERNAL LINKS-----------------------------]: #

[vlxi-cookiecutter-research]: https://github.com/velexi-corporation/VLXI-Cookiecutter-Research

[cookiecutter]: https://cookiecutter.readthedocs.io/en/latest/

[cookiecutter-data-science]: https://github.com/drivendata/cookiecutter-data-science

[fastds]: https://github.com/DAGsHub/fds/

[khuyentran-data-science-template]: https://github.com/khuyentran1401/data-science-template

[python-poetry]: https://python-poetry.org/

[whitmore-2016]:
  https://www.svds.com/tbt-jupyter-notebook-best-practices-data-science/
