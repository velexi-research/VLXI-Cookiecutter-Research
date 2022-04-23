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

* Add files or folders to the Git and DVC repositories. FastDS will
  automatically detect large files and ask whether they should be added to DVC.

  ```shell
  $ fds add PATH
  ```

  __Note__. To add small data files to DVC, use `dvc` directly. Otherwise,
  the small data files will be added to the Git repository.

  ```shell
  $ dvc add PATH/TO/SMALL/DATA
  ```

* commit              commits added changes to git and dvc repository

* push                push commits to remote git and dvc repository

* save                saves all project files to a new version and pushes
                        them to your remote

* clone               clone git repository and pull dvc repository based on
                        tracked dvc config file

------------------------------------------------------------------------------
