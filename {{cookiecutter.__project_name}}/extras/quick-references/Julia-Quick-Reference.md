Julia Quick Reference
=====================

__Authors__  
Kevin T. Chu `<kevin@velexi.com>`

-------------------------------------------------------------------------------

Table of Contents
-----------------

1. [Julia Package Manager Commands][#1]

2. [Making a Julia Package Importable][#2]

-------------------------------------------------------------------------------

## 1. Julia Package Manager Commands

* Activate Julia package manager REPL.

  ```julia
  julia> ]

  (...) pkg>
  ```

* Display the list of Julia package dependencies.

  ```julia
  (...) pkg> status
  ```

  or

  ```julia
  (...) pkg> st
  ```

* Add a Julia package dependency.

  ```julia
  (...) pkg> add PKG_NAME
  ```

* Remove a Julia package dependency.

  ```julia
  (...) pkg> remove PKG_NAME
  ```

  or

  ```julia
  (...) pkg> rm PKG_NAME
  ```

-------------------------------------------------------------------------------

## 2. Making a Julia Package Importable

To make Julia code in the `src` directory importable using the `import X`
syntax in Julia, the following conditions must be satisified.

* `Project.toml` must contain the name of the Julia package/module.

  ```toml
  name = "X"
  ```

* A file named `X.jl` must exist in the `src` directory.

* If `/PATH/TO/PROJECT_DIR` is the parent directory of the `src` directory, it
  must be included in

  * the `JULIA_LOAD_PATH` environment variable

    ```shell
    $ export JULIA_LOAD_PATH=/PATH/TO/PROJECT_DIR:$JULIA_LOAD_PATH
    ```

    or

  * the `LOAD_PATH` Julia variable

    ```julia
    julia> push!(LOAD_PATH, "/PATH/TO/PROJECT_DIR")
    ```

-------------------------------------------------------------------------------

[-----------------------------INTERNAL LINKS-----------------------------]: #

[#1]: #1-julia-package-manager-commands

[#2]: #2-making-a-julia-package-importable
