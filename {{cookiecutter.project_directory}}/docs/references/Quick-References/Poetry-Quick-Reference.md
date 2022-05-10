Poetry Quick Reference
======================

__Authors__  
Kevin T. Chu `<kevin@velexi.com>`

-------------------------------------------------------------------------------

[Poetry][poetry] is a useful Python package and dependency management tool.
It also provides support for managing Python environments, building and
packaging Python projects, and publishing Python packages.

-------------------------------------------------------------------------------

## Dependency Management Commands

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

-------------------------------------------------------------------------------

## Package Management Commands

* Install the package dependencies included in `pyproject.toml`.

  ```shell
  $ poetry install
  ```

* Update the package dependencies to the latest available versions.

  ```shell
  $ poetry update
  ```

  __Note__. This to equivalent to deleting the `poetry.lock` file and
  running `poetry install`.

-------------------------------------------------------------------------------

[-----------------------------EXTERNAL LINKS-----------------------------]: #

[poetry]: https://python-poetry.org/
