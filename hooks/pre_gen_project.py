# ------------------------------------------------------------------------------
#   Copyright 2019 Velexi Corporation
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
# ------------------------------------------------------------------------------
"""
Cookiecutter pre-generation script
"""

import re
import sys


PACKAGE_NAME_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

package_name = "{{ cookiecutter.__package_name }}"

if not re.match(PACKAGE_NAME_REGEX, package_name):
    print()
    print(f'ERROR: "{package_name}" is not a valid Python package name')
    sys.exit(1)
