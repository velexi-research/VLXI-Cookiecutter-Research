Automated Testing
=================

__Authors__  
Kevin T. Chu `<kevin@velexi.com>`

------------------------------------------------------------------------------

This project is configured to support

* automated testing of code located in the `src` directory and

* analysis of how well the tests cover of the source code (i.e., coverage
  analysis).

For an example of how to write basic automated tests, see the
`tests/test_utils.py` file.

------------------------------------------------------------------------------

## Running Automated Tests

* Run all of the tests.

  ```shell
  $ make test
  ```

* Run all of the tests in fail-fast mode (i.e., stop after the first failing
  test).

  ```shell
  $ make fast-test
  ```

* After running all tests, run `pylint` on all source code files.

  ```shell
  $ make full-test
  ```

------------------------------------------------------------------------------
