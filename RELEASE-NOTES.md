Velexi Research Project Cookiecutter Release Notes
==================================================

-------------------------------------------------------------------------------
0.8.13 (2024-01-12)
===================
### Cookiecutter Template
* Exclude `.ipynb` files from `pretty-format-json` pre-commit hook.
* Update package dependency versions.

### Cookiecutter Development
* Update package dependency versions.

-------------------------------------------------------------------------------
0.8.12 (2023-12-28)
===================
### Cookiecutter Template
* Update package dependencies.

### Cookiecutter Development
* Update package dependencies.

-------------------------------------------------------------------------------
0.8.11 (2023-12-15)
===================
### Cookiecutter Template
* Update package dependencies to fix security vulnerability.

### Cookiecutter Development
* Update package dependencies.

-------------------------------------------------------------------------------
0.8.10 (2023-10-19)
===================
### Cookiecutter Template
* Update default Python version to fix security vulnerability.

-------------------------------------------------------------------------------
0.8.9 (2023-10-19)
==================
### Cookiecutter Template
* Fix bugs in Makefile.
* Update Jupyter quick reference.
* Update README.
* Update package dependencies.

### Cookiecutter Development
* Update package dependencies.

-------------------------------------------------------------------------------
0.8.8 (2023-06-29)
==================
### Cookiecutter Template
* Update Makefile "clean" target.
* Update package dependencies.
* Update dependencies in pre-commit configuration.

### Cookiecutter Development
* Update package dependencies.

-------------------------------------------------------------------------------
0.8.7 (2023-06-19)
==================
### Cookiecutter Template
* Improve organization of project Python package.
* Polish .gitignore.
* Polish pre-commit configuration.

### Cookiecutter Development
* Polish .gitignore.
* Polish pre-commit configuration.

-------------------------------------------------------------------------------
0.8.6 (2023-06-18)
==================
### Cookiecutter Template
* Fix pre-commit configuration bug.
  - Add --allow-missing-credentials option for detect-aws-credentials.
* Simplify pyproject.toml.
  - Merge dependencies from "test" and "dev" groups into main dependency list.
* Update package dependency versions.

### Cookiecutter Development
* Update package dependency versions.

-------------------------------------------------------------------------------
0.8.5 (2023-05-22)
==================
### Cookiecutter Template
* Polish dot-envrc.
* Update package dependency versions.

### Cookiecutter Development
* Polish dot-envrc.
* Update package dependency versions.

-------------------------------------------------------------------------------
0.8.4 (2023-05-21)
==================
### Cookiecutter Template
* Fix pytest configuration bugs in Makefile.
* Update package dependency versions.

### Cookiecutter Development
* Update package dependency versions.

-------------------------------------------------------------------------------
0.8.3 (2023-04-22)
==================
### Cookiecutter Template
* Fix DVC bugs in .gitignore.
* Update package dependency versions.

-------------------------------------------------------------------------------
0.8.2 (2023-04-09)
==================
### Cookiecutter Template
* Fix package dependency version incompatibilities.
* Polish documentation.

-------------------------------------------------------------------------------
0.8.1 (2023-04-08)
==================
### Cookiecutter Template
* Slugify project name in places where special characters may cause problems
  (e.g., URLs and directory names).
* Polish code and documentation.

### Cookiecutter Development
* Add Apache license incantations to cookiecutter hook scripts.
* Update private cookiecutter variables.

-------------------------------------------------------------------------------
0.8.0 (2023-04-02)
==================
### Cookiecutter Template
* Update cookiecutter parameters.
  * "package_name" is no longer user-defined. It is now automatically set.
* Remove "full-test" target from Makefile.
* Reorganize dependency groups in `pyproject.toml`.
* Update package dependency versions.
* Polish code and documentation.

### Cookiecutter Development
* Update package dependency versions.

-------------------------------------------------------------------------------
0.7.5 (2022-12-24)
==================
### Cookiecutter Template Enhancements
* Restructure repository to be more tuned for research workflows.
* Update pre-commit configuration to allow larger file sizes (e.g., Jupyter
  notebooks with figures).
* Change default project name in `pyproject.toml` to use dashes instead of
  underscores.
* Update package dependencies to address security vulnerabilities.
* Update README template.

-------------------------------------------------------------------------------
0.7.4 (2022-10-22)
==================
### Cookiecutter Template Enhancements
* Improve pytest configuration.

-------------------------------------------------------------------------------
0.7.3 (2022-10-17)
==================
### Cookiecutter Template Enhancements
* Fix bug in authors field of pyproject.toml files.
* Update documentation.

-------------------------------------------------------------------------------
0.7.2 (2022-10-14)
==================
### Cookiecutter Template Enhancements
* Move quick references to `extras` directory to separate them from project
  documentation.
* Update README template.

### Cookiecutter Development Enhancements
* Simplify logic for default values in cookiecutter.json.
* Update documentation.

-------------------------------------------------------------------------------
0.7.1 (2022-10-10)
==================
### Bug Fixes
* Fix symbolic links to documentation.

-------------------------------------------------------------------------------
0.7.0 (2022-10-10)
==================
### Cookiecutter Template Enhancements
* Simplify user-specified cookiecutter parameters.
* Add pre-generation hook to validate package name.
* Improve consistency of Jinja template variable expressions.
* Fix bugs.

### Cookiecutter Development Enhancements
* Migrate cookiecutter hooks to shell scripts.
* Remove unneeded package dependencies for cookiecutter development.
* Simplify pre-commit hooks.
* Update documentation.

-------------------------------------------------------------------------------
0.6.0 (2022-10-08)
==================
### Cookiecutter Template Enhancements
* Consolidate Python project metadata and tool configurations into
  pyproject.toml.
* Add and streamline integrations with code quality tools: pytest, coverage,
  flake8, black, git pre-commit hooks.
* Migrate to `pdoc` from `pdoc3`.
* Update documentation.
* Update all files to pass all pre-commit checks.
* Improve application of Apache License 2.0.

### Cookiecutter Template Bug Fixes
* Fix bugs in Jinja2 logic in template files.
* Remove obsolete configurations and files.

## Cookiecutter Development Enhancements
* Add integrations with tools for supporting code quality: black and git
  pre-commit hooks.
* Update all files to pass all pre-commit checks.
* Improve application of Apache License 2.0.

-------------------------------------------------------------------------------
0.5.2 (2022-10-04)
==================
* Fix errors in README files.
* Remove obsolete files.

-------------------------------------------------------------------------------
0.5.1 (2022-10-04)
==================
* Improve application of Apache License 2.0 (for both the cookiecutter and
  projects generated by the cookiecutter).
* Update README files.

-------------------------------------------------------------------------------
0.5.0 (2022-10-03)
==================
* Update pyproject.toml files to use Poetry dependency group syntax.
* Update documentation.
* Update dependencies to address security vulnerabilities.

-------------------------------------------------------------------------------
0.4.6 (2022-08-24)
==================
* Update Python package dependencies.
* Update README (improve instructions for setting up virtual environments).
* Update quick reference for `poetry`.

-------------------------------------------------------------------------------
0.4.5 (2022-08-06)
==================
* Update Python package dependencies.
* Add license field to pyproject.toml.
* Update README file.
* Add quick reference for `pyenv`.

-------------------------------------------------------------------------------
0.4.4 (2022-06-09)
==================
* Bump 'cookiecutter' dependency from 1.7.3 to 2.1.1 to fix security
  vulnerability.

-------------------------------------------------------------------------------
0.4.3 (2022-05-31)
==================
* Add guidelines for organizing research notes.
* Update cookiecutter project and template documentation.
* Update Python package dependencies.
* Fix typos in LICENSE.

-------------------------------------------------------------------------------
0.4.2 (2022-05-25)
==================
* Update package dependencies for cookiecutter template to fix security
  vulnerability.

-------------------------------------------------------------------------------
0.4.1 (2022-05-16)
==================
* Update package dependencies for cookiecutter template.
* Clean up `.gitignore`.
* Update `version` number in `pyproject.toml`.

-------------------------------------------------------------------------------
0.4.0 (2022-05-10)
==================
* Added quick reference for using `pdoc` to auto-generate API documentation
  from source code.
* Removed `version` cookiecutter variable (version numbers are not needed
  for research projects).
* Updated and reoganized documentation.
* Improved Makefile `help` documentation.

-------------------------------------------------------------------------------
0.3.1 (2022-05-06)
==================
* Added `pdoc3` as default package for supporting auto-generation of
  documentation.
* Updated documentation.
* Improved license format.

-------------------------------------------------------------------------------
0.3.0 (2022-04-23)
==================
* Restructured project to be a cookiecutter instead of a template.
* Changed repository name from "Velexi Template: Data Science Project" to
  "Velexi Research Project Cookiecutter".
* Added and updated documentation.

-------------------------------------------------------------------------------
0.2.1 (2021-08-31)
==================
* Rename "research" directory to "notebooks".
* Migrate to semantic version numbers without "v" prefix.

-------------------------------------------------------------------------------
0.2.0 (2021-06-13)
==================
* Reorganize template structure.
* Update documentation.
* Improve support for common data science workflows.
  * Add DVC to Python requirements. Add documentation for DVC.
  * Add support for MLflow and Conda in `envrc.example` and `env.example`.
* Simplify Julia setup steps.

-------------------------------------------------------------------------------
0.1.3 (2021-02-10)
==================
* Fix minor typo in README-Template-Usage.md.

-------------------------------------------------------------------------------
0.1.2 (2021-02-10)
==================
* Fix errors and improve README files.
* Add standard data directory (that is ignored by git).

-------------------------------------------------------------------------------
0.1.1 (2020-11-24)
==================
* Add support for Julia.
* Update README file.

-------------------------------------------------------------------------------
0.1.0 (2020-09-18)
==================
* Initial version of package with core functionality implemented and tested.

-------------------------------------------------------------------------------
