zip -r -qq apitax-nodep-$BUILD_TAG-commit-$GIT_COMMIT.zip .
npm --prefix apitax/ah/web/node/node install
npm --prefix apitax/ah/web/node/node run build-jenkins
zip -r -qq apitax-dep-$BUILD_TAG-commit-$GIT_COMMIT.zip .