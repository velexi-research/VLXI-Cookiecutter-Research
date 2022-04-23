FastDS Quick Reference
======================

__Authors__  
Kevin T. Chu `<kevin@velexi.com>`

------------------------------------------------------------------------------

## FastDS Commands

* Display status of the Git and DVC repositories.

  ```shell
  $ fds status
  ```

* Add files or folders to the Git and DVC repositories. FastDS automatically
  detects large files and ask whether they should be added to DVC.

  ```shell
  $ fds add PATH
  ```

  __Note__. To add small data files to DVC, you must use `dvc` instead of `fds`.
  Otherwise, the small data files will be added to the Git repository, not the
  DVC repository.

  ```shell
  $ dvc add PATH/TO/SMALL/DATA
  ```

* Commit staged changes to the Git and DVC repositories.

  ```shell
  $ fds commit COMMIT_MESSAGE
  ```

  where `COMMIT_MESSAGE` is the commit message to use when committing the
  changes to Git.

* Push commits to the remote Git and DVC repositories.

  ```shell
  $ fds push
  ```

* Add, commit, and push all project files in the current directory (including
  untracked files).

  ```shell
  $ fds save COMMIT_MESSAGE
  ```

  where `COMMIT_MESSAGE` is the commit message to use when committing the
  changes to Git.

  __Note__. `fds save` is equivalent to

  ```shell
  $ fds add .
  $ fds commit -m COMMIT_MESSAGE
  $ fds push
  ```

* Get the code and data for a project.

  ```shell
  $ fds clone GIT_REPO_URL
  ```

  where `GIT_REPO_URL` is the URL of the project's remote Git repository.

  __Note__. `fds clone GIT_REPO_URL` is equivalent to

  ```shell
  $ git clone GIT_REPO_URL
  $ cd PROJECT_DIR
  $ dvc pull
  ` ``

------------------------------------------------------------------------------
