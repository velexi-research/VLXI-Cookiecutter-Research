"""
Setup steps to perform after project creation.
"""
# --- Imports

# Standard library
from pathlib import Path


# --- Constants

PROJECT_DIRECTORY = Path.cwd()


# --- Utility functions

def _remove_file(*filepath):
    try:
        Path(PROJECT_DIRECTORY, *filepath).unlink()
    except FileNotFoundError:
        pass


# --- Main program

if __name__ == "__main__":

    if "{{ cookiecutter.enable_julia }}" == "no":
        _remove_file("Project.toml")
