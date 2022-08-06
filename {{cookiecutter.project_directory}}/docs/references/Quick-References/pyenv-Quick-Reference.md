pyenv Quick Reference
=====================

__Authors__  
Kevin T. Chu `<kevin@velexi.com>`

-------------------------------------------------------------------------------

[pyenv][pyenv] is a simple CLI tool for managing Python versions.

-------------------------------------------------------------------------------

### Installing a Python Version

* Get a list of the available Python versions.

  ```shell
  $ pyenv install -l
  ```

* Install the desired Python version. For example, if you want to install
  Python 3.8.13, execute the following command:

  ```shell
  $ pyenv install 3.8.13
  ```

### Setting a Local Python Version

`pyenv` supports configuring the Python version used within a specific
directory (without affecting the Python version used elsewhere on the system).

* Show a list of the available Python versions.

  ```shell
  $ pyenv versions
  ```

* Configure the local directory to use a specific Python version. For example,
  to set the local Python version to 3.8.13, execute the following command:

  ```shell
  $ pyenv local 3.8.13
  ```

  __Note__: this command will make Python 3.8.13 the default Python version
  _only_ for the directory it is executed in. The Python version used outside
  of the directory will be unaffected.

[-----------------------------EXTERNAL LINKS-----------------------------]: #

[pyenv]: https://github.com/pyenv/pyenv
