pyenv Quick Reference
=====================

__Authors__  
Kevin T. Chu `<kevin@velexi.com>`

-------------------------------------------------------------------------------

[pyenv][pyenv] is a simple CLI tool for managing Python versions.

-------------------------------------------------------------------------------

### Installing `pyenv`

* See the [installation instructions][pyenv-installation] from the `pyenv`
  website.

### Installing a Python Version

* Get a list of the available Python versions for installation.

  ```shell
  $ pyenv install -l
  ```

* Install the desired Python version. For example, if you want to install
  Python 3.8.13, execute the following command:

  ```shell
  $ pyenv install 3.8.13
  ```

### Getting a List of Installed Python Versions

* Show a list of the installed Python versions.

  ```shell
  $ pyenv versions
  ```

### Setting a User-Level Python Version

`pyenv` supports configuring the default Python version for a user (without
affecting the Python version used elsewhere on the system). For example, to
set the default Python version of the current user to 3.8.13, execute the
following command:

```shell
$ pyenv global 3.8.13
```

__Note__: this command will make Python 3.8.13 the default Python version
for the current user _only_. The default Python version for other users on the
system will be unaffected.

### Setting a Directory-Level Python Version

`pyenv` supports configuring the Python version used within a specific
directory (without affecting the Python version used by the current user
elsewhere on the system). For example, to set the Python version used in the
current directory to 3.8.13, execute the following command:

```shell
$ pyenv local 3.8.13
```

__Note__: this command will make Python 3.8.13 the default Python version
_only_ for the directory it is executed in. The default Python version outside
of the directory (even for the same user) will be unaffected.

[-----------------------------EXTERNAL LINKS-----------------------------]: #

[pyenv]: https://github.com/pyenv/pyenv

[pyenv-installation]: https://github.com/pyenv/pyenv#installation
