#!/bin/bash
echo "here2"
python -m venv venv
source venv/bin/activate
pip install wheel setuptools
pip install .


