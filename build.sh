#/bin/bash
set -euox pipefail
pandoc -o readme.docx -f markdown -t docx README.md

zip -r -qq $BUILD_TAG-commit-$GIT_COMMIT-nodep.zip .

/bin/bash install_python.sh
source venv/bin/activate
# python -m unittest discover -v -p uTest*.py
python setup.py sdist bdist_wheel

/bin/bash install_node.sh
npm --prefix apitax/ah/web/node/node run build-jenkins

/bin/bash test.sh
#zip -r -qq $BUILD_TAG-commit-$GIT_COMMIT-dep.zip .
