python3 -m venv venv
source venv/bin/activate
pip install wheel
pip install .

npm --prefix apitax/ah/web/node/node install
npm --prefix apitax/ah/web/node/node run build-jenkins