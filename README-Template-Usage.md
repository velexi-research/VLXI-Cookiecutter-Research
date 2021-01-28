Velexi Template: Data Science Project
=====================================

___Authors___  
Kevin T. Chu `<kevin@velexi.com>`

------------------------------------------------------------------------------

Table of Contents
-----------------

1. [Overview][#1]

   1.1. [Software Dependencies][#1.1]

   1.2. [Directory Structure][#1.2]

   1.3. [Template Files][#1.3]

2. [Usage][#2]

   2.1. [Setting Up][#2.1]

   2.2. [Conventions][#2.2]

   2.3. [Environment][#2.3]

   2.4. [Using Jupyter Notebook][#2.4]

3. [References][#3]

------------------------------------------------------------------------------

## 1. Overview

This project template is intended to support data science projects that
utilize Jupyter notebooks for experimentation and reporting. The design of
the template is based on the blog article
["Jupyter Notebook Best Practices for Data Science"][#whitmore-2016] by
Jonathan Whitmore.

Features include:

* compatible with standard version control software;

* automatically saves HTML and `*.py` versions of Jupyter notebooks to
  facilitate review of both (1) data science results and (2) implementation
  code; and

* supports common data science workflows (for both individuals and teams).

### 1.1 Software Dependencies

#### Base Requirements

* Python (>=3.5)

#### Recommended Packages ####

* Julia (>=1.4)
* `direnv`

### 1.2 Directory Structure

    README.md
    README-Template-Usage.md
    README.md.template
    requirements.txt
    Project.toml
    Manifest.toml
    bin/
    data/
    extras/
    lab-notebook/
    reports/
    src/

* `README.md`: symbolic to `README-Template-Usage.md`

* `README-Template-Usage.md`: this file

* `README.md.template`: template README file for data science project

* `requirements.txt`: `pip` requirements file containing Python packages for
  data science, testing, and assessing code quality

* `Project.toml`: Julia package management file containing Julia packagesi
  dependencies

* `Manifest.toml`: Julia package management file that Julia uses to maintain
  a record of the state of the Julia environment. This file should _not_ be
  edited.

* `bin`: directory where scripts and programs should be placed. It also
  contains the `init-julia.jl` script that can be used to initialize a
  Julia-based project.

* `data`: directory where project data should be placed. __Note__: data placed
  in this directory ___does not___ necessarily need to be committed to the git
  repository. For projects with large datasets, committing the data to the git
  repository is ___discouraged___.

* `extras`: directory containing template configuration files (e.g., `direnv`
  configuration file)

* `lab-notebook`: directory containing Jupyter notebooks used for
  experimentation and development. Jupyter notebooks saved in this directory
  should (1) have a single author and (2) be dated.

* `lib`: directory containing source code developed to support project

* `reports`: directory containing Jupyter notebooks that present and record
  final results. Jupyter notebooks saved in this directory should be polished,
  contain final analysis results, and be the work product of the entire data
  science team.

### 1.3. Template Files

Template files and directories are indicated by the 'template' suffix. These
files and directories are intended to simplify the set up of the lab notebook.
When appropriate, they should be renamed (with the 'template' suffix removed).

------------------------------------------------------------------------------

## 2. Usage

### 2.1 Setting Up

* Set up environment for project using only one of the following approaches.

  * `direnv`-based Setup

    * Copy `extras/envrc.template` to `.envrc` in project root directory.

    * Grant permission to `direnv` to execute the `.envrc` file.

      ```shell
      $ `direnv allow
      ```

    * If needed, edit "User-Specified Configuration Parameters" section of
      `.envrc`.

  * `autoenv`-based Setup

    * Create Python virtual environment.

      ```shell
        $ python3 -m venv .venv
      ```

    * Copy `extras/env.template` to `.env` in project root directory.

    * If needed, edit "User-Specified Configuration Parameters" section of
      `.env`.

* Install required Python packages.

    ```shell
    $ pip install -r requirements.txt
    ```

* (OPTIONAL) Install required Julia packages.

    ```shell
    $ init-julia.jl
    ```

### 2.2 Conventions

#### `lab-notebook` directory

* Jupyter notebooks in the `lab-notebook` directory should be named using the
  following convention: `YYYY-MM-DD-AUTHOR_INITIALS-BRIEF_DESCRIPTION.ipynb`.

  * Example: `2019-01-17-KTC-information_theory_analysis.ipynb`

* Depending on the nature of the project, it may be useful to organize lab
  notebook entries into sub-directories (e.g., by team member, by sub-project).

### 2.3 Environment

If `direnv` or `autoenv` is enabled, the following environment variables are
automatically set.

* `DATA_DIR`: absolute path to data directory

* When using `autoenv` to manage the shell environment, the following aliases
  are created. Unfortunately, aliases cannot be automatically set when `direnv`   manages the shell environment.

  * `jn`: start Jupyter notebook

### 2.4 Using Jupyter Notebook

#### Creating a New Jupyter Notebook

1. Change to the directory where Jupyter notebook should be saved.

    ```shell
    $ cd NOTEBOOK_DIR
    ```

2. Launch the Jupyter Notebook App.

    ```shell
    $ jupyter notebook
    ```

3. Use the menu under the `New` button to create a new Jupyter Notebook.

#### Opening an Existing Jupyter Notebook

1. Change to the directory containing the Jupyter notebook.

    ```shell
    $ cd NOTEBOOK_DIR
    ```

2. Launch the Jupyter Notebook App with the specified notebook file.

    ```shell
    $ jupyter notebook NOTEBOOK_FILE.ipynb
    ```

------------------------------------------------------------------------------

## 3. References

* J. Whitmore.
  ["Jupyter Notebook Best Practices for Data Science"][#whitmore-2016]
  (2016/09).

------------------------------------------------------------------------------

[-----------------------------INTERNAL LINKS-----------------------------]: #

[#1]: #1-overview
[#1.1]: #11-software-dependencies
[#1.2]: #12-directory-structure
[#1.3]: #13-template-files

[#2]: #2-usage
[#2.1]: #21-setting-up
[#2.2]: #22-conventions
[#2.3]: #23-environment
[#2.4]: #24-using-jupyter-notebook

[#3]: #3-references

[-----------------------------EXTERNAL LINKS-----------------------------]: #

[#whitmore-2016]:
  https://www.svds.com/tbt-jupyter-notebook-best-practices-data-science/
