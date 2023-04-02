#!/usr/bin/env bash
#------------------------------------------------------------------------------
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
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Cookiecutter post-generation script
#------------------------------------------------------------------------------

# --- Update project template files based on user configuration

# Remove Project.toml if Julia is not enabled
if [[ "{{ cookiecutter.enable_julia }}" == "no" ]]; then
    rm Project.toml
fi

# Remove NOTICE file if license is not Apache License 2.0
if [[ "{{ cookiecutter.license }}" != "Apache License 2.0" ]]; then
    rm NOTICE
fi

# Force LICENSE file to be an empty file if an empty license is selected
if [[ "{{ cookiecutter.license }}" == "None" ]]; then
    rm LICENSE
    touch LICENSE
fi

# --- Set up Git repository for project

# Initialize Git repository
git init

# Commit cookiecutter files
git add .
git commit -m "Initial commit."
