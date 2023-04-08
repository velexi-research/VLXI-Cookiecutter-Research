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
Utility functions.
"""{% else %}"""
Utility functions.
"""{% endif %}

# --- Imports

# Standard library
import datetime

# External packages
from slugify import slugify


# --- Utility functions


def get_experiment_name(description: str, include_timestamp: bool = False) -> str:
    """
    Get standard experiment name.

    Parameters
    ----------
    description: brief description

    include_timestamp: when True, include a timestamp in the experiment name

    Return value
    ------------
    experiment name
    """
    description_slugified = slugify(description, separator="_")

    datestamp = datetime.date.today().isoformat()
    if include_timestamp:
        timestamp = datetime.datetime.now().strftime("-%H%M%S")
    else:
        timestamp = ""

    experiment_name = f"{datestamp}{timestamp}-{description_slugified}"

    return experiment_name
