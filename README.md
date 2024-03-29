Velexi Research Project Cookiecutter
====================================

The [Velexi Research Project Cookiecutter][vlxi-cookiecutter-research] is
intended to streamline the process of setting up a Jupyter-based research
project involving computational work (but that is not necessarily centered
around data science and/or machine learning models). The structure of this
research project template is inspired by
[Cookiecutter Data Science][cookiecutter-data-science],
Kuygen Tran's [Data Science Template][khuyentran-data-science-template], the
blog article ["Jupyter Notebook Best Practices for Data Science"][whitmore-2016]
by Jonathan Whitmore.

### Features

* Support for common research workflows (for both individuals and teams)

* A directory structure that organizes and separates different components and
  stages of research: data, exploration/experimentation (e.g., Jupyter
  notebooks), documentation (e.g., reports, references), and software (e.g.,
  custom functions and test code)

* Integration with tools that encourage code, data, and scientific quality
  while promoting research efficiency.

  * Code version control: [Git][git]
  * Data version control: [DVC][dvc], [FastDS][fastds]
  * Experiment tracking: [MLflow Tracking][mlflow-tracking]
  * Automated testing and coverage reporting: [pytest][pytest], [coverage][coverage]
  * Code quality: [pre-commit][pre-commit], [black][black], [flake8][flake8],
    [radon][radon]

* Quick references for software tools (e.g., [FastDS][fastds],
  [MLflow][mlflow], [Poetry][poetry])

* Support for the [Julia][julia] programming language

* Python package and dependency management using [Poetry][poetry]

* Directory-based development environment isolation with [direnv][direnv]

-------------------------------------------------------------------------------

Table of Contents
-----------------

1. [Usage][#1]

   1.1. [Cookiecutter Parameters][#1.1]

   1.2. [Setting Up a New Research Project][#1.2]

   1.3. [Publishing Project Documentation to GitHub Pages][#1.3]

   1.4. [Known Issues][#1.4]

2. [Contributor Notes][#2]

   2.1. [License][#2.1]

   2.2. [Repository Contents][#2.2]

   2.3. [Software Requirements][#2.3]

   2.4. [Setting Up to Develop the Cookiecutter][#2.4]

   2.5. [Additional Notes][#2.4]

3. [Documentation][#3]

-------------------------------------------------------------------------------

## 1. Usage

### 1.1. Cookiecutter Parameters

* `project_name`: project name

* `author`: project's primary author

* `email`: primary author's email

* `license`: type of license to use for the project

* `python_version`: Python versions compatible with project. See the
  "[Dependency sepcification][poetry-dependency-specification]" section
  of the Poetry documentation for version specifier semantics.

* `enable_julia`: flag indicating whether Julia should be enabled for the
  project

### 1.2. Setting Up a New Research Project

1. Prerequisites

   * Install [Git][git].

   * Install [Python][python] 3.9 (or greater).

   * If the project uses [Julia][julia], install [Julia][julia] 1.6 (or
     greater).

   * Install [Poetry][poetry] 1.2 (or greater).

     ___Note___. The project template uses `poetry` instead of `pip` for
     management of Python package dependencies.

   * Install the [Cookiecutter][cookiecutter] Python package.

   * _Optional_. Install [direnv][direnv].

2. Use `cookiecutter` to create a new research project.

   ```shell
   $ cookiecutter https://github.com/velexi-research/VLXI-Cookiecutter-Research.git
   ```

3. Set up a dedicated virtual environment for the project. Any of the common
   virtual environment options (e.g., `venv`, `direnv`, `conda`) should work.
   Below are instructions for setting up a `direnv` or `poetry` environment.

   ___Note___: to avoid conflicts between virtual environments, only one method
   should be used to manage the virtual environment.

   * __`direnv` Environment__. _Note_: `direnv` manages the environment for
     both Python and the shell.

     * Prerequisite. Install `direnv`.

     * Copy `extras/dot-envrc` to the project root directory, and rename it to
       `.envrc`.

       ```shell
       $ cd $PROJECT_ROOT_DIR
       $ cp extras/dot-envrc .envrc
       ```

     * Grant permission to direnv to execute the .envrc file.

       ```shell
       $ direnv allow
       ```

   * __`poetry` Environment__. _Note_: `poetry` only manages the Python
     environment (it does not manage the shell environment).

     * Create a `poetry` environment that uses a specific Python executable.
       For instance, if `python3` is on your `PATH`, the following command
       creates (or activates if it already exists) a Python virtual environment
       that uses `python3` for the project.

       ```shell
       $ poetry env use python3
       ```

       For commands to use other Python executables for the virtual environment,
       see the [Poetry Quick Reference][poetry-quick-reference].

4. Install the base Python package dependencies.

   ```shell
   $ poetry install
   ```

5. Configure Git.

   * Install the Git pre-commit hooks.

     ```shell
     $ pre-commit install
     ```

   * _Optional_. Set up a remote Git repository (e.g., GitHub repository).

     * Create a remote Git repository.

     * Configure the remote Git repository.

       ```shell
       $ git remote add origin GIT_REMOTE
       ```

       where `GIT_REMOTE` is the URL of the remote Git repository.

     * Push the `main` branch to the remote Git repository.

       ```shell
       $ git checkout main
       $ git push -u origin main
       ```

6. Configure DVC.

   * Initialize DVC (Data Version Control). In the following command
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
     $ dvc config core.autostage true
     ```

7. Finish setting up the new research project.

   * Verify the copyright year and owner in the copyright notice. If the
     project is licensed under Apache License 2.0, the copyright notice is
     located in the `NOTICE` file. Otherwise, the copyright notice is located
     in the `LICENSE` file.

   * Update the base Python package dependencies to the latest available
     versions.

     ```shell
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

     For instance, to add numpy to the project dependencies, use the command:

     ```shell
     $ poetry add numpy
     ```

   * Fill in any empty fields in `pyproject.toml`.

   * Customize the `README.md` file to reflect the specifics of the project.

   * If the project was created with Julia support enabled, configure the Julia
     package dependencies for the project

     ```julia
     julia> ]

     (...) pkg> instantiate
     ```

     * Review the Julia package dependencies for the project, and modify them
       as needed using the Julia package manager. For a quick reference of
       Julia package manager REPL commands, see the
       [Julia Quick Reference][julia-quick-reference].

   * Commit all updated files (e.g., `poetry.lock`, `Project.toml`) to the
     project Git repository.

### 1.3. Publishing Project Documentation to GitHub Pages

1. From the project GitHub repository, navigate to "Settings" > "Pages" (in the
   "Code and automation" section of the side menu) and configure GitHub Pages
   to deploy from the `main` branch.

   * Source: Deploy from a branch
   * Branch: main
     * Folder: /(root)

2. In the "About" section of the project GitHub repository, set "Website" to
   the URL for the project GitHub Pages.

3. That's it! Every time the `main` branch is updated, GitHub will
   automatically build project documentation from the `README.md` file (and
   any linked Markdown files) and publish them to the project GitHub Pages.

### 1.4. Known Issues

* When including `numba` as a project dependency, the Python version constraint
  `pyproject.toml` needs to be more restrictive than the default `^3.9`. For
  numba 0.55, the Python version constraint in `[tool.poetry.dependencies]`
  section of `pyproject.toml` should be set to:

  ```
  python = ">=3.9,<3.11"
  ```

-------------------------------------------------------------------------------

## 2. Contributor Notes

### 2.1. License

The contents of this cookiecutter are covered under the Apache License 2.0
(included in the `LICENSE` file). The copyright for this cookiecutter is
contained in the `NOTICE` file.

### 2.2. Repository Contents

```
├── README.md                         <- this file
├── RELEASE-NOTES.md                  <- cookiecutter release notes
├── LICENSE                           <- cookiecutter license
├── NOTICE                            <- cookiecutter copyright notice
├── cookiecutter.json                 <- cookiecutter configuration file
├── pyproject.toml                    <- Python project metadata file for
│                                        cookiecutter development
├── poetry.lock                       <- Poetry lockfile for cookiecutter
│                                        development
├── docs/                             <- cookiecutter documentation
├── extras/                           <- additional files that may be useful for
│                                        cookiecutter development
├── hooks/                            <- cookiecutter scripts that run before
│                                        and/or after project generation
├── spikes/                           <- experimental code
└── {{cookiecutter.__project_name}}/  <- cookiecutter template
```

### 2.3. Software Requirements

#### Base Requirements

* [Git][git]
* [Python][python] (>=3.9)
* [Poetry][poetry] (>=1.2)

#### Optional Packages

* [direnv][direnv]

#### Python Packages

See `[tool.poetry.dependencies]` section of [`pyproject.toml`](pyproject.toml).

### 2.4. Setting Up to Develop the Cookiecutter

1. Set up a dedicated virtual environment for cookiecutter development.
   See Step 3 from [Section 2.1][#2.1] for instructions on how to set up
   `direnv` and `poetry` environments.

2. Install the Python packages required for development.

   ```shell
   $ poetry install

3. Install the Git pre-commit hooks.

   ```shell
   $ pre-commit install
   ```

4. Make the cookiecutter better!

### 2.5. Additional Notes

#### Updating Template Dependencies

To update the Python dependencies for the template (contained in the
`{{cookiecutter.__project_name}}` directory), use the following procedure to
ensure that Python package dependencies for developing the non-template
components of the cookiecutter (e.g., `hooks/pre_gen_project.py`) do not
interfere with Python package dependencies for the template.

* Create a local clone of the cookiecutter Git repository to use for
  cookiecutter development.

  ```shell
  $ git clone git@github.com:velexi-research/VLXI-Cookiecutter-Research.git
  ```

* Use `cookiecutter` from the local cookiecutter Git repository to create an
  instance of the template to use for updating Python package dependencies.

  ```shell
  $ cookiecutter PATH/TO/LOCAL/REPO
  ```

* In the instance of the template, perform the following steps to update the
  template's Python package dependencies.

  * Set up a virtual environment for developing the template (e.g., a direnv
    environment).

  * Use `poetry` or manually edit `pyproject.toml` to (1) make changes to the
    Python package dependency list and (2) update the versions of Python package
    dependencies.

  * Use `poetry` to update the Python package dependencies and versions recorded
    in the `poetry.lock` file.

* Update `{{cookiecutter.__project_name}}/pyproject.toml`.

  * Copy `pyproject.toml` from the instance of the template to
    `{{cookiecutter.__project_name}}/pyproject.toml`.

  * Restore the templated values in the `[tool.poetry]` section to the
    following:

    <!-- {% raw %} -->
    ```jinja
    [tool.poetry]
    name = "{{ cookiecutter.__project_name }}"
    version = "0.0.0"
    description = ""
    license = "{% if cookiecutter.license == 'Apache License 2.0' %}Apache-2.0{% elif cookiecutter.license == 'BSD-3-Clause License' %}BSD-3-Clause{% elif cookiecutter.license == 'MIT License' %}MIT{% endif %}"
    readme = "README.md"
    authors = ["{{ cookiecutter.author }} <{{ cookiecutter.email }}>"]
    ```
    <!-- {% endraw %} -->

* Update `{{cookiecutter.__project_name}}/poetry.lock`.

  * Copy `poetry.lock` from the instance of the template to
    `{{cookiecutter.__project_name}}/poetry.lock`.

* Commit the updated `pyproject.toml` and `poetry.lock` files to the Git
  repository.

-------------------------------------------------------------------------------

## 3. Documentation

* [FastDS Quick Reference][fastds-quick-reference]

* [Julia Quick Reference][julia-quick-reference]

* [MLflow Quick Reference][mlflow-quick-reference]

* [Poetry Quick Reference][poetry-quick-reference]

-------------------------------------------------------------------------------

[----------------------------- INTERNAL LINKS -----------------------------]: #

[#1]: #1-usage
[#1.1]: #11-cookiecutter-parameters
[#1.2]: #12-setting-up-a-new-research-project
[#1.3]: #13-publishing-project-documentation-to-github-pages
[#1.4]: #14-known-issues

[#2]: #2-contributor-notes
[#2.1]: #21-license
[#2.2]: #22-repository-contents
[#2.3]: #23-software-requirements
[#2.4]: #24-setting-up-to-develop-the-cookiecutter
[#2.5]: #25-additional-notes

[#3]: #3-documentation

[---------------------------- REPOSITORY LINKS ----------------------------]: #

[fastds-quick-reference]: {{cookiecutter.__project_name}}/extras/quick-references/FastDS-Quick-Reference.md

[julia-quick-reference]: {{cookiecutter.__project_name}}/extras/quick-references/Julia-Quick-Reference.md

[mlflow-quick-reference]: {{cookiecutter.__project_name}}/extras/quick-references/MLflow-Quick-Reference.md

[poetry-quick-reference]: {{cookiecutter.__project_name}}/extras/quick-references/Poetry-Quick-Reference.md

[vlxi-cookiecutter-research]: https://github.com/velexi-corporation/VLXI-Cookiecutter-Research

[----------------------------- EXTERNAL LINKS -----------------------------]: #

[black]: https://black.readthedocs.io/

[cookiecutter]: https://cookiecutter.readthedocs.io/en/latest/

[cookiecutter-data-science]: https://github.com/drivendata/cookiecutter-data-science

[coverage]: https://coverage.readthedocs.io/

[direnv]: https://direnv.net/

[dvc]: https://dvc.org/

[fastds]: https://github.com/DAGsHub/fds/

[flake8]: https://flake8.pycqa.org/

[git]: https://git-scm.com/

[julia]: https://julialang.org/

[khuyentran-data-science-template]: https://github.com/khuyentran1401/data-science-template

[mlflow]: https://www.mlflow.org

[mlflow-tracking]: https://www.mlflow.org/docs/latest/tracking.html

[poetry]: https://python-poetry.org/

[poetry-dependency-specification]: https://python-poetry.org/docs/dependency-specification/

[pre-commit]: https://pre-commit.com/

[pytest]: https://docs.pytest.org/

[python]: https://www.python.org/

[radon]: https://radon.readthedocs.io/

[whitmore-2016]: https://www.svds.com/tbt-jupyter-notebook-best-practices-data-science/
