"""
Unit tests for `utils.py` module.
"""
# --- Imports

# Standard library
import datetime

# Local imports
import utils


# --- Tests

def test_get_experiment_name():
    """
    Test utils.test_get_experiment_name().
    """
    # --- Preparations

    expected_date = datetime.date.today().isoformat()

    # --- Tests

    # include_timestamp = False (default)
    description = "Experiment Description"
    description_slugified = "experiment_description"
    experiment_name = utils.get_experiment_name(description)
    expected_experiment_name = f"{expected_date}-{description_slugified}"
    assert experiment_name == expected_experiment_name

    # include_timestamp = True
    description = "Experiment Description"
    description_slugified = "experiment_description"
    experiment_name = utils.get_experiment_name(description,
                                                include_timestamp=True)
    experiment_name_parts = experiment_name.split('-')
    assert len(experiment_name_parts) == 5
    assert '-'.join(experiment_name_parts[0:3]) == expected_date
    assert experiment_name_parts[-1] == description_slugified
