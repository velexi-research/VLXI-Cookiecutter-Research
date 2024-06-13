Poetry Quick Reference
======================

__Authors__  
Kevin T. Chu `<kevin@velexi.com>`

__Version__: 2024-06-13

--------------------------------------------------------------------------------------------

[Poetry][poetry] is a useful Python package and dependency management tool.
It also provides support for managing Python environments, building and
packaging Python projects, and publishing Python packages.

--------------------------------------------------------------------------------------------

## Managing Project Dependencies

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

## Managing Virtual Environments

### Basic Commands

All of the following commands operate on the Python virtual environments for
a specific project defined by a `pyproject.toml` file. They all require that a
`pyproject.toml` file exists in the current directory or an ancestor of the
current directory.

* Activate or create a virtual environment using one of the following command
  variations.

  * Use a specific Python executable for the virtual environment.

    ```shell
    $ poetry env use /full/path/to/python
    ```

  * Use a Python executable on your `PATH` for the virtual environment.
    For instance,

    ```shell
    $ poetry env use python3.11
    ```

    or

    ```shell
    $ poetry env use 3.11
    ```

* Deactivate a virtual environment.

  ```shell
  $ poetry env use system
  ```

* Display information about the virtual environment.

  ```shell
  $ poetry env info
  ```

* Delete a virtual environment using one of the following command variations.

  ```shell
  $ poetry env remove /full/path/to/python
  $ poetry env remove python3.11
  $ poetry env remove 3.11
  $ poetry env remove package-name-12345678-py3.11
  ```

  The full environment name in the last variation is available in the output
  of the `poetry env info` command.

### Configuration

* __In-Project Virtual Environments__. By default, `poetry` stores Python virtual
  environments in a (user-level) central location. However, we recommend configuring
  `poetry` to use an in-project virtual environment for ease of maintenance (e.g. deleting
  the entire project directory automatically deletes the Python virtual environment).

  * To configure `poetry` to use in-project virtual environments for all projects, use

    ```shell
    $ poetry config virtualenvs.in-project true
    ```

  * To configure `poetry` to use in-project virtual environments locally within a specific
    projects, use

    ```shell
    $ poetry config --local virtualenvs.in-project true
    ```

    This command will create a `poetry.toml` file that can be added to the project code
    repository.

### References

* [Poetry Docs: Managing environments][poetry-managing-environments]

--------------------------------------------------------------------------------------------

[----------------------------------- EXTERNAL LINKS -----------------------------------]: #

[poetry]: https://python-poetry.org/
[poetry-managing-environments]: https://python-poetry.org/docs/managing-environments/
