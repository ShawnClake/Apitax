#/bin/bash
set -euox pipefail
source venv/bin/activate
python -m unittest discover -v -p uTest*.py
npm --prefix apitax/ah/web/node/node test