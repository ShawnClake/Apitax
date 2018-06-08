zip -r -qq $BUILD_TAG-commit-$GIT_COMMIT-nodep.zip .
npm --prefix apitax/ah/web/node/node install
npm --prefix apitax/ah/web/node/node run build-jenkins
zip -r -qq $BUILD_TAG-commit-$GIT_COMMIT-dep.zip .