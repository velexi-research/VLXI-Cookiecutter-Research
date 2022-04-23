Project Environment
===================

__Authors__  
Kevin T. Chu `<kevin@velexi.com>`

------------------------------------------------------------------------------

__Note__. This reference only applies if you are using `direnv` to manage
your project environment.

------------------------------------------------------------------------------

### Environment Variables

If `direnv` is enabled, the following environment variables are automatically
set whenever you change into the project directory.

* `DATA_DIR`: path to `data` directory

* `SRC_DIR`: path to `src` directory

* `PYTHONPATH`: search paths for Python packages and modules
{% if cookiecutter.enable_julia == 'yes' %}
* `JULIA_LOAD_PATH`: search paths for Julia packages and modules
{% endif %}
* `MLFLOW_TRACKING_URI`: path to directory where MLflow stores run data

### Customizing the Project Environment

The following variables can be set in the `.envrc` file to customize the
project environment.

* `PATH_EXTRA`: space-delimited list of paths to add to the `PATH` environment
  variable

* `PYTHONPATH_EXTRA`: space-delimited list of paths to add to the `PYTHONPATH`
  environment variable

* `JULIA_LOAD_PATH_EXTRA`: space-delimited list of paths to add to the
  `JULIA_LOAD_PATH` environment variable

* `MLFLOW_TRACKING_URI`: URI of MLflow tracking server. By default,
  `MLFLOW_TRACKING_URI` is set to `/PROJECT_ROOT_DIR/mlruns`.

------------------------------------------------------------------------------
