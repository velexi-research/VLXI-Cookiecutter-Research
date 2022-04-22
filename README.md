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

------------------------------------------------------------------------------

## 1. Overview

The [Velexi Research Project Cookiecutter][vlxi-cookiecutter-research]
is intended to streamline the process of setting up a general Jupyter-based
research project involving computational work but _not_ centered on data science
and machine learning models. The structure of this research project template is
inspired by [Cookiecutter Data Science][cookiecutter-data-science] (v1),
Kuygen Tran's [Data Science Template][khuyentran-data-science-template], the
blog article ["Jupyter Notebook Best Practices for Data Science"][whitmore-2016]
by Jonathan Whitmore.

Features include:

* support for common research workflows (for both individuals and teams);

* a directory structure that organizes and separates different components of a
  research project: data, exploration/experimentation (e.g., Jupyter notebooks),
  documentation (e.g., reports, references), and software (e.g., custom
  functions and test code);

* automatic generation of HTML and pure code versions of Jupyter notebooks to
  facilitate review of both (1) research results and (2) implementation;

* Git and DVC integration to encourage code _and_ data version control;

* inclusion of default Python packages for data and experiment management,
  interactive work environments, and code quality;

* Python package management using [Poetry](https://python-poetry.org/);

* support for Julia; and

* directory-based Python _and_ shell environment isolation for system with
  `direnv` installed.

### 1.1. Repository Contents

```
├── README.md          <- this file
├── RELEASE-NOTES.md   <- release notes for this cookiecutter
├── LICENSE            <- license for this cookiecutter
├── pyproject.toml     <- project configuration file
│
├── extras/            <- additional files that may be useful for cookiecutter
│                      <- development
│
├── hooks/             <- cookiecutter pre- and post-generation scripts
│
└── {{cookiecutter.project_directory}}/   <- cookiecutter template files
```

### 1.2. License

The contents of this package are covered under the Apache License contained in
the `LICENSE` file.

------------------------------------------------------------------------------

## 2. Setting Up a New Research Project

1. ___Prerequisite___. Install the [Cookiecutter][cookiecutter] Python package.

2. Use `cookiecutter` to create a new research project.

   ```shell
   $ cookiecutter https://github.com/velexi-corporation/VLXI-Cookiecutter-Research.git
   ```

3. Finish initializing the project.

   * ___Optional___. Use `direnv` to set up a Python virtual environment for
     the project.

     * Copy `extras/dot-envrc` to `.envrc` in the project directory.

     * Grant permission to `direnv` to execute the `.envrc` file.

       ```shell
       $ direnv allow
       ```

   * Install the Python package dependencies.

     * Review the Python package dependencies for the project, and update them
       as needed using the `poetry` CLI tool. See [Appendix A][#Appendix.A] for
       a quick reference of `poetry` commands.

       Packages that may be useful (but are not included by default):

       * numpy
       * scipy
       * numba
       * pandas
       * scikit-learn
       * matplotlib
       * seaborn

   * If the project was created with Julia support enabled, install the Python
     package dependencies.

     * Review the Julia package dependencies for the project, and update them
       as needed using the Julia package manager. See [Appendix B][#Appendix.B]
       for a quick reference of Julia package manager REPL commands.

   * Initialize DVC (data version control). In the following command
     `PROJECT_DIR` should be replaced by the path to the newly created research
     project.

     ```shell
     $ cd PROJECT_DIR
     $ dvc init
     $ git commit -m "Initialize DVC"
     ```

     or

     ```shell
     $ cd PROJECT_DIR
     $ fds init
     $ fds commit -m "Initialize DVC"
     ```

4. Update the project documentation.

   * Customize the `README.md` file to reflect the specifics of the project.

   * Verify `LICENSE` file is correct. In particular, check the year and name
     of the copyright owner.

------------------------------------------------------------------------------

## 3. Notes for Developers

### 3.1. Software Requirements

#### Base Requirements

* Git
* Python (>=3.7)
* [Poetry](https://python-poetry.org/)

#### Optional Packages

* `direnv`

#### Python Packages

See [`pyproject.toml`](pyproject.toml).

### 3.2. Setting Up to Develop the Cookiecutter

1. ___Optional___. Use `direnv` to set up a Python virtual environment for the
   cookiecutter.

    * Copy `extras/dot-envrc` to `.envrc` in the Git repository's root
      directory.

    * Grant permission to `direnv` to execute the `.envrc` file.

      ```shell
      $ direnv allow
      ```

2. Install the Python packages required for development.

   ```shell
   $ poetry install
   ```

3. Make the cookiecutter better.

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

  ```shell
  $ julia

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

[-----------------------------EXTERNAL LINKS-----------------------------]: #

[vlxi-cookiecutter-research]: https://github.com/velexi-corporation/VLXI-Cookiecutter-Research

[cookiecutter]: https://cookiecutter.readthedocs.io/en/latest/

[cookiecutter-data-science]: https://github.com/drivendata/cookiecutter-data-science

[khuyentran-data-science-template]: https://github.com/khuyentran1401/data-science-template

[whitmore-2016]:
  https://www.svds.com/tbt-jupyter-notebook-best-practices-data-science/
