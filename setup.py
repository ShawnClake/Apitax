from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install
from subprocess import check_call

class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        #check_call("apt-get install this-package".split())
        develop.run(self)

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        check_call("npm install --prefix apitax/ah/api/dashboard".split())
        check_call("npm run --prefix apitax/ah/api/dashboard build".split())
        install.run(self)
        
#class NPMInstall():
#    def run(self):
#        self.run_command('npm install --prefix apitax/ah/api/dashboard')
#        self.run_command('npm run --prefix apitax/ah/api/dashboard build')
#        build_py.run(self)

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name = 'Apitax',
  packages = find_packages(), # this must be the same as the name above
  version = '2.2.6',
  description = 'Apitax combines the power of Scriptax and Commandtax into a quick and easy to use Python package to facillitate powerful Restful API Request Scripting',
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'Shawn Clake',
  author_email = 'shawn.clake@gmail.com',
  url = 'https://github.com/ShawnClake/Apitax', # use the URL to the github repo
  keywords = ['restful', 'api', 'commandtax', 'scriptax'], # arbitrary keywords
  include_package_data=True,
  classifiers = (
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ),
  install_requires = [
    'click',
    'bottle',
    'requests',
    'antlr4-python3-runtime',
    'python-gitlab',
    'pygithub',
    'gitpython',
    'connexion == 1.1.15',
    'flask-jwt-extended',
    'python_dateutil == 2.6.0',
    'typing == 3.5.2.2',
  ],
  #cmdclass={
  #  'develop': PostDevelopCommand,
  #  'install': PostInstallCommand,
  #},
)
