zip -r -qq $BUILD_TAG-commit-$GIT_COMMIT-nodep.zip .
/bin/bash install.sh
python -m unittest discover -p uTest*.py
python setup.py sdist bdist_wheel
#zip -r -qq $BUILD_TAG-commit-$GIT_COMMIT-dep.zip .
