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
    try:
        Path(_PROJECT_DIRECTORY, *filepath).unlink()
    except FileNotFoundError:
        pass


# --- Main program

if __name__ == "__main__":

    # --- Update project template files based on user configuration

    if "{{ cookiecutter.enable_julia }}" == "no":
        _remove_file("Project.toml")

    # --- Initialize Git repository project

    os.chdir(_PROJECT_DIRECTORY)
    cmd = ["git", "init"]
    subprocess.run(cmd, check=True)
