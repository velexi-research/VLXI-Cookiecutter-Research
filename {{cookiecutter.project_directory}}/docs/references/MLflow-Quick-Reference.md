MLflow Quick Reference
======================

__Authors__  
Kevin T. Chu `<kevin@velexi.com>`

-------------------------------------------------------------------------------

### Preliminaries

[MLflow Tracking](mlflow-tracking) is the only component of [MLflow][mlflow]
that is needed for general research projects. The other components of
[MLflow][mlflow] may be useful for projects involving data science and machine
learning models.

-------------------------------------------------------------------------------

Table of Contents
-----------------

1. [Using MLflow Tracking within a Jupyter Notebook][#1]

2. [Viewing MLflow Tracking Results][#2]

-------------------------------------------------------------------------------

## 1. Using MLflow Tracking within a Jupyter Notebook

MLflow Tracking facilitates support for recording experiment configuration
parameters and results. Below is a short set of instructions for setting up
MLflow experiment tracking within a Jupyter notebook.

1. Near the beginning of the Jupyter notebook, include a cell to set up MLflow
   Tracking.

   ```python
   # --- Set up MLflow Tracking

   # Set experiment
   mlflow.set_experiment(experiment_name)

   # Ensure that previous run (possibly failed) has been terminated by MLflow.
   if mlflow.active_run():
       mlflow.end_run()

   # Initialize dictionary for experiment results
   mlflow_results = {}
   ```

   __Note__. For situations where it is useful to group experiments by date
   or time, the `utils` Python module provides the `get_experiment_name()`
   function to faciliate consistent generation of date and time stamped
   experiment names.

2. Before running the experiment, include a cell to record all of the experiment
   parameters.

   ```python
   # --- Record experiment parameters

   mlflow.log_param("some-parameter", some_parameter)
   mlflow.log_param("another-parameter", another_parameter)
   ```

   __Note__. MLflow Tracking automatically includes a timestamp for each run
   of an experiment to facilitate comparison of different runs of an experiment
   using the same set of configuration parameters.

3. Throughout the Jupyter notebook, add results to `mlflow_results` and/or record
   individual results (saved as MLflow "metrics").

   ```python
   # Add a result to `mlflow_results`. This result will be saved at the end of the
   # Jupyter notebook
   mlflow_results["some-result"] = some_result

   # Record an individual result (as an MLflow "metric")
   mlflow.log_metric("another-result") = another_result
   ```

4. After the experiment is completed, include a cell to record the results.

   ```python
   # --- Record experiment results

   mlflow.log_dict(mlflow_results, "results.json")
   ```

5. At the end of the Juypter notebook, include a cell to end the MLflow run.

   ```python
   # --- End current MLflow run

   mlflow.end_run()
   ```

-------------------------------------------------------------------------------

## 2. Viewing MLflow Tracking Results

MLflow Tracking provides support for reviewing and comparing experiments. It
is particularly useful when comparing results across multiple runs of the same
experiment with different parameter settings. For basic research projects, the
following short set of steps should be sufficient to viewing MLflow Tracking
results.

* Change to the directory containing the `mlruns` directory (usually the
  project root directory).

  ```shell
  $ cd PROJECT_DIR
  ```

* Start a local MLflow Tracking UI server.

  ```shell
  $ mlflow ui
  ```

  __Note__. The MLflow tracking server can also be used to serve experiment
  tracking data.

  ```shell
  $ mlflow server
  ```

* View results in a web browser by opening the URL provided displayed to the
  console. By default, the Mlflow tracking server listens at `localhost:5000`.

-------------------------------------------------------------------------------

[-----------------------------INTERNAL LINKS-----------------------------]: #

[#1]: #1-using-mlflow-tracking-within-a-jupyter-notebook

[#2]: #2-viewing-mlflow-tracking-results

[-----------------------------EXTERNAL LINKS-----------------------------]: #

[mlflow]: https://www.mlflow.org

[mlflow-tracking]: https://www.mlflow.org/docs/latest/tracking.html
