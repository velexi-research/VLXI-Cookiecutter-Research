Velexi Scaffolding: Data Science Project
========================================

___Authors___  
Kevin T. Chu `<kevin@velexi.com>`

------------------------------------------------------------------------------

Table of Contents
-----------------

1. [Overview][#1]

   1.1. [Software Dependencies][#1.1]

   1.2. [Directory Structure][#1.2]

2. [Usage][#2]

   2.1. [Setting Up][#2.1]

   2.2. [Conventions][#2.2]

   2.3. [Creating a New Jupyter Notebook][#2.3]

   2.4. [Opening an Existing Jupyter Notebook][#2.4]

3. [References][#3]

------------------------------------------------------------------------------

1 Overview
----------

This project scaffolding is intended to support data science projects that
utilize Jupyter notebooks for experimentation and reporting. The design of
the scaffolding is based on the blog article
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
  data science, testing, and assessing code quality.

* `config`: directory containing template configuration files (e.g., `autoenv`
  configuration file)

* `data`: directory where project data should be placed

* `lab-notebook`: directory intended for Jupyter notebooks used for
  experimentation and development. Jupyter notebooks saved in this directory
  should (1) have a single author and (2) be dated.

* `reports`: directory intended for Jupyter notebooks that present and record
  final results. Jupyter notebooks saved in this directory should be polished,
  contain final analysis results, and be the work product of the entire data
  science team.

* `src`: directory intended for source code developed to support project

------------------------------------------------------------------------------

2 Usage
-------

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

  - Copy `config/env` to `.env` in project root directory.

  - Set template variables in `.env` (indicated by `{{ }}` notation).

### 2.2 Conventions

#### `lab-notebook` directory

* Jupyter notebooks in the `lab-notebook` directory should be named using the
  following convention: `YYYY-MM-DD-AUTHOR_INITIALS-BRIEF_DESCRIPTION.ipynb`.

    * Example: `2019-01-17-KTC-information_theory_analysis.ipynb`

* Depending on the nature of the project, it may be useful to organize lab
  notebook entries into sub-directories (e.g., by team member, by sub-project).

### 2.3 Creating a New Jupyter Notebook

1. Change to the directory where Jupyter notebook should be saved.

    ```bash
    $ cd NOTEBOOK_DIR
    ```

2. Launch the Jupyter Notebook App.

    ```bash
    $ jupyter notebook
    ```

3. Use the menu under the `New` button to create a new Jupyter Notebook.

### 2.4 Opening an Existing Jupyter Notebook

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
[#1.1]: #1-1-software-dependencies
[#1.2]: #1-2-directory-structure

[#2]: #2-usage
[#2.1]: #2-1-setting-up
[#2.2]: #2-2-conventions
[#2.3]: #2-3-creating-a-new-jupyter-notebook
[#2.4]: #2-4-opening-an-existing-jupyter-notebook

[#3]: #3-references

[-----------------------------EXTERNAL LINKS-----------------------------]: #
[#whitmore-2016]:
  https://www.svds.com/tbt-jupyter-notebook-best-practices-data-science/
