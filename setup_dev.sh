#!/bin/bash
python3 -m venv venv
source venv/bin/activate
pip install wheel setuptools
pip install .
python setup.py sdist bdist_wheel
set -euox pipefail
npm --prefix apitax/ah/api/dashboard install
npm --prefix apitax/ah/api/dashboard run build-jenkins