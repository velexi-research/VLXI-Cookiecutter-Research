pdoc Quick Reference
====================

__Authors__  
Kevin T. Chu `<kevin@velexi.com>`

------------------------------------------------------------------------------

[pdoc][pdoc3] is a simple CLI tool that generates API documentation from
Python source code (docstrings).

This project is configured to support auto-generation of API documentation
for Python code in the `src` directory, but `pdoc` can be used directly to
generate documentation for Python modules and packages in any location.

------------------------------------------------------------------------------

## Generating API Documentation

### Using the project `make` rules

* Generate documentation for Python code in the `src` directory.

  ```shell
  $ make docs
  ```

  Documentation is generated in HTML format and written to the `docs/api`
  directory.

### Using `pdoc`

* Generate HTML-formatted documentation for a Python package or module.

  ```shell
  $ pdoc --html MODULE -o DOC_DIR
  ```

  __Notes__

  * `MODULE` can be (1) a path to a file or directory or (2) the name of an
    importable Python package or module.

  * Documentation written to the `DOC_DIR` directory.

------------------------------------------------------------------------------

[-----------------------------EXTERNAL LINKS-----------------------------]: #

[pdoc3]: https://pdoc3.github.io/pdoc/
