{% if cookiecutter.license == 'Apache License 2.0' %}#   Copyright {% now 'utc', '%Y' %} {{ cookiecutter.author }}
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
"""
Unit tests for `utils.py` module.
"""{% else %}"""
Unit tests for `utils.py` module.
"""{% endif %}

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
