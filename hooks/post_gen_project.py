"""
Apply post-generation project configuration and setup.
"""
# --- Imports

# Standard library
import os
from pathlib import Path
import subprocess


# --- Constants

_PROJECT_DIRECTORY = Path.cwd()

# --- Utility functions


def _remove_file(*filepath):
    """
    Remove file relative to _PROJECT_DIRECTORY.
    """
    try:
        Path(_PROJECT_DIRECTORY, *filepath).unlink()
    except FileNotFoundError:
        pass


# --- Main program

if __name__ == "__main__":

    # --- Preparations

    # Change to project directory
    os.chdir(_PROJECT_DIRECTORY)

    # --- Update project template files based on user configuration

    if "{{ cookiecutter.enable_julia }}" == "no":
        _remove_file("Project.toml")

    if "{{ cookiecutter.license }}" != "Apache License 2.0":
        _remove_file("NOTICE")

    # --- Set up Git repository for project

    # Initialize Git repository
    cmd = ["git", "init"]
    subprocess.run(cmd, check=True)

    # Commit cookiecutter files
    cmd = ["git", "add", "."]
    subprocess.run(cmd, check=True)

    cmd = ["git", "commit", "-m", "Initial commit."]
    subprocess.run(cmd, check=True)
