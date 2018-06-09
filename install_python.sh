#/bin/bash
set -euox pipefail
python3 -m venv venv
source venv/bin/activate
pip install wheel
pip install .


