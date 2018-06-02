from distutils.core import setup
setup(
  name = 'apitax',
  packages = ['apitax'], # this must be the same as the name above
  version = '2.0.0',
  description = 'Apitax combines the power of Scriptax and COmmandtax into a quick and easy to use Python package to facillitate powerful Restful API Request Scripting',
  author = 'Shawn Clake',
  author_email = 'shawn.clake@gmail.com',
  url = 'https://github.com/ShawnClake/Apitax', # use the URL to the github repo
  download_url = '', # I'll explain this in a second
  keywords = ['restful', 'api', 'commandtax', 'scriptax'], # arbitrary keywords
  classifiers = [],
  install_requires = [
    'click',
    'bottle',
    'requests',
    'antlr4-python3-runtime',
  ],
)