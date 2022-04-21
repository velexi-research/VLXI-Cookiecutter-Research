Velexi Research Project Cookiecutter: Project Structure Reference
=================================================================

* `requirements.txt`: `pip` requirements file containing Python packages for
  project (e.g., data science, testing, and assessing code quality packages)

* `Project.toml`: Julia package management file containing Julia package
  dependencies. It is updated whenever new Julia packages are added via the
  REPL. This file may be safely removed if Julia is not required for the
  project.

* `tox.ini`: configuration file for tox testing framework

* `bin`: directory where scripts and programs should be placed

* `data`: directory where project data should be placed

    * __Recommendation__: data placed in the `data` directory should be managed
      using DVC (or an analogous tool) rather than being included in the `git`
      repository. This is especially important for projects with large datasets
      or datasets containing sensitive information. For projects with small
      datasets that do not contain sensitive information, it may be reasonable
      to have the data contained in the `data` directory be managed directly by
      `git`.

* `docs`: directory where project documentation should be placed

* `models`: directory where deployable models should be placed

* `notebooks`: directory containing Jupyter notebooks used for research phase
  work (e.g., exploration and development of ideas, DS/ML experiments). Each
  Jupyter notebook in this directory should (1) be dated and (2) have the
  initials of the person who created it. When an existing notebook is modified,
  it should be saved to a new file with a name constructed from the
  modification date and initials of the person who created the new notebook.

* `references`: directory where reference materials (e.g., articles, data
  manuals, etc.) should be placed

* `reports`: directory containing reports (in any format) that summarize
  research results. When a report is prepared as a Jupyter notebook, the
  notebook should be polished, contain final analysis results (not preliminary
  results), and is usually the work product of the entire data science team.

* `src`: directory containing source code to support the project (e.g.,
  custom code developed for the project, utility modules, etc.)
