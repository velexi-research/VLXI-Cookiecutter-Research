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

* Compatible with standard version control software.

* Automatically saves HTML and `*.py` versions of Jupyter notebooks to
  facilitate review of both (1) data science results and (2) implementation
  code.

* Supports common data science workflows (for both individuals and teams).

### 1.1 Software Dependencies

#### Base Requirements

* Python

#### Recommended Python Packages ####

* `autoenv`
* `virtualenv`
* `virtualenvwrapper`

### 1.2 Directory Structure

    README.markdown
    requirements.txt
    config/
    data/
    lab-notebook/
    reports/
    src/

* `README.markdown`: this file

* `requirements.txt`: `pip` requirements file containing Python packages for
  data science, testing, and assessing code quality

* `config`: directory containing template configuration files (e.g., `autoenv`
  configuration file)

* `data`: directory where project data should be placed. __Note__: data placed
  in this directory ___does not___ necessarily need to be committed to the git
  repository. For projects with large datasets, committing the data to the git
  repository is ___discouraged___.

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

* Create Python virtual environment for project.

    ```bash
    $ mkvirtualenv -p /PATH/TO/PYTHON PROJECT_NAME
    ```

* Install required Python packages.

    ```bash
    $ pip install -r requirements.txt
    ```

* Set up autoenv.

  - Copy `config/env.template` to `.env` in project root directory.

  - Set template variables in `.env` (indicated by `{{ }}` notation).

### 2.2 Conventions

#### `lab-notebook` directory

* Jupyter notebooks in the `lab-notebook` directory should be named using the
  following convention: `YYYY-MM-DD-AUTHOR_INITIALS-BRIEF_DESCRIPTION.ipynb`.

    * Example: `2019-01-17-KTC-information_theory_analysis.ipynb`

* Depending on the nature of the project, it may be useful to organize lab
  notebook entries into sub-directories (e.g., by team member, by sub-project).

### 2.3 Environment

* TODO

* autoenv
  - `DATA_DIR`

* aliases
  - jn

### 2.4 Using Jupyter Notebook

#### Creating a New Jupyter Notebook

1. Change to the directory where Jupyter notebook should be saved.

    ```bash
    $ cd NOTEBOOK_DIR
    ```

2. Launch the Jupyter Notebook App.

    ```bash
    $ jupyter notebook
    ```

3. Use the menu under the `New` button to create a new Jupyter Notebook.

#### Opening an Existing Jupyter Notebook

1. Change to the directory containing the Jupyter notebook.

    ```bash
    $ cd NOTEBOOK_DIR
    ```

2. Launch the Jupyter Notebook App with the specified notebook file.

    ```bash
    $ jupyter notebook NOTEBOOK_FILE.ipynb
    ```

------------------------------------------------------------------------------

3 References
------------

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
