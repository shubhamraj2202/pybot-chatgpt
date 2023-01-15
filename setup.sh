#!/bin/bash

# Install PipEnv
python3 -m pip install --user pipenv
# Install Dependencies
python3 -m pipenv install
# Sync Dev Dependencies
python3 -m pipenv sync -d
# Install Pre-Commit
python3 -m pipenv run pre-commit install
# Setup CI Test Requirements
python3 -m pipenv requirements --dev > .github/workflows/ci-test-requirements.txt
# Enter Shell
python3 -m pipenv shell
