#/bin/bash
set -euox pipefail
zip -r -qq $BUILD_TAG-commit-$GIT_COMMIT-nodep.zip .
/bin/bash install.sh
source venv/bin/activate
python -m unittest discover -v -p uTest*.py
python setup.py sdist bdist_wheel
#zip -r -qq $BUILD_TAG-commit-$GIT_COMMIT-dep.zip .
