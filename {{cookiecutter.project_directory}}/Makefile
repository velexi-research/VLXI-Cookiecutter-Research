# --- Makefile parameters

# Default rule
.DEFAULT_GOAL := help

# Source directories
SRC_DIR=src
CODE_DIRS=${SRC_DIR} tests

# Testing parameters
NPROCS=auto

PYTEST_SEARCH_PATHS=${CODE_DIRS}
PYTEST_OPTIONS=-n ${NPROCS} --cov=${SRC_DIR}
PYTEST_PYLINT_OPTIONS=

# --- Testing rules

.PHONY: test fast-test full-test \
        coverage-report coverage-html

## Run all tests
test:
	py.test ${PYTEST_SEARCH_PATHS} ${PYTEST_OPTIONS} ${PYTEST_PYLINT_OPTIONS}

## Run tests in fail-fast mode (i.e., stop at first failure)
fast-test:
	make test PYTEST_OPTIONS="-x ${PYTEST_OPTIONS}"

## Run comprehensive tests (includes linting with pylint)
full-test:
	make test PYTEST_PYLINT_OPTIONS="--pylint --pylint-error-types=EF";

.coverage:
	-make test

## Generate basic coverage report
coverage-report: .coverage
	coverage report -m

## Generate coverage report in HTML format
coverage-html: .coverage
	coverage html -d coverage

# --- Code quality rules

.PHONY: lint \
		radon-mi radon-mi-fail radon-cc radon-cc-fail radon-raw

## Lint code using flake8
lint:
	flake8 ${CODE_DIRS}

## Compute the Maintainability Index for source code files.
radon-mi:
	radon mi ${CODE_DIRS} -s --sort

## Compute the Maintainability Index for source code files.
## Show only failing results (i.e., that do not have an "A" rating).
radon-mi-fail:
	radon mi ${CODE_DIRS} -xB -s --sort

## Compute the Cyclomatic Complexity (CC) for source code files.
radon-cc:
	radon cc ${CODE_DIRS} --total-average

## Compute the Cyclomatic Complexity (CC) for source code files.
## Show only failing results (i.e., that do not have an "A" rating).
radon-cc-fail:
	radon cc ${CODE_DIRS} -nC --average

## Show the raw source code metrics computed by the `radon` tool.
radon-raw:
	radon raw ${CODE_DIRS} -s

# --- Documentation rules

.PHONY: docs docs-pdf

## Generate API documentation in HTML format.{% if cookiecutter.enable_julia == 'yes' %} Note: only generates docs for Python modules.{% endif %}
docs:
	pdoc --html -o docs/api/html ${SRC_DIR}

## Generate API documentation in Markdown format.{% if cookiecutter.enable_julia == 'yes' %} Note: only generates docs for Python modules.{% endif %}
docs-md:
	pdoc --pdf ${SRC_DIR} > docs/api/api.md

# --- Utility rules

.PHONY: clean

## Clean up project directory (e.g., remove all compiled code, coverage files,
## etc.)
clean:
	find . -type d -name "__pycache__" -delete  # compiled python
	find . -type f -name "*.py[co]" -delete  # compiled python
	rm -rf .cache  # pytest
	rm -rf .coverage .coverage.* coverage htmlcov  # coverage
	find . -name "*.log" -exec rm -f {} \;  # demos

# --- Makefile Self-Documentation

# Inspired by
# <http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html>
#
# sed script explained:
# /^##/:
# 	* save line in hold space
# 	* purge line
# 	* Loop:
# 		* append newline + line to hold space
# 		* go to next line
# 		* if line starts with doc comment, strip comment character off and loop
# 	* remove target prerequisites
# 	* append hold space (+ newline) to line
# 	* replace newline plus comments by `---`
# 	* print line
# Separate expressions are necessary because labels cannot be delimited by
# semicolon; see <http://stackoverflow.com/a/11799865/1968>

.PHONY: help

## Display this list available rules
help:
	@echo "$$(tput bold)Default rule:$$(tput sgr0) ${.DEFAULT_GOAL}"
	@echo
	@echo "$$(tput bold)Available rules:$$(tput sgr0)"
	@echo
	@sed -n -e "/^## / { \
		h; \
		s/.*//; \
		:doc" \
		-e "H; \
		n; \
		s/^## //; \
		t doc" \
		-e "s/:.*//; \
		G; \
		s/\\n## /---/; \
		s/\\n/ /g; \
		p; \
	}" ${MAKEFILE_LIST} \
	| LC_ALL='C' sort --ignore-case \
	| awk -F '---' \
		-v ncol=$$(tput cols) \
		-v indent=19 \
		-v col_on="$$(tput setaf 6)" \
		-v col_off="$$(tput sgr0)" \
	'{ \
		printf "%s%*s%s ", col_on, -indent, $$1, col_off; \
		n = split($$2, words, " "); \
		line_length = ncol - indent; \
		for (i = 1; i <= n; i++) { \
			line_length -= length(words[i]) + 1; \
			if (line_length <= 0) { \
				line_length = ncol - indent - length(words[i]) - 1; \
				printf "\n%*s ", -indent, " "; \
			} \
			printf "%s ", words[i]; \
		} \
		printf "\n"; \
	}' \
	| more $(shell test $(shell uname) = Darwin && echo '--no-init --raw-control-chars')
